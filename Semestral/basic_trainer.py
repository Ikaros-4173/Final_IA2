#!/usr/bin/env python  
import roslib
#import message_filters
roslib.load_manifest('sufrimiento_semestral')
import rospy
import math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import PointCloud
import time
import sys,tty,termios
import csv

global rightDistance 
global leftDistance 
global floorDistance


def cmd_velReceived(message):
    infile = open("left.txt","r")
    leftDistance = infile.read()
    infile.close()
    infile = open("right.txt","r")
    rightDistance = infile.read()
    infile.close()
    infile = open("floor.txt","r")
    floorDistance = infile.read()
    infile.close()
    with open('training.csv', 'a') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([rightDistance, leftDistance,  floorDistance, str(message.linear.x), str(message.angular.z)])
	
def leftSensorCallback(data):
     output = open("left.txt","w")
     leftDistance = data.points[0].x
     output.write(" "+str(leftDistance))
     output.close()
     rospy.loginfo("SENSOR IZQUIERDO x %f", data.points[0].x)
   

def rightSensorCallback(data):
     output = open("right.txt","w")
     rightDistance = data.points[0].x
     output.write(" "+str(rightDistance))
     output.close()
     rospy.loginfo("SENSOR DERECHO x %f", data.points[0].x)

def floorSensorCallback(data):
     output = open("floor.txt","w")
     floorDistance = data.points[0].x
     output.write(" "+str(floorDistance))
     output.close()
     rospy.loginfo("SENSOR FLOOR x %f", data.points[0].x)



rospy.init_node('sufrimiento_semestral', log_level=rospy.DEBUG)
rospy.loginfo("Me subscribire al canal cmd_vel")
#rospy.Timer(rospy.Duration(5), calling)
#rospy.Subscriber('/distance_sensors_state/front_left_srf10', PointCloud,rospy.Timer(rospy.Duration(5), calling))
rospy.Subscriber('/cmd_vel', Twist, cmd_velReceived)
rospy.Subscriber('/distance_sensors_state/front_left_srf10', PointCloud, leftSensorCallback)
rospy.Subscriber('/distance_sensors_state/front_right_srf10', PointCloud, rightSensorCallback)
rospy.Subscriber('/distance_sensors_state/floor_sensor', PointCloud, floorSensorCallback)
rightDistance=0.0
leftDistance=0.0
floorDistance=0.0
rospy.spin()

	
