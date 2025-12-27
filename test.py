def login(username, password):
    try:
        assert username == "admin" and password == "1234", "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)

login("admin", "1234")     
login("user", "0000")       
