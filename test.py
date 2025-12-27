def login(username, password):
    try:
        assert username == "admin" and password == "1234", "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)

user = input("Введіть ім'я користувача: ")
pwd = input("Введіть пароль: ")

login(user, pwd)
