# LP модуль для IrCA Duty
LP модуль предоставляет дежурному информацию о сигналах самому себе вместо Iris CM, что позволяет использовать большинство команд дежурного в любых чатах.\
Данный модуль также обеспечивает работу игнора

# Установка
## Termux (эмулятор терминала для Android)
Вводи по очереди следующие команды:
```shell script
pkg install git clang python
git clone https://github.com/elchinchel/icad_lp
cd icad_lp
pip install -r requirements.txt
python3 start.py
```
