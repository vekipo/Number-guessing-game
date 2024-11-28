from random import randint

print('Добро пожаловать в числовую угадайку')

def start_game():
    # Запрос диапазона в начале игры
    n = int(input('Выберите диапазон от 1 до n-го числа: '))
    generated_random_number = randint(1, n)  # Генерация случайного числа в выбранном диапазоне

    def game():  # Функция ввода данных и вывода некорректного входа данных
        while True:
            print(f'Введите целое число от 1 до {n}:')
            number = input()
            if check_text(number):
                return int(number)
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            if restart_game():
                continue
            else:
                break

    def check_text(number):  # Функция проверки входных данных
        return number.isdigit() and 1 <= int(number) <= n

    def number_check():  # Функция проверки введенного числа и подсчет попыток
        count = 0
        while True:
            count += 1
            user_number = game()  # Получаем введенное число
            if generated_random_number < user_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif generated_random_number > user_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Загаданное число было:', generated_random_number)
                print('Количество попыток:', count)
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break

    def restart_game():
        print('Хотите повторить игру?')
        restart = input('Чтобы повторить игру напишите - ДА, в ином случае - ENTER: ')
        if restart.lower() == 'да':
            return True
        else:
            return False

    number_check()

    # Запрос на перезапуск игры после окончания
    if restart_game():
        start_game()

# Запуск игры
start_game()