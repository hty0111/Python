import pygal
import random


class Die:
    """n面的骰子"""
    def __init__(self, n_sides):
        self.sides = n_sides

    def roll(self):
        return random.randint(1, self.sides)


die1 = Die(6)
die2 = Die(6)
results = []
for num in range(5000):
    results.append(die1.roll()+die2.roll())
frequencies = []
for value in range(2, die1.sides+die2.sides+1):
    frequencies.append(results.count(value))

hist = pygal.Bar()
hist.title = "Results of rolling two D6 5000 times"
hist.x_labels = [i for i in range(2, 13)]
hist.x_title = 'Results'
hist.y_title = 'Frequencies of results'
hist.add('D6+D6', frequencies)         # 图标
hist.render_to_file('myPygal.svg')

