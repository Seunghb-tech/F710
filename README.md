## This package is to change the F710's axes[3] & axes[2] signals into linear.x & angular.z ones of cmd_vel topic.  
### Usage

$ cd turtlebot3_ws/src

$ git clone https://github.com/Seunghb-tech/F710/my_joystic_pkg

$ cd ..

$ colcon build --packages-select my_joystic_pkg

$ source install/local_setup.bash

$ ros2 run joy joy_node

$ ros2 run my_joystic_pkg joy_to_cmd_vel_node [--ros-args -p linear_factor:=0.5 -p angular_factor:=0.5]

or

ros2 run my_joystic_pkg joy_to_cmd_vel_stamped_node [--ros-args -p linear_factor:=0.5 -p angular_factor:=0.5]

$ ros2 launch my_joystic_pkg joystic_control.launch.py

