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
kitten.heading_control.pid(kp=6500, ki=3000, kd=100)
kitten.settings(350, 350, 350, 350)
hub.imu.reset_heading(0)
kitten.reset()
front_cat.run_target(200, 0)
back_cat.run_target(200, 0)
wait(500)

# path1 start
"""kitten.straight(600)
front_cat.run_target(motor_speed, 70)
kitten.settings(650, 650, 500, 750)
kitten.turn(-150)
wait(100)
kitten.turn(150)
kitten.settings(350, 350, 350, 350)
kitten.straight(-600)
front_cat.run_target(motor_speed, 0)

kitten.stop()
wait(2500)
hub.imu.reset_heading(0)
# second path start
kitten.straight(14)
kitten.turn(90)
kitten.straight(263)
kitten.turn(8)
kitten.straight(-75)

# Push barrier
front_cat.run_target(motor_speed, 120)
kitten.turn(-100)
kitten.straight(110)
kitten.turn(-90)
back_cat.run_target(motor_speed, -300)
kitten.settings(650, 650, 750, 750)
kitten.straight(-490)
kitten.settings(350, 350, 350, 350)
# return to left base
kitten.straight(530)
front_cat.run_target(motor_speed, 0)
back_cat.run_target(motor_speed, 0)


# path 3 setup
kitten.stop()
wait(7000)
hub.imu.reset_heading(0)


# path 3
front_cat.run_target(motor_speed, 90)
kitten.straight(700)
kitten.turn(-37)
kitten.straight(110)
front_cat.run_target(motor_speed, 190)
kitten.straight(-110)
kitten.turn(37)
kitten.straight(-390)
kitten.turn(50)
kitten.straight(150)
front_cat.run_target(motor_speed, 90)
kitten.straight(-550)
back_cat.run_target(motor_speed, 0)
front_cat.run_target(motor_speed, 0)

# path 4 setup
kitten.stop()
wait(3000)
hub.imu.reset_heading(0)

# path 4
front_cat.run_target(motor_speed, 90)
kitten.straight(200)
kitten.turn(30)
kitten.straight(515)
kitten.turn(-120)
kitten.straight(110)
front_cat.run_target(motor_speed, 190)
kitten.straight(-100)
kitten.turn(90)
kitten.straight(-400)
kitten.turn(40)
kitten.straight(150)
front_cat.run_target(motor_speed, 50)
kitten.straight(-400)
back_cat.run_target(motor_speed, 0)
front_cat.run_target(motor_speed, 0)

# path 5 setup
kitten.stop()
wait(2000)
hub.imu.reset_heading(0)"""

# path 5
kitten.straight(300)
kitten.turn(35)
kitten.straight(500)
kitten.turn(55)
front_cat.run_target(motor_speed, 170)
back_cat.run_target(motor_speed, -290)
kitten.straight(265)
kitten.turn(90)
kitten.straight(-30)
back_cat.run_target(motor_speed, -100)
kitten.straight(-30)
back_cat.run_target(motor_speed, -30)
kitten.straight(10)
back_cat.run_target(motor_speed, 0)
kitten.turn(90)
kitten.straight(-610)
kitten.turn(90)
back_cat.run_target(motor_speed, -100)
kitten.straight(-30)
