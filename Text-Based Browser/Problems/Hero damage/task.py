hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = hero_damage * 2
    print(hero_damage)


def disarmed():
    global hero_damage
    hero_damage = (hero_damage / 100) * 90
    print(hero_damage)


def power_potion():
    global hero_damage
    hero_damage += 100
    print(hero_damage)

double_damage()
disarmed()
power_potion()