from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
motor_speed = 300
# drive base
cat_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
kitten_motor = Motor(Port.B, Direction.CLOCKWISE)
front_cat = Motor(Port.F, Direction.COUNTERCLOCKWISE)
back_cat = Motor(Port.E, Direction.CLOCKWISE)
kitten = DriveBase(cat_motor, kitten_motor, 56, 120)
kitten.use_gyro(True)
# pid constants, WHY ARE THEY SO BIG?
kitten.heading_control.pid(kp=1500, ki=1000, kd=50)
kitten.settings(750, 650, 750, 750)
hub.imu.reset_heading(0)
kitten.reset()
# first path start
kitten.straight(14)
kitten.turn(90)
kitten.straight(219)
kitten.turn(8)
kitten.straight(-100)

# Push barrier
front_cat.run_target(motor_speed, 150)
kitten.turn(-100)
kitten.straight(123)
kitten.turn(-90)
back_cat.run_target(motor_speed, -300)
kitten.straight(-490)
kitten.straight(530)
back_cat.run_target(motor_speed, 0)
kitten.turn(90)

# return to left base
wait(3500)

front_cat.run_target(motor_speed, 67)

# Lift The Pin
kitten.straight(610)
kitten.turn(-10)
kitten.straight(75)
front_cat.run_target(motor_speed, 180)
kitten.straight(-280)
kitten.turn(80)
front_cat.run_target(motor_speed, 18)
