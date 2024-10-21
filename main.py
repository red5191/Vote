print("Пройдите простой тест чтобы узнать можно ли вам голосовать.", '\n')

age = 'Вы старше 18? '
citizenship = 'У вас актуальное гражданство? '
disqualified = 'Вы освобождены от уголовного преследования? '
again = 'Ещё раз? '

QAs_list = [age, citizenship, disqualified, again]
QAs_dict = {
    age: 'Вы слишком молоды и не можете голосовать',
    citizenship: 'Вы не гражданин, и не можете голосовать.',
    disqualified: 'Вам запрещено голосовать до прекращения уголовного преследования',
    again: 'Тестирование завершено.'
}


def test(QA):
    correct = ['да', 'нет']
    answer = input(QA).lower()
    while answer not in correct:
        print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
        answer = input(QA).lower()
    if answer == 'да':
        return True


def vote_test():
    for n, qa in enumerate(QAs_dict):
        if not test(qa):
            print(QAs_dict.get(QAs_list[n]))
            break
        elif n == 2:
            print('Поздравляем! Вы можете голосовать.', '\n')
            break

vote_test()

while test(again) == True:
    vote_test()
else:
    print(QAs_dict.get(again))

