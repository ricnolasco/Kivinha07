"""
 * @author ricardonolasco
 *
"""

class Charger:
    
    def __init__ (self, chargerlocation, status, chargetime):
        self._chargerlocation = chargerlocation # location of the robot charger
        self._status = status   # tells if the charger requested status: available or unavailable
        self._chargetime = chargetime # time to fully recharge robot (in minutes)
    """
     * @provide instructions for the robot charge request
    """
    def chargeBattery(self):
        if self._status == "available":
            return ("The charger located at {} is {}, and the time to recharge the robot is {} minutes" .format(self._chargerlocation, self._status, self._chargetime))
        elif self._status == "unavailable":
            return ("Charger is currently in use. Choose another charger.")
