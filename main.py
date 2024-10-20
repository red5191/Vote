print("Пройдите простой тест чтобы узнать можно ли вам голосовать.", '\n')


def vote_test():
    def age_test():
        while True:
            try:
                age = int(input("Введите количество полных лет "))
                break
            except ValueError:
                print('Пожалуйста используйте целое число')
        return age

    def citizenship_test():
        correct = ['да', 'нет']
        citizenship = input("Вы гражданин? ")
        while citizenship not in correct:
            print('Пожалуйста используйте для ответа \"да\" или\"нет\"')
            citizenship = input("Вы гражданин? ")
        return citizenship

    def disqualified_test():
        correct = ['да', 'нет']
        disqualified = input("Вы находитесь под уголовным преследованием? ")
        while disqualified not in correct:
            print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
            disqualified = input("Вы находитесь под уголовным преследованием? ")
        return disqualified

    age_input = age_test()
    if age_input < 18:
        print('Вы ещё слишком молоды, и не можете голосовать.', '\n')
    else:

        citizenship_input = citizenship_test()
        if citizenship_input != 'да':
            print('Вы не гражданин, и не можете голосовать.', '\n')
        else:

            disqualified_input = disqualified_test()
            if disqualified_input == 'да':
                print('Вам запрещено голосовать до прекращения уголовного преследования.', '\n')
            else:
                print('Поздравляем! Вы можете голосовать.', '\n')


vote_test()


def repeater():
    while True:
        correct = ['да', 'нет']
        repeater_input = input("Ещё раз? ")
        while repeater_input not in correct:
            print('Пожалуйста используйте для ответа \"да\" или\"нет\"')
            repeater_input = input("Ещё раз? ")
        if repeater_input == 'да':
            vote_test()
        elif repeater_input == 'нет':
            print('Тестирование завершено.')
            break


repeater()
