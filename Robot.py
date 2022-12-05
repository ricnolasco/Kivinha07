from Sensor import Sensor
from Lifter import Lifter
from Wheels import Wheels
"""
 * @author ricardonolasco
 *
"""

class Robot:
    
    def __init__ (self, model, weightlimit, speedlimit, robotdimension, robotlocation, batterylife, minimumbattery, temperature):
        self._model = model # the model of the robot
        self._weightlimit = weightlimit   # the weight limit capacity of the robot, (in pounds)
        self._speedlimit = speedlimit # the speed limit of the robot, (in km per hour)
        self._robotdimension = robotdimension # the dimension of the robot, (in feet2)
        self._robotlocation = robotlocation # the location of the robot
        self._batterylife = batterylife # the battery life precentage of the robot
        self._minimumbattery = minimumbattery # the minimum battery percentage before the robot has to charge
        self._temperature = temperature # the temperature of the robot (in fahrenheits)
    
    """
     * Power on the robot
    """
    def power(self):
        pass
    
    """
     * @return the battery of the robot
    """
    def measureBattery(self):
        return ('battery: {}' .format(self._batterylife))

    """
     * @set the robot to cool down its temperature
    """
    def robotCooling(self):
        return ("past temperature: {} new temperature: {}".format(self._temperature, self._temperature-20))