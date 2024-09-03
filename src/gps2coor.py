#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Point

def callback(data):
    base_lat = 39.89645
    base_long = 32.77730

    rospy.loginfo("Received GPS Fix:")
    rospy.loginfo("Latitude: %f", data.latitude)
    rospy.loginfo("Longitude: %f", data.longitude)
    rospy.loginfo("Altitude: %f", data.altitude)

    cur_lat = data.latitude
    cur_long = data.longitude

    coor_x = (cur_long-base_long)*111111
    coor_y = (cur_lat-base_lat)*111111

    rospy.loginfo("Received point: x=%f, y=%f", coor_x,coor_y)

    coor_point = Point()
    coor_point.x = coor_x
    coor_point.y = coor_y
    coor_point.z = 0.0

    pub.publish(coor_point)


def gps_subscriber_node():
    # Initialize the ROS node
    rospy.init_node('gps_subscriber', anonymous=True)

    # Subscribe to the "/fix" topic with NavSatFix messages
    global pub
    pub = rospy.Publisher('coordinate',Point,queue_size=10)

    rospy.Subscriber('/fix', NavSatFix, callback)

    # Keep the node running
    rospy.spin()

if __name__ == '__main__':
    try:
        gps_subscriber_node()
    except rospy.ROSInterruptException:
        pass
