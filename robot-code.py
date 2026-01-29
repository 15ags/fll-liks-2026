from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
# drive base
cat_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
kitten_motor = Motor(Port.B, Direction.CLOCKWISE)
front_cat = Motor(Port.F, Direction.COUNTERCLOCKWISE)
back_cat = Motor(Port.E, Direction.CLOCKWISE)
kitten = DriveBase(cat_motor, kitten_motor, 56, 120)
kitten.use_gyro(True)
# pid constants, WHY ARE THEY SO BIG?
kitten.heading_control.pid(kp=1500, ki=1000, kd=50)
kitten.settings(550, 550, 750, 750)
hub.imu.reset_heading(0)
kitten.reset()
# first path start
kitten.straight(12)
kitten.turn(90)
kitten.straight(238)
kitten.turn(8)
kitten.straight(-100)

front_cat.run_target(200, 0)
back_cat.run_target(200, 0)
front_cat.run_target(200, 200)
kitten.turn(-90)
back_cat.run_target(200, -300)
kitten.straight(-490)
kitten.straight(530)
back_cat.run_target(200, 0)
kitten.turn(90)
# wait for second path
wait(3500)

front_cat.run_target(999, 0)
front_cat.run_target(200, 78)

kitten.straight(610)
kitten.turn(-12)
kitten.straight(85)
front_cat.run_target(200, 208)
kitten.straight(-280)
kitten.turn(80)
front_cat.run_target(200, 18)
