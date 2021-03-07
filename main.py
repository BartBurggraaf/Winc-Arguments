# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greet='Hello, <name>!'):
    greet_name = greet
    greet_name = greet_name.replace("<name>", name)
    return greet_name


print(greet('doc'))

# force = mass*gravity


def force(mass, body='earth'):
    planet_gravity = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    gravity = planet_gravity[body]
    force = mass*gravity
    return force


print(force(10))

# pull = G*((m1*m2)/d**2)


def pull(m1, m2, d):
    g = 6.674*10**-11
    gravitational_pull = g*((m1*m2)/d**2)
    return gravitational_pull


print(pull(0.1, 5.972*10**24, 6.371*10**6))
