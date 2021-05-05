import urwid


STRONG_LENGTH = 12
SCORE_STEP = 2


def is_very_long(password):
    return len(password) > STRONG_LENGTH


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def doesnt_consist_of_symbols(password):
    return any(char.isalnum() for char in password)


password_checks = [
    is_very_long,
    has_digit,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
    doesnt_consist_of_symbols,
]


def check_password(_, password):
    score = 0
    for check in password_checks:
        if check(password):
            score += SCORE_STEP
    reply.set_text(f"Рейтинг этого пароля: {score}")


def exit_on_esc(key):
    if key == "esc":
        raise urwid.ExitMainLoop()


if __name__ == "__main__":
    password = urwid.Edit("Введите пароль: ", mask='*')
    reply = urwid.Text("Рейтинг этого пароля: 0")
    exit_text = urwid.Text("\nНажмите ESC для выхода")
    menu = urwid.Pile([password, reply, exit_text])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', check_password)
    urwid.MainLoop(menu, unhandled_input=exit_on_esc).run()