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
kitten.heading_control.pid(kp=1500, ki=100, kd=50)
kitten.distance_control.pid(kp=1500, ki=100, kd=50)
kitten.settings(750, 650, 750, 750)
hub.imu.reset_heading(0)
kitten.reset()
# first path start
kitten.straight(10000)
