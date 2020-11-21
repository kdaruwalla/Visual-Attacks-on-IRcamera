
def correlate(image_stream, i):
    newIm = image_stream
    row = 480
    col = 640
    denom1 = 0
    denom2 = 0
    num1 = 0
    num2 = 0

    if i is 1:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame1'
    if i is 2:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame2'
    if i is 3:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame3'
    if i is 4:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame4'
    if i is 5:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame5'
    if i is 6:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame6'
    if i is 7:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame7'
    if i is 8:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame8'
    if i is 9:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame9'
    if i is 10:
        oldIm = 'Users/jakecolapietro/Desktop/CapturedFrames/frame10'


    sumOld = sum(oldIm)
    sumNew = sum(newIm)

    for j in range(row):
        for k in range(col):
            denom1 = denom1 + (oldIm(j, k) - sumOld)^2
            denom2 = denom2 + (newIm(j, k) - sumNew)^2

            num1 = oldIm(j, k) - sumOld
            num2 = newIm(j, k) - sumNew

    denom = denom1*denom2
    num = num1*num2
    D = float(math.sqrt(denom))
    ifc = num/D
    
    print(ifc)
    
    return ifc
