# -*- coding: utf-8 -*-  
#############################################################
#
#               Python OSX MouseClick
#
#       (c) 2010 Alex Assouline, GeekOrgy.com
#               modified by Greg Bigwood
#
#############################################################
import sys
try:
    xclick=int(sys.argv[1])
    yclick=int(sys.argv[2])
    try:#
        delay=int(sys.argv[3])
    except:
        delay=0
    numclicks=int(sys.argv[4])
except:
    print "USAGE mouseclick [int x] [int y] [delay in seconds] [number of clicks]"
    exit()

print "mouse click at ", xclick, ",", yclick," in ", delay, "seconds", "numberof clicks",numclicks
#you only want to import the following after passing the parameters check above, because ‘importing’ takes time, about 1.5s
#(why so long!, these libs must be huge : anyone have a fix for this ?? please let me know.)


import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
    #mouseEvent(kCGEventMouseMoved, posx,posy); #uncomment this line if you want to force the mouse to MOVE to the click location first (i found it was not necesary).
    mouseEvent(kCGEventLeftMouseDown, posx,posy);
    mouseEvent(kCGEventLeftMouseUp, posx,posy);

time.sleep(delay);
for i in xrange(numclicks):
    mouseclick(xclick, yclick);


print "done."

