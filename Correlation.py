def correlate(image_stream, i):
    newIm = image_stream
    row = 480
    col = 640
    denom1 = 0
    denom2 = 0
    num1 = 0
    num2 = 0

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

    old = oldIm.astype(float)
    new = newIm.astype(float)


    sumOld = np.sum(old)
    sumNew = np.sum(new)

    for j in range(row):
        for k in range(col):
            denom1 = denom1 + (oldIm[j][k] - sumOld) ** 2
            denom2 = denom2 + (newIm[j][k] - sumNew) ** 2

            num1 = oldIm[j][k] - sumOld
            num2 = newIm[j][k] - sumNew

    denom = denom1 * denom2
    num = num1 * num2
    D = np.sqrt(denom)

    A = num / D
    ifc = np.average(A)

    print(ifc)

    return ifc
