from Camera import Camera
"""
 * @author ricardonolasco
 *
"""

class Sensor:
    
    def __init__ (self, weights, dimensions, bumperreadings, infraredreadings):
        self._weights = weights # the weight of the item or pod the robot has to pick (in pounds)
        self._dimensions = dimensions # the dimension detected for the robot to adjust and drop or pick a item (in inches)
        self._bumperreadings = bumperreadings # bumper readings can be: obstacle or clear
        self._infraredreadings = infraredreadings # infrared readings can be: obstacle or clear

    """
     * @order the robot to lift
    """
    def measureWeight(self):
        return ("The item or pod weight is {} pounds" .format(self._weights))
    """
     * @order the robot to lower its lifter
    """
    def approveWeight(self):
        weightlimit = 1000
        if self._weights <= weightlimit:
            print ("The weight is approved and the robot can pick up the item or pod")
            return True
        else:
            print ("The item or pod is too heavy for the robot")
    """
     * @order the robot to lower its lifter
    """
    def bumperReader(self):
        return ('The bumper reading is: {}' .format(self._bumperreadings))
    """
     * @order the robot to lower its lifter
    """
    def infraredReader(self):
        return ('The infrared reading is: {}' .format(self._infraredreadings))
    """
     * @order the robot to lower its lifter
    """
    def fitDimension(self):
        return ('Adjust the robot to fit the pickup or drop location dimension of: {}' .format(self._dimensions))
    """
     * @order the robot to lower its lifter
    """
    def stopRobot(self):
        if self._bumperreadings or self._infraredreadings == "obstacle":
            return ('Stop the robot. Obstacle ahead')