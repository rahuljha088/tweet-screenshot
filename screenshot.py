import pyscreenshot as ImageGrab

import datetime

if __name__ == '__main__':

    # grab fullscreen
    im = ImageGrab.grab()

    ts = datetime.datetime.utcnow()

    filename = "images/screenshot.png"

    # save image file
    im.save(filename)

    # show image in a window
    im.show()
