# LP модуль для IrCA Duty
LP модуль предоставляет дежурному информацию о сигналах самому себе вместо Iris CM, что позволяет использовать большинство команд дежурного в любых чатах.\
Данный модуль также обеспечивает работу игнора

## Установка
### Termux (эмулятор терминала для Android)
Вводи по очереди следующие команды:
```shell script
pkg install git
pkg install nano
pkg install clang
pkg install python
git clone https://github.com/elchinchel/icad_lp
cd icad_lp
pip install -r requirements.txt
python3 start.py
nano config.ini
```
## Настройка конфига
*Поле host нужно заполнять только в том случае, если calllabck модуль не на **pythonanywhere***
![](https://sun9-59.userapi.com/UbdxCZB2ar_COycjt8r4aKuui2N1iagUkjW_-A/KAG4gtp-qhs.jpg)\
*(**специально для мусаева: НЕ ТРОГАЙ СТРОКИ С КВАДРАТНЫМИ СКОБКАМИ**)*

Настройка завершена, команда для запуска: *`python3 start.py`*