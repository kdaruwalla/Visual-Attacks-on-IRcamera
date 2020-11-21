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


#funciton used to  write frames to file
def write_bytesio_to_file(filename, bytesio):
    with open(filename, "wb") as outfile:
        outfile.write(bytesio.getbuffer())
    return cv.imread(filename)


def correlate(image, i):
    newIm = image

    if i is 0:
        print('0')
        return 0
    if i is 1:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame1.jpg')
    if i is 2:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame2.jpg')
    if i is 3:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame3.jpg')
    if i is 4:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame4.jpg')
    if i is 5:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg')
    if i is 6:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame6.jpg')
    if i is 7:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame7.jpg')
    if i is 8:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame8.jpg')
    if i is 9:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame9.jpg')
    if i is 10:
        oldIm = cv.imread('/Users/jakecolapietro/Desktop/CapturedFrames/frame10.jpg')

    ifc = ssim.structural_similarity(oldIm, newIm, multichannel=True)
    #ifc = np.average(c)

    print(ifc)

    return ifc


# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
counter = 0 # initilizing counter to keep track of the file to put the stream capture in
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
        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
        # Trying some shit out below

        #Cases for writing the stream into specific files
        if counter == 0:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame1.jpg", image_stream)
        if counter == 1:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame2.jpg", image_stream)
        if counter == 2:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame3.jpg", image_stream)
        if counter == 3:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame4.jpg", image_stream)
        if counter == 4:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg", image_stream)
        if counter == 5:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame6.jpg", image_stream)
        if counter == 6:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame7.jpg", image_stream)
        if counter == 7:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame8.jpg", image_stream)
        if counter == 8:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame9.jpg", image_stream)
        if counter == 9:
            img = write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame10.jpg", image_stream)


        corr = correlate(img, i)
        counter = counter + 1
        i = i + 1

finally:
    connection.close()
    server_socket.close()

