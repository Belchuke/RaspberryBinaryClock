# RaspberryBinaryClock Description
Raspberry Pie Binary Clock School Task

A Binary clock project for sensehat for raspberry pie made in python. 
Simply download the repository to the pie. 

# Joystick actions
Pressing the joystick on the sence hat brings two options
- Pushing up or down will change the clock to switch between vertical or horizontal display of the clock
- Pushing Left or right wil change the clock between 12 hour showing and 24 hour showing.


# Setting up as service
* sudo nano hello.service

To set up the service first run following command to path to the system folder
* cd /lib/systemd/system/

after that create the service by typing the following command
* sudo nano clock_script.service

# Closing and starting service

To check the status of the service
* sudo systemctl status clock_script.service

To start the service
* sudo systemctl start clock_script.service

To stop the service
* sudo systemctl stop clock_script.service

