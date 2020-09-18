#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Pose, Point, Quaternion, PoseWithCovarianceStamped, Twist
from math import atan2

x = 0.0
y = 0.0 
theta = 0.0

def newPose(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    

rospy.init_node("speed_controller")

sub = rospy.Subscriber("amcl_pose",PoseWithCovarianceStamped, newPose)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

speed = Twist()

r = rospy.Rate(10)

goal = Point()
goal.x = 6
goal.y = -3

while not rospy.is_shutdown():
    inc_x = goal.x -x
    inc_y = goal.y -y

    angle_to_goal = atan2(inc_y, inc_x)

    if abs(angle_to_goal - theta) > 0.1:
        rospy.loginfo("angle to goal = "+str(angle_to_goal)+"theta = "+str(theta))
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0

    pub.publish(speed)
    r.sleep()    

