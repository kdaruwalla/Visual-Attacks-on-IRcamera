from PIL import Image
import cv2 as cv


# function that copies one of the stream captures and pastes it over the other
def imageCopy(img, img2):
    # img = Image.open(r'C:\Users\Kivan\OneDrive\Pictures\Camera Roll\image2.jpg', 'r') #represents the image to be pasted
    # img2 = Image.open(r'C:\Users\Kivan\OneDrive\Pictures\Camera Roll\image1.jpg', 'r')#represnets the image to get pasted over
    img_w, img_h = img.size
    # background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
    background = Image.new('RGBA', (2560, 1600), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    img2.paste(img, offset)
    img2.save(r"/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg")
    return cv.imread("/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg")

def frameCopy(img, img2):
    # img = Image.open(r'C:\Users\Kivan\OneDrive\Pictures\Camera Roll\image2.jpg', 'r') #represents the image to be pasted
    # img2 = Image.open(r'C:\Users\Kivan\OneDrive\Pictures\Camera Roll\image1.jpg', 'r')#represnets the image to get pasted over
    img_w, img_h = img.size
    # background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
    background = Image.new('RGBA', (2560, 1600), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    img2.paste(img, offset)
    img.save(r"/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg")
    return cv.imread("/Users/jakecolapietro/Desktop/CapturedFrames/frame5.jpg")
