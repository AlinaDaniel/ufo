from ufo import *
import turtle as tr
import random

amount_of_ufos = 15

tr.tracer(0)
colors = ['violet', 'lightblue', 'green', 'pink', 'red', 'orange', 'purple']
ufos = [Ufo(name='ПРИШЕЛЕЦ-' + str(i+1), x=random.randint(-300, 300), y=random.randint(-300, 300),
        size=random.randint(30, 200), color=colors[random.randint(0, len(colors) - 1)],
        count_pillars=random.randint(2, 5), count_lamps=random.randint(2, 5), speed=random.randint(10, 500))
        for i in range(amount_of_ufos)]
while True:
    for ufo in ufos:

        ufo.random_travel()
tr.done()
