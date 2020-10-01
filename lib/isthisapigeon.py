# да, не очень, но работает и черт с ним
from typing import Union, Tuple


def _trydigit(val: str) -> Union[str, float, int]:
    try:
        num = float(val)
        if num % 1 == 0:
            return int(num)
        return num
    except ValueError:
        return val


def parse(data: str, save_format: bool = False) -> Union[dict, Tuple[dict, dict]]:  # noqa
    result = {}
    unprocessed = {}
    cur_field = None
    for i, line in enumerate(data.splitlines()):
        line = line.strip()
        if line == "":
            if save_format:
                unprocessed.update({i: line})
            continue
        if line[0] in {';', '#'}:
            if save_format:
                unprocessed.update({i: line})
            continue
        if line.startswith('['):
            result.update({line[1:-1]: None})
            cur_field = line[1:-1]
            continue
        if cur_field is None:
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            if type(result[cur_field]) == list:
                if type(result[cur_field][-1]) == dict:
                    result[cur_field][-1].update({key: _trydigit(value)})
                else:
                    result[cur_field].append({key: _trydigit(value)})
                continue
            if type(result[cur_field]) != dict:
                result[cur_field] = {}
            result[cur_field].update({key: _trydigit(value)})
            continue
        line = _trydigit(line)
        if type(result[cur_field]) == list:
            if line == '$':
                result[cur_field].append({})
                continue
            result[cur_field].append(line)
            continue
        if result[cur_field] is not None:
            result[cur_field] = [result[cur_field], line]
            continue
        if line == '&#null;':
            line = None
        result[cur_field] = line
    if save_format:
        return result, unprocessed
    return result


def _format(val: Union[str, float, int, dict], comments: dict = {}) -> list:
    result = []
    type_ = type(val)
    if type_ in {int, float}:
        return [str(val)]
    if type_ == str:
        return [val]
    if type_ == dict:
        result = []
        for key in val:
            if type(val[key]) == dict:
                raise ValueError('Nested dicts is not supported')
            result += [f'{key}={val[key]}']
        return result
    if val is None:
        return ['&#null;']
    raise ValueError('Nested lists is not supported')


def make(data: dict, unprocessed_lines: dict = {}) -> str:
    lines = []
    for key in data:
        value = data[key]
        field = []
        if type(value) in {list, tuple, set}:
            for i, item in enumerate(value):
                if type(item) == dict:
                    if i != 0:
                        if type(value[i-1]) == dict:
                            field += '$\n'
                field += _format(item)
        else:
            field = _format(value)
        lines += ([f'[{key}]'] + field)
    for pos in unprocessed_lines:
        lines = lines[:pos] + [unprocessed_lines[pos]] + lines[pos:]
    return '\n'.join(lines)
