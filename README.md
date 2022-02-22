# LP модуль для IrCA Duty
LP модуль предоставляет дежурному информацию о сигналах самому себе вместо Iris CM, что позволяет использовать большинство команд дежурного в любых чатах.\
Данный модуль также обеспечивает работу игнора

# Установка

## Heroku
1. [Регистрируемся на Heroku](https://signup.heroku.com/) (кликабельно)
2. После регистрации и подтверждения почты идем в [billing](https://dashboard.heroku.com/account/billing)
3. Жмём на _Add credit card_ и вводим данные своей карты (Qiwi подойдёт)
*если нет карты, то после истечения бесплатных часов создаем второй аккаунт; 
когда кончатся часы на втором, возвращаемся на первый
4. Жмем на кнопку: [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Elchinchel/ICAD-Longpoll) <!--Если хочешь протестить то https://heroku.com/deploy?template=https://github.com/Obnovlator3000/ICAD-Longpoll-->
5. В поле "App name" вписываем что угодно маленькими буквами без пробелов, лишь бы понравилось Heroku
6. В "Choose a region" выбираем Europe
7. В поле "host" вписываем имя аккаунта на Pythonanywhere; если же дежурный не на PA, то вписываем хост
8. В поле "token" вписываем токен (спасибо, кэп) от Kate Mobile, взять можно [тут](https://oauth.vk.com/authorize?client_id=2685278&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1)
 !!!ВНИМАНИЕ!!! Скопируйте часть адресной строки от access_token= до &expires_in
9. Жмем на "Deploy app" и ждём окончания загрузки
10. После окончания загрузки пишем в любом чате ".лп пинг", если работает, то поздравляю, ты восхитителен, если же нет, то добро пожаловать в беседу помощи

## Termux (эмулятор терминала для Android)
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
### Настройка конфига
*Поле host нужно заполнять только в том случае, если calllback модуль не на **pythonanywhere***
![](https://sun9-59.userapi.com/UbdxCZB2ar_COycjt8r4aKuui2N1iagUkjW_-A/KAG4gtp-qhs.jpg)\
*(**специально для мусаева: НЕ ТРОГАЙ СТРОКИ С КВАДРАТНЫМИ СКОБКАМИ**)*

Настройка завершена, команда для запуска: *`python3 start.py`*

