from Controller import Controller
from WMS import WMS
from Robot import Robot
from Camera import Camera
from Charger import Charger
from Pod import Pod
from Lifter import Lifter
from Sensor import Sensor
from Wheels import Wheels

if __name__ == '__main__':
    print("Order has been received")

    # Create a new Order
    
    newOrder = WMS("134A38J", "drop","deck31","pod20")
    print(newOrder)


    # Start the order processing
    print("\nRunning the algorithm and coordinating the robot")
    
    c = Controller("calculate","start moving", "forward")
    c.move()

    #power on the robot and safety check
    r = Robot ('Kiva', 1000, 5, 4.5, 'qrcode90', 64, 12, 40)
    r.power()
    print ("\nRobot is powered on and starting from {} \nRobot temperature is {}F° \nRobot battery life is at {}%" .format(r._robotlocation,r._temperature,r._batterylife))

    #use sensors while operating
    s = Sensor(464, "24x37", "clear", "clear")
    s.bumperReader()
    s.infraredReader()
    s.fitDimension()
    s.stopRobot()
    print ()

    #Pick pod
    print("\nThe robot is picking up the pod!")
    l = Lifter (0,20,24)
    r1 = Robot ('Kiva', 1000, 5, 4.5, 'pod20', 57, 12, 43)
    l.lift()
    l.lower()
    s.measureWeight()
    if s.approveWeight()== True:
        print("\nRobot is has picked the pod at location {} \nRobot temperature is {}F° \nRobot battery life is at {}%" .format(r1._robotlocation,r1._temperature,r1._batterylife))
    
    # The robot will start moving to deliver the pod
    print("\nThe robot is adjusting its position!")
    wh = Wheels(45, "right")
    wh.forward()
    wh.backward()
    wh.turnLeft()
    wh.turnRight()
    wh.spin()
    wh.speedUp()
    wh.speedDown()
    wh.stopRobot()

    # Ordering the robot to move to the drop location
    c = Controller("calculate","deliver to operator", "forward")
    c.move()

    #Deliver pod
    r2 = Robot('Kiva', 1000, 5, 4.5, 'deck31', 50, 12, 47)
    print ("\nRobot is arriving at location {} \nRobot temperature is {}F° \nRobot battery life is at {}%" .format(r2._robotlocation,r2._temperature,r2._batterylife))
    print("\nThe robot has delivered the pod to the operator!")
    l = Lifter (20,12,24)
    l.lift()
    l.lower()