# Программа просит ввести пароль для регистрации. Пароль должен быть длиною минимум 8 символов или более. Должен
# состоять только из букв и начинаться с заглавной буквы
password = input('Введите пароль: ')
len_password = len(password)
if len_password >= 8 and password.istitle() and password.isalpha():
    print('Регистрация прошла успешно')
elif len_password < 8 and password.istitle() and password.isalpha():
    print('Пароль меньше 8 символов')
elif len_password >= 8 and password.istitle():
    print('Пароль должен начинаться с заглавной буквы ')
elif len_password >= 8 and password.isalpha():
    print('Пароль должен состоять из букв')
else:
    print('Пароль не соответствует требованиям. Попробуйте снова')









