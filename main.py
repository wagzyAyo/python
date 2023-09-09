class Robot:
    population = 0

    def __init__(self, name):
        """Initializing new robot"""
        self.name = name
        print("Initializing new Robot")
        print("Hello my masters call me {}".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is dieing".format(self.name))
        print("{} is destroyed".format(self.name))

        Robot.population -= 1

    def say_hi(self):
        print("Hi my name is {} what can i do for you today".format(self.name))

    @classmethod
    def robot_population(self):
        print("There are {} robots available".format(Robot.population))


droid_1 = Robot("M-g30")
droid_2 = Robot("C-3p0")
droid_1.say_hi()
droid_2.say_hi()
Robot.robot_population()
droid_1.die()
Robot.robot_population()
