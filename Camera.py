"""
 * @author ricardonolasco
 *
"""

class Camera:
    
    def __init__ (self, qrcodes, barcodes, jpeg, mp4):
        self._qrcodes = qrcodes # reads the QR Code of the current location for the robot
        self._barcodes = barcodes   # reads the Barcode for the item being picked
        self._jpeg = jpeg # jpeg file name for picture taken
        self._mp4 = mp4 # mp4 file name for video recorded
    """
     * @return the direction for the robot to move
    """
    def takePicture(self):
        return self._jpeg
    """
     * @return the decision made for the robot
    """
    def recordVideo(self):
        return self._mp4
    """
     * @return the decision made for the robot
    """
    def captureQRCode(self):
        return self._qrcodes
    """
     * @return the decision made for the robot
    """
    def captureBarcode(self):
        return self._barcodes