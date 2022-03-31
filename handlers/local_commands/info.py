import subprocess

VERSION = "0.2.0"


async def info(*_) -> str:
    subprocess.run("git fetch", shell=True)
    out = subprocess.run("git log origin/master -1 --pretty=format:%B",
                         shell=True, capture_output=True).stdout
    out = out.decode('utf-8').splitlines()
    if out[0] == VERSION:
        update_info = ''
    else:
        update_info = 'Доступно обновление! Новая версия: ' + out[0] + '\n'
        if len(out) > 1:
            update_info += 'Что нового:\n' + '\n'.join(out[2:]) + '\n\n'
    return (
        f"{update_info}LP модуль ver. {VERSION}\n"
        "Больше инфы в следующих сериях!"
    )