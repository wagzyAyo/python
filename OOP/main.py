from robot import Robot

droid_1 = Robot("M-g30")
droid_2 = Robot("C-3p0")
droid_1.say_hi()
droid_2.say_hi()
Robot.robot_population()
droid_1.die()
Robot.robot_population()
droid_2.die()
Robot.robot_population()
