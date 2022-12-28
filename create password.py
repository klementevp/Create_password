import random, string

# create the lists of symbols
digits = list(string.digits[1:])
lowercase_letters = [elem for elem in string.ascii_uppercase if elem not in 'OI']
uppercase_letters = [elem for elem in string.ascii_lowercase if elem not in 'ol']
punctuation = [elem for elem in string.punctuation if elem not in '\\']

# create the dictionary: keys - questions, values - lists of symbols
choice_chars = {'Включить цифры? (д = да, н = нет) ': digits,
                'Включить прописные буквы? (д = да, н = нет) ': uppercase_letters,
                'Включить ЗАГЛАВНЫЕ буквы? (д = да, н = нет)? ': lowercase_letters,
                'Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ': punctuation}


# the function checks the correctness of the answer
def is_answer(answer):
    if answer.lower() in ('д', 'н', 'да', 'нет'):
        return True
    else:
        return False


# the function determines the length of the password
def choice_length():
    global length
    while True:
        length = input('Какая требуется длина пароля?' + '\n')
        if length.isdigit():
            length = int(length)
            if length < 6:
                print('Длина пароля меньше 6 знаков. Рекомендуем минимум 8 знаков.')
            else:
                print('Ваше пожелание по длине пароля принято в работу!')
                return length
        else:
            print('Это не число. Введите, пожалуйста, корректное число')


# the function determines the choice of symbols
def choiсe_chars():
    global choicen_chars
    choicen_chars = []
    for txt, choice in choice_chars.items():
        while True:
            response = input(txt + '\n').lower()
            if not is_answer(response):
                print("Твой ответ некорректен. Введи 'д' либо 'н'")
                continue
            else:
                print(random.choice(['Принято!', 'Хорошо!', 'Учтем!', 'OK!', 'Ладушки!', 'Пожелание услышано!']))
                if response[0] == 'д':
                    choicen_chars.append(choice)
                break
    return choicen_chars


# the function generates the random password
def generate_password(length, choicen_chars):
    password = [random.choice(row) for row in choicen_chars]
    password += [random.choice(choicen_chars[random.randint(0, len(choicen_chars) - 1)]) for _ in
                 range(length - len(choicen_chars))]
    random.shuffle(password)
    return ''.join(password)


# the function generates the desired password based on the user's requests
def create_password():
    choice_length()
    while True:
        choicen_chars = choiсe_chars()
        if choicen_chars:
            return generate_password(length, choicen_chars)
        else:
            print('Не выбраны символы... Я не знаю из каких элементов составить пароль')
            print('Давай попробуем заново!')


print('Приветствую! Сейчас мы вместе создадим самый сильный пароль')

# create a loop that generates a password until it receives a termination response
answer = 'первый запрос'  # for the first query
while answer != 'н':
    if answer != 'первый запрос':  # query, for non-first loop
        answer = input(
            '\n' + 'Предложить новый пароль? (н = нет, д = да, т = задать новые требования к длине и символам)' + '\n')
    if is_answer(answer) or answer == 'т' or answer == 'первый запрос':
        if answer == 'д':  # create the password again
            print('Предлагаемый пароль:\n' + generate_password(length, choicen_chars))
        elif answer == 'т' or answer == 'первый запрос':  # create password with new requirements or for the first query
            answer = ''
            print('Предлагаемый пароль:\n' + create_password())
        else:
            print('Спасибо за работу! Обращайся снова :)')
    else:
        print('Я не понял твой ответ. Ответь, пожалуйста, заново')
