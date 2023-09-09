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

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working".format(
                Robot.population))

    def say_hi(self):
        print("Hi my name is {} what can i do for you today".format(self.name))

    @classmethod
    def robot_population(cls):
        print("There are {} robots available".format(cls.population))
