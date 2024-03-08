# LP модуль для IrCA Duty
LP модуль предоставляет дежурному информацию о сигналах самому себе вместо Iris CM, что позволяет использовать большинство команд дежурного в любых чатах.\
Данный модуль также обеспечивает работу игнора

# Установка
## Termux (эмулятор терминала для Android)
1) Заходим на https://f-droid.org/en/packages/com.termux/ и листаем до "Download APK" (НЕ ДО DOWNLOAD F-DROID), после чего скачиваем, устанавливаем и запускаем Termux.
2) Вводим команду:
```shell script
pkg install git clang python libexpat -y 
```
3) Вводим команду:
```shell script
git clone https://github.com/elchinchel/icad_lp
```
4) Вводим команду:
```shell script
cd icad_lp
```
5) Вводим команду:
```shell script
pip install -r requirements.txt
```
6) Вводим команду:
```shell script
python3 start.py
```
7) Следуем указаниям в терминале

Токен брать тут: http://vk.cc/9LuvMs
Имя пользователя на Pythonanywhere можно узнать, написав "Я" в лс https://vk.me/ircaduty. Имя пользователя - строка между "https://" и первой точкой.


В случае ошибки вида
```shell script
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.")': /simple/https/
Could not fetch URL https://pypi.org/simple/https/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/https/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping
ERROR: Could not find a version that satisfies the requirement https (from versions: none)
ERROR: No matching distribution found for https
```
1) Выполняем команду:
```shell script
pkg upgrade
```
2) Перезапускаем Termux
