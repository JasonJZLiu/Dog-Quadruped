from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

#for x in range(16): 
#    kit.servo[x].set_pulse_width_range(130, 600)

# for x in range(12): 
#     kit.servo[x].angle = 90 

# while True:
#    for i in range(30, 130):
#        kit.servo[0].angle = i
#    for i in range (130, 30):
#        kit.servo[0].angle = i

print("--servo calibration--")

kit.servo[1].angle =100 
kit.servo[2].angle =170 
kit.servo[3].angle = 50 

kit.servo[4].angle = 45 #positive is ccw
kit.servo[5].angle =80 
kit.servo[6].angle = 170 

kit.servo[8].angle =95 #positive is ccw 
kit.servo[9].angle = 120 #positive is cw
kit.servo[10].angle =95 

kit.servo[12].angle=115 #positive is cw
kit.servo[13].angle=45  #positive is ccw
kit.servo[14].angle=97




