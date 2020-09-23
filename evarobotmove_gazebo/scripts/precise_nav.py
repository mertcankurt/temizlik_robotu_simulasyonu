#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from trajectory_msgs.msg import *
from visualization_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, PoseWithCovarianceStamped, Twist
from tf.transformations import euler_from_quaternion
import sensor_msgs.msg

rospy.init_node('precise_nav', anonymous=False)

robotpose = PoseWithCovarianceStamped()
theta = 0.0

goal = Point()
goal.x = 5.8
goal.y = -2.8

LINX = 0.0 #Always forward linear velocity.
PI = 3.14
angz = 0
L=0
R=0
F=0

def SonarFScan(data):
    global F
    global LINX
    global angz
    try:
        F = data.range
    except Exception as err:
        print(err)

def SonarLScan(data):
    global L
    global angz
    try:
        L = data.range
    except Exception as err:
        print(err)

def SonarRScan(data):
    global R
    global angz
    try:
        R = data.range
    except Exception as err:
        print(err)

def VelScan(data):
    global angz
    global LINX
    LINX = data.linear.x
    angz = data.angular.z

def amclPoseSub(data):
    global robotpose
    global theta
    robotpose = data
    rot_q = data.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def pubVel(lin, ang):
    command = Twist()
    command.linear.x = lin
    command.angular.z = ang
    velocity_pub.publish(command)

r = rospy.Rate(10)

def main():
    while not rospy.is_shutdown():
        global robotpose
        global goal
        global theta
        global F
        global L
        global R
        global LINX
        global angz

        dist = Point()

        dist.x = goal.x - robotpose.pose.pose.position.x
        dist.y = goal.y - robotpose.pose.pose.position.y

        distAngleZ = math.atan2(dist.y,dist.x)

        distSize = math.sqrt(math.pow(dist.x,2) + math.pow(dist.y,2)) 
        rospy.loginfo(distSize)

        if(distSize > 0.3):
            if(F<=0.6):
                slowing = True
                LINX = 0.15   
                if(L > 0.35 and R > 0.35 and distSize > 1):
                    turningLeft = True
                    angz = 0.8
                    pubVel(LINX,angz)
                elif((L<0.4 and R < 0.4 and distSize > 1) or (F < 0.25 and distSize > 1) or (L < 0.25 and distSize > 1) or (R < 0.25 and distSize > 1)):
                    LINX = LINX-0.5
                    pubVel(LINX,angz)
                else: 
                    angz = 0
                    pubVel(LINX,angz)
                    turningLeft = False
            else:
                slowing = False
            
            if((F<0.6 and L<0.4) or L < 0.3):
                turningRight = True
                angz = -0.5
            else:
                if (not slowing):
                    if (distSize > 2):
                        LINX = 0.5
                    else:
                        LINX = distSize/4
                turningRight = False

            if((F<0.6 and R<0.4) or R < 0.3):
                turningLeft = True
                angz = 0.5    
            else: 
                if (not slowing):
                    if (distSize > 2):
                        LINX = 0.5
                    else:
                        LINX = distSize/4
                turningLeft = False
        else:
            slowing = False
            turningLeft = False
            turningRight = False
            
        if(distAngleZ - theta > 0.1 and distSize > 0.2 and L > 0.3 and R > 0.3):
            if(distAngleZ - theta > 0.5):
                angz = 0.5
            else:  
                angz = 0.2
            if (distSize > 2):
                LINX = 0.5
            else:
                LINX = distSize/4
            rospy.loginfo("turning on the objective, error = "+str(distAngleZ-theta))
        elif(distAngleZ - theta < -0.1 and distSize > 0.2 and L > 0.3 and R > 0.3):
            if(distAngleZ - theta < -0.5):
                angz = -0.5
            else:  
                angz = -0.2
            if (distSize > 2):
                LINX = 0.5
            else:
                LINX = distSize/4
            rospy.loginfo("turning on the objective, error = "+str(distAngleZ-theta))
        elif(distSize > 0.1):
            if(distSize > 2):
                if(not turningLeft and not turningRight and not slowing):
                        LINX = 0.5
                        angz = 0
                        rospy.loginfo("distance > 2 "+str(distSize))     
            else:
                if(not turningLeft and not turningRight and not slowing):
                    LINX = distSize/4
                    angz = 0
                    rospy.loginfo("distance < 2 "+str(distSize))
        elif(distSize <= 0.1):
            LINX = 0
            angz = 0
            rospy.loginfo("objective reached")
            #rospy.signal_shutdown("objective reached")
            #sys.exit()
        pubVel(LINX, angz)
        r.sleep()


if __name__ == '__main__':
    try:
        velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
        amcl_pose = rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped,amclPoseSub)
        rospy.Subscriber("/cmd_vel",Twist, VelScan)
        rospy.Subscriber("/sonar1", sensor_msgs.msg.Range , SonarFScan)
        rospy.Subscriber("/sonar0", sensor_msgs.msg.Range , SonarRScan)
        rospy.Subscriber("/sonar2", sensor_msgs.msg.Range , SonarLScan)

        main()

        # Sleep to give the last log messages time to be sent
        rospy.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
