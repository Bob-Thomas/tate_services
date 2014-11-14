from flask.ext import login


def check_roles(roles):
    for role in roles:
        if role in login.current_user.get_roles():
            return True
    return False