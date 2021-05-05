# Оцениваем пароли

Скрипт проверяет надёжность пароля по шкале от 0 до 14.

## Запуск скрипта

Чтобы запустить скрипт нужен Python 3.6 и библиотека urwid.  
Установить нужные зависимости можно следующей командой:

```bash
$ pip install -r requirements.txt
```
Теперь можно проверить пароль. Выполните следующую команду в терминале и вводите пароль:

```bash
$ python main.py
```
Пример вывода:

```bash
Введите пароль: **********
Рейтинг этого пароля: 12

Нажмите ESC для выхода
```

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python на [Devman](https://dvmn.org).  