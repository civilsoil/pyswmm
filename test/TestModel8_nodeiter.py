'''
TestModel1_Current Time

Author: Bryant E. McDonnell (EmNet LLC)
Date: 11/12/2016


'''
import time
import os
import sys

#point to location of the pyswmm file
sys.path.append(os.getcwd()+'\\..\\pyswmm\\')

from swmm5 import pyswmm, Nodes, Node, Links, Link


swmmobject = pyswmm('./TestModel1_weirSetting.inp')
swmmobject.swmm_open()

for node in Nodes(swmmobject):
    print node
    print node.nodeid
    print node.invertel
    node.set_invertel(10)
    print node.invertel

node = Node(swmmobject, "J1")
print node.invertel

for link in Links(swmmobject):
    print link
    print link.linkid
    print link.qLimit
    link.set_qLimit(10)
    print link.qLimit

link = Link(swmmobject, "C2")
print link.qLimit

swmmobject.swmmExec()

swmmobject.swmm_close()

 
print("swmm_step() Check Passed")
