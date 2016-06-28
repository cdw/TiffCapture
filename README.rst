===========
tiffcapture
===========

Provides a PIL based capture interface to multi-part tiffs, allowing them to be used more easily with OpenCV. This allows you to use OpenCV's image and video processing capabilities with tiff stacks, a video form frequently encountered in scientific video as it is lossless and supports custom metadata. 

Examples
========

A minimal example looks like this::

    import tiffcapture as tc
    import matplotlib.pyplot as plt
    tiff = tc.opentiff(filename)
    plt.imshow(tiff.read()[1])
    plt.show()
    tiff.release()
    

More real world usage looks like this::

    import tiffcapture as tc
    import cv2
    tiff = tc.opentiff(filename) #open img
    _, first_img = tiff.retrieve() 
    cv2.namedWindow('video')
    for img in tiff:
        tempimg = cv2.absdiff(first_img, img) # bkgnd sub
        _, tempimg = cv2.threshold(tempimg, 5, 255, 
            cv2.THRESH_BINARY) # convert to binary
        cv2.imshow('video', tempimg)
        cv2.waitKey(80)
    cv2.destroyWindow('video')
    

