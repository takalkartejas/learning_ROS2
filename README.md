# learning_ROS2
This repository will explain basics of ROS2 

### Steps taken
1. Installed ros2 foxy by follwing the steps for debian
2. sourced the foxy setup.bash in bashrc
3. created alias for noetic and foxy source commands to choose between them when using terminal
4. installed python colcon extention using - 'sudo apt install python3-colcon-common-extensions'
5. colcon bash file inside -'cd /usr/share/colcon_argcomplete/hook/'
6. sourced the bash file in bashrc
7. created a working directory - ros2_ws and created src folder inside it
8. colcon build inside the ros2_ws directory
9. checked the ros2 working using ros2 run demo_nodes_cpp lister and talker
10. they share info through the topic chatter


### Usefull commands
1. ros2 run - run nodes
2. alias <variable_name> = " <command1>;<command2>" -  create easy access alias for multiple big commands, can add in bashrc
3. ros2 - for ros2 help
 
