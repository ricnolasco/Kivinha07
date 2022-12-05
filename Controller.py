from Robot import Robot
from Pod import Pod
from Charger import Charger
"""
 *
 * @author ricardonolasco
 *
"""

class Controller:
    
    def __init__ (self, algorithm, algorithmdecision, movementdirections):
        self._algorithm = algorithm # the algorithm running on the controller of the robot
        self._algorithmdecision = algorithmdecision   # the algorithm decision
        self._movementdirections = movementdirections # the movement directions for the robot

    """
     * @return the direction for the robot to move
    """
    def move(self):
        return ("direction: {}" .format(self._movementdirections))
    
    """
     * @return the decision made for the robot
    """
    def runAlgorithm(self):
        return ('decision: {}' .format(self._algorithmdecision))