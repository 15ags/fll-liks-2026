from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor

hub = PrimeHub()

front_cat = Motor(Port.F, Direction.COUNTERCLOCKWISE)
back_cat = Motor(Port.E, Direction.CLOCKWISE)
# run this code to put the motors to 0, then put on the robot attachments and u are ready for running the robot code
front_cat.run_target(200, 0)
back_cat.run_target(200, 0)
