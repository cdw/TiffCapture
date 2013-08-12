tiff-capture
============

Provides a PIL based capture interface to multi-part tiffs, allowing them to be used more easily with OpenCV. 

Example usage:
    import tiffcapture as tc
    import cv2
    tiff = tc.opentiff(filename) #open img
    _, first_img = tiff.retrieve() 
    cv2.namedWindow('video')
    for f,img in tiff:
        tempimg = cv2.absdiff(first_img, img) # bkgnd sub
        _, tempimg = cv2.threshold(tempimg, 5, 255, 
            cv2.cv.CV_THRESH_BINARY) # convert to binary
        cv2.imshow('video', tempimg)
        cv2.waitKey(80)
    cv2.destroyWindow('video')


