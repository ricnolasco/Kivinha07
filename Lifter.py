"""
 * @author ricardonolasco
 *
"""

class Lifter:
    
    def __init__ (self, height, liftheight, maximumheight):
        self._height = height # current height of the robot lifter
        self.__liftheight = liftheight # the height that the robot lifter has to reach (in inches)
        self._maximumheight = maximumheight   # the maximum height the robot lifter can operate in a safe mode (in inches)

    """
     * @order the robot to lift
    """
    def lift(self):
        while self.__liftheight > self._height:
            if self.__liftheight > self._maximumheight:
                return ("Lift the robot until {} inches" .format(self._maximumheight))
            elif self.__liftheight <= self._maximumheight:
                return ("Lift the robot until {} inches" .format(self.__liftheight))
            break
    """
     * @order the robot to lower its lifter
    """
    def lower(self):
        if self.__liftheight < self._height:
            return ('Lower the lift until {} inches' .format(self.__liftheight))