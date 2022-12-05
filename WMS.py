from Controller import Controller
"""
 * This is the main WMS class that receives order information and 
 communicates with the robot controller
 * 
 * Includes a main method that runs the application
 * 
 * @author ricardonolasco
 *
"""

class WMS:
    
    def __init__ (self, order, operationtype, droplocation, pickuplocation):
        self.__order = order # the order id
        self._operationtype = operationtype   # the operation type to be performed (drop or ship)
        self._droplocation = droplocation # the location for the robot to drop the item at
        self._pickuplocation = pickuplocation # the location for the robot to pickup the item at

    """
    * @order the robot to pick item
    """
    def pickItem(self):
        return ("pick item at {}" .format(self._pickuplocation)) 
    """   
    * @order the robot to drop item
    """
    def dropItem(self):
        return ('drop item at {}' .format(self._droplocation))
    """
    * @order the robot to ship product
    """
    def shipItem(self):
        return ('ship item at {}' .format(self._droplocation))
    """
    * @order the robot to drop item
    """
    def operation(self):
        if (self._operationtype == "drop"):
            self._dropItem()
        else:
            self._shipItem()

