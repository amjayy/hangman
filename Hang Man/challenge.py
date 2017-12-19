flying_animals= 'canary', 'robin', 'mockingbird', 'bat','fly', 'butterfly', 'lovebug','ladybug','dragonfly','parrot'.split()
water_animals = 'salmon', 'starfish', 'oyster', 'crab', 'lobster', 'eel', 'octopus', 'shark', 'whale','clown_fish'.split()
land_animals = 'dogs', 'cats', 'horses', 'pigs', 'chickens', 'cows', 'sheep', 'lambs', 'kangaroos', 'lizards'.split()


def pick_a_category():
    category = input( " Please choose a category ")
    category_land_animals = land_animals.split()
    category_water_animals = water_animals .split()
    category_flying_animals = flying_animals.split()

    resulting_animal= ' '

    for i in resulting_animal :
        resulting_animal +=i.capitialize()
        resulting_animal += ' '

    return resulting_animal.strip()
