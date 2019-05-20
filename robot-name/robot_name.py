import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
class Robot(object):
    def __init__(self):
        self.used = []

    def name(self):
        let = random.sample(alphabet, 2)
        num = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)
        name = ''.join((let + num))


        if name in self.used:
            Continue
        else:
            self.used.append(name)
            return name

    def reset(self):
        for name in self.used:
            name.pop


