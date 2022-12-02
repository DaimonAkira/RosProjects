#include "ros/ros.h"
#include <stdio.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "node1");
  ros::NodeHandle n;
  ros::Rate rate(1);

  while (ros::ok())
  {
      printf("Node-1 is running. \n");
      rate.sleep();
  }
  return 0;
}