# Guido van Rossum <guido@python.org>
import random as rn
import time


def check_weather():
    seasons = ['☀', '⛈', '❄']
    weather = rn.choice(seasons)
    return weather


class Duck:
    name = 'Говорящая утка'
    profession = 'Маляр'
    bag = '🍺'
    photo = '🦆'
    anger = 1
    health = 50

    def look(self):
        return self.photo + self.bag

    def kick(self):
        return round((1 + self.anger) * rn.random(), 2)


class Criminal:
    name = 'Васёк'
    bag = '🍺'
    photo = '👿'
    anger = 10
    health = 10

    def look(self):
        return self.photo + self.bag

    def kick(self):
        return round(5 * rn.random(), 2)


def you_loose(duck):
    print(f'{duck.name} чувствует себя как-то нехорошо.')
    time.sleep(1.6)
    print('#############################################\n'
          '############ G A M E  O V E R ###############\n'
          '#############################################')


def you_win(duck):
    print(f'{duck.name} счастлив, как никогда ранее.')
    time.sleep(1.6)
    print('#############################################\n'
          '############## Y O U  W I N   ###############\n'
          '#############################################')


def stats(person):
    return f'♥:{person.health} 😠:{person.anger} - {person.look()} - {person.name}'


def drink_beer(duck):
    duck.health = round(duck.health * 0.7, 2)
    duck.bag = ''
    print(f'{stats(duck)} залпом выпивает 🍺. Оно так себе влияет на здоровье')
    time.sleep(1.6)
    return


def step1(duck):
    print(
        'Уткамаляр 🦆 решила погулять. '
        'Взять ей зонтик? ☂️'
    )

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        duck.bag = '☂'
    return step2(duck)


def step2(duck):
    while duck.health > 0:
        weather = check_weather()
        print(f'{weather} - {stats(duck)} гуляет')
        time.sleep(1.6)
        if weather == '☀':
            print(f'{weather} - {stats(duck)} говорит: "В такую чудесную погоду бахнуть бы 🍺!"')
            time.sleep(1.6)
            return step3_beer(duck)
        if weather == '⛈':
            print(f'{weather} - {stats(duck)} говорит: "Дождь как из ведра, спасацца!!11" \n')
            time.sleep(1.6)
            duck.anger += 1
            if duck.bag != '☂':
                print(f'{duck.name} сегодня без зонта. Дождь больно бьет по перьям утки, нанося урон -1.')
                time.sleep(1.6)
                duck.health -= 1
            else:
                print(f'Молния попадает прямо в зонтик! \n {stats(duck)} невредима, но просто в ярости!')
                duck.anger += 5
            print(f'Спасаясь от непогоды, {duck.name} забегает в цирк.')
            time.sleep(1.6)
            return step5_circus(duck)
        else:
            print(f'{weather} - {stats(duck)} молча гуляет')
            time.sleep(1.6)
            gopnik = Criminal()
            return step4_gopnik(duck, gopnik)
    you_loose(duck)


def step3_beer(duck):
    items = list(duck.bag)
    try:
        items.remove('🍺')
        drink_beer(duck)
        return step2(duck)
    except ValueError:
        duck.anger = round(duck.anger * 1.7, 2)
        duck.health = round(duck.health * 0.9, 2)
        print(f'{stats(duck)} грустит: в сумке что-то не то. нужно раздобыть пивка')
        time.sleep(1.6)
        return step2(duck)


def step4_gopnik(duck, gopnik):
    print(f'{stats(duck)} неспешно прогуливался по парку, когда на него внезапно напали')
    time.sleep(1.6)

    while duck.health > -1 and gopnik.health > 0:
        enemies = {gopnik, duck}
        for enemy in enemies:
            damage = round(enemy.kick(), 2)
            other_enemy = list(enemies.difference({enemy, }))[0]
            print(f'{stats(enemy)} наносит удар. Урон -{damage}')
            time.sleep(1.6)
            other_enemy.health -= damage

    if duck.health < 0:
        return you_loose(duck)
    else:
        print(f'{gopnik.name} повержен. Из него дропается {gopnik.bag}.')
        time.sleep(1.6)
        duck.bag = gopnik.bag
        return step2(duck)


def step5_circus(duck):
    today_vacancy = rn.choice(['Говорящая утка', 'Маляр'])

    print('\nЦиркач: как здорово, что вы зашли. У нас как раз открыта кое-какая вакансия.')
    time.sleep(1.6)
    print('Циркач: кто-вы?')

    option = ''
    options = {'1', '2'}

    while option not in options:
        print('Выберите: \n '
              '1 - назвать имя.\n 2 - назвать профессию.'.format(*options))
        option = input()

        if option == '1':
            answer = duck.name
        else:
            answer = duck.profession

        print(f'{duck.name}: я не просто какой-то там обычный человек, я - {answer}')
        time.sleep(1.6)

        if answer == today_vacancy:
            print(f'Циркач: какая удача что вы зашли к нам, уважаемый товарищ {answer}! Выходите на работу сегодня же!')
            time.sleep(1.6)
            return you_win(duck)
        else:
            print(f'Циркач: ааа, опять {answer}! Таких как вы тут толпы ходят! \n'
                  f'Сегодня мы ищем действительно редкого работника - нам нужен {today_vacancy}! \n'
                  f'Приходите потом')
            time.sleep(1.6)
            duck.anger += 2
            return step2(duck)


if __name__ == '__main__':
    Utka_Malyar = Duck()
    step1(Utka_Malyar)
