import io
import socket
import struct
from PIL import Image
import shutil
import math
import numpy as np
import cv2 as cv
from scipy import stats
from skimage.metrics import _structural_similarity as ssim
from ImageCopyPaste import frameCopy


#funciton used to  write frames to file
def write_bytesio_to_file(filename, bytesio):
    with open(filename, "wb") as outfile:
        outfile.write(bytesio.getbuffer())
    return cv.imread(filename)


def correlate(image, i):
    newIm = image

    if i is 0:
        print('First Frame')
        return 1
    else:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame' + str(i) + '.jpg')

    ifc = ssim.structural_similarity(oldIm, newIm, multichannel=True)

    print("The structural similarity between frames " + str(i) + " AND " + str(i+1) + " = " + str(ifc))
    return ifc


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
counter = 0  # initializing counter to keep track of the file to put the stream capture in
i = 0

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
try:
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)
        #print('Image is %dx%d' % image.size)
        image.verify()
        #print('Image is verified')
        # Trying some shit out below

        #Cases for writing the stream into specific files
        img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame" + str(counter + 1) + ".jpg",
                                    image_stream)

        # attack injection
        if counter == 4:
            img1 = Image.open(r"/Users/jakecolapietro/Desktop/CapturedFrames/frame1.jpg", 'r')  # represents the image to be pasted
            img2 = Image.open(r"/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg", 'r')  # represnets the image to get pasted over
            img = frameCopy(img1, img2)  # function to copy and paste attack

        counter = counter + 1
        corr = correlate(img, i)
        # check to see if the returned correlation value is not within threshold, if not send warning message to user
        if corr <= .2:
            print("-------------------------------------------------(Threat detected between frames: " + str(i) + " and " + str(i+1) + ")-------------------------------------------------")
        i = i + 1


finally:
    connection.close()
    server_socket.close()



