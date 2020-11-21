import io
import socket
import struct
from PIL import Image
import shutil

#funciton used to  write frames to file
def write_bytesio_to_file(filename, bytesio):
    with open(filename, "wb") as outfile:
        outfile.write(bytesio.getbuffer())

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)
counter = 0 # initilizing counter to keep track of the file to put the stream capture in

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
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame1.jpeg", image_stream)
        if counter == 1:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame2.jpeg", image_stream)
        if counter == 2:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame3.jpeg", image_stream)
        if counter == 3:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame4.jpeg", image_stream)
        if counter == 4:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpeg", image_stream)
        if counter == 5:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame6.jpeg", image_stream)
        if counter == 6:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame7.jpeg", image_stream)
        if counter == 7:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame8.jpeg", image_stream)
        if counter == 8:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame9.jpeg", image_stream)
        if counter == 9:
            write_bytesio_to_file("/Users/jakecolapietro/Desktop/CapturedFrames/frame10.jpeg", image_stream)
        counter = counter + 1


finally:
    connection.close()
    server_socket.close()

