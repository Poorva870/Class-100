class Car(object):
    """
    blueprint for a car
    """
    def __init__(self, model, color, company, speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print('started')

    def stop(self):
        print('stoped')

    def accelerate(self):
        print('accelerating')
        "accelerated functionality here"

    def change_gear(self, gear_type):
        print('gear changed')
        "gear related functionality here"

audi=Car('A6', 'red', 'audi', 80)

print(audi.color)
