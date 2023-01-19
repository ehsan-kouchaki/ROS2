# ROS2 Velocity Control of a Walker
Implementation of ROS2 control on a walker model. The walker has a IMU sensor.

In this repositort a walker model consists of five links and four revolute joints is controled using ROS2 control (veocity control)

# Run Rviz Model

Run this command:

ros2 launch my_robot my_robot_rviz.launch.py 

The model will show up in rviz like this:

![rviz_screenshot_2022_08_06-18_14_20](https://user-images.githubusercontent.com/79801992/183251567-d76443b3-15b0-49db-b8a0-ea277e43843e.png)

# Run the model in gazebo withou controller

Run this command:

ros2 launch my_robot my_robot_nocontrol.launch.py

you can see that the walker fall down:
![gazebo](https://user-images.githubusercontent.com/79801992/183251739-bd5e01c4-498b-4f51-8b49-d84878002130.png)

# Run the model in gazebo with velocity controller

ros2 launch my_robot my_robot_velocity.launch.py

The robot will show up in gazebo and maintain its balance
