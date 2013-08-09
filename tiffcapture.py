#!/usr/bin/env python
# encoding: utf-8
"""
TiffCapture.py - a capture class 

This guy provides a capture interface to multi-part-tiffs for 
use with OpenCV. It uses PIL to open the images and then reads
them frame-by-frame as needed, avoiding memory borking.

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

Created by Dave Williams on 2013-07-15
"""

try:
    import Image
    import numpy as np
except ImportError, e:
    raise Exception("You'll need both numpy and PIL installed (and to be able to import 'Image') for TiffCapture to work")


def opentiff(filename):
    """Open a tiff with TiffCapture and return the capture object"""
    return TiffCapture(filename)

class TiffCapture(object):
    """Feed me a filename, I'll give you a tiff's capture object"""
    def __init__(self, filename):
        """Initialize and return the capture object"""
        self.filename = filename
        self.tiff = Image.open(filename)
        self.length = self._count_frames()
        self.shape = self.tiff.size
        self._curr = 0
    
    def __iter__(self):
        return self
    
    def next(self):
        f, img = self.read()
        if f is True:
            return img
        else:
            raise StopIteration()
    
    def _count_frames(self):
        """Return the number of frames in the tiff, takes a bit"""
        try:
            self.tiff.seek(10**1000) #gonna assume that's long enough
        except EOFError:
            length = self.tiff.tell()
            self.tiff.seek(0)
            return length
    
    def grab(self):
        """Move to the next stack image, return True for success"""
        try:
            self.tiff.seek(self._curr+1)
            self._curr += 1
            return True
        except EOFError:
            return False
    
    def retrieve(self):
        """Decode and return the grabbed video frame"""
        return True, np.array(self.tiff) 
    
    def read(self):
        """Grab, decode, and return the next video frame"""
        grabbed = self.grab()
        if grabbed is True:
            return True, self.retrieve()
        else:
            return False, np.array([])
    
    def find_and_read(self, i):
        """Find and return a specific frame number, i"""
        self.tiff.seek(i)
        try:
            img = np.array(self.tiff)
            self.tiff.seek(self._curr)
        except EOFError:
            img = np.array([])
        return img

