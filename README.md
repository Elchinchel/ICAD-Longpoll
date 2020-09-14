# LP модуль для IrCA Duty
LP модуль предоставляет дежурному информацию о сигналах самому себе вместо Iris CM, что позволяет использовать большинство команд дежурного в любых чатах.\
Данный модуль также обеспечивает работу игнора

## Установка
### Termux (эмулятор терминала для Android)
Вводим по очереди команды
```shell script
pkg install git
pkg install python
git clone https://github.com/elchinchel/icad_lp
cd icad_lp
pip install -r requirements.txt
nano config.ini
```
*Вставляй токен и ссылку на сайт или имя пользователя*

Настройка завершена, команда для запуска: *`python3 start.py`*