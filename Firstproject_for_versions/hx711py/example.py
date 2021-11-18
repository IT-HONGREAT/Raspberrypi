#! /usr/bin/python2

import time
import sys


EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from .hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(20, 16)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")


def make_weight():

    data_weight = 0
    count = 0
    while True:
        try:
            val = hx.get_weight()
            ave_weight = 724

            output_weight = int(val/ave_weight)


            if -1 <= output_weight <= 1:
                print("zeros : ", output_weight)
                count = 0
            else:
                count += 1
                print("weight : ", output_weight)
                if count == 2:
                    data_weight = output_weight
                    return data_weight


                print('data_weight:',data_weight)
            # if data_weight >=10:
            #     # break
            #
            #     return data_weight
            hx.power_down()
            hx.power_up()
            time.sleep(0.1)

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

make_weight()





