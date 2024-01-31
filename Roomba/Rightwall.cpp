#include "ros/ros.h"
#include "std_msgs/String.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"

using namespace std;

ros::Publisher pub; 
ros::Subscriber sub; 
geometry_msgs::Twist msg;

void moveForward()
{
  cout << "Forward" << endl;
  msg.linear.x = 0.2;
  msg.angular.z = 0;
  pub.publish(msg);
  usleep(10);
}

void moveLeft(){
  cout << "Left" << endl;
  msg.linear.x = 0.2;
  msg.angular.z = 0.5;
  pub.publish(msg);
  usleep(10);
}

void moveRight(){
  cout << "Right" << endl;
  msg.linear.x = 0.2;
  msg.angular.z = -0.5;
  pub.publish(msg);
  usleep(10);
}

void Scan_data(const sensor_msgs::LaserScan::ConstPtr& scan)
{
  // If an object is farther than 1m on the right side
  if(scan->ranges[630] < 8 && scan->ranges[540] > 8){ 
    moveForward();
  }
  // If an object is closer than 1m on the right side
  else if (scan->ranges[630] > 8 && scan->ranges[540] < 8){
    moveRight();
  }
  //
  else if (scan->ranges[630] < 1 && scan->ranges[540] > 12){
    moveLeft();   
  }
  else if (scan->ranges[630] < 1 && scan->ranges[540] > 0.7){
    moveLeft();   
  }
  else{
    if (scan->ranges[540] > 0.7){
      moveRight();
    }
    else if(scan->ranges[540] < 0.7){
      moveLeft();
    }
    else{
      moveForward();
    }
    }

size_t range_size = scan->ranges.size(); 
cout<<scan->ranges[540] << endl; 
cout<<scan->ranges[630] << endl; 


}
int main(int argc, char **argv)
{

  ros::init(argc, argv, "scan_listen");
  ros::NodeHandle n;
  sub = n.subscribe<sensor_msgs::LaserScan>("/scan", 100, Scan_data);
  pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
  ros::spin();

  return 0;
}

