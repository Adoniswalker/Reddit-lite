def check_if_user_exists(user_list, username, email):
    """check if the username or email has already been used"""

    for item in user_list:
        if item[3] == username:
            return 'Sorry, This username has already been taken'
        if item[4] == email:
            return 'Sorry, This email is already in use'