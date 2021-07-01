import gpiozero
import time


motorLeft = gpiozero.PhaseEnableMotor(17,23)
motorRight = gpiozero.PhaseEnableMotor(27,24)


motorLeft.forward(0.8)

input()

motorLeft.forward(0.4)

input()


motorLeft.forward(0.5)

input()

motorLeft.forward(0.6)

input()
motorLeft.forward(0.7)

input()
motorLeft.forward(0.8)

input()
