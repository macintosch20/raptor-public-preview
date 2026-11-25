"""One display-name rule for UI, chat and notifications; never an auth identifier."""
def text(value):
    value = str(value or '').strip()
    return '' if value.lower() in {'undefined','null','none','@'} else value


def display_name(user, *, fallback='Пользователь'):
    username = text(getattr(user,'username','')).lstrip('@').strip()
    if username: return '@' + username
    return text(getattr(user,'telegram_first_name','')) or text(getattr(user,'name','')) or fallback


def greeting(user):
    name = display_name(user, fallback='')
    return f'Здравствуйте, {name}!' if name else 'Здравствуйте!'
