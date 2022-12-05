"""
 * @author ricardonolasco
 *
"""

class Wheels:
    
    def __init__ (self, spinangle, action):
        self.__spinangle = spinangle # gives the angle coordinates for the robot to spin (in degrees)
        self._action = action   # gives the action the robot needs to perform.. actions can be: forward, backward, right, left, stop, speedup, speeddown
    """
     * @order the robot to move forward
    """
    def forward(self):
        if self._action == "forward":
            return ('Move forward')
    """
     * @order the robot to move backwards
    """
    def backward(self):
        if self._action == "backward":
            return ('Move backward')
    """
     * @@order the robot to turn left
    """
    def turnLeft(self):
        if self._action == "left":
            return ('Turn left')
    """
     * @order the robot to turn right
    """
    def turnRight(self):
        if self._action == "right":
            return ('Turn right')
    """
     * @order the robot to spin in a specic angle direction
    """
    def spin(self):
        if self.__spinangle == 0:
            return ("Do not spin")
        else:
            return ('Spin at {} degrees' .format(self.__spinangle))
    """
     * @order the robot to increase its speed
    """
    def speedUp(self):
        if self._action == "speedup":
            return ('Increase robot speed until maximum speed')
    """
     * @order the robot to reduce its speed
    """
    def speedDown(self):
        if self._action == "speeddown":
            return ('Reducing robot speed before stopping')
    """
     * @order the robot to stop moving
    """
    def stopRobot(self):
        if self._action == "stop":
            return ('Stop robot')