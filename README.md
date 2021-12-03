# RaspberryBinaryClock Description
Raspberry Pie Binary Clock School Task

A Binary clock project for sensehat for raspberry pie made in python. 

You can use the joysticks for various actions descripted in the joystick Actions descriptions

# Joystick actions
Pressing the joystick on the sence hat brings two options
- Pushing up or down will change the clock to switch between vertical or horizontal display of the clock
- Pushing Left or right wil change the clock between 12 hour showing and 24 hour showing.

# Downloading the content
start by downloading git
* sudo apt-get install git

after download the repository
* git clone https://github.com/Belchuke/RaspberryBinaryClock.git

# Setting up as service
For setting up as service run following command
* sudo sh RaspberryBinaryClock/setup.sh

# Closing and starting service

To check the status of the service
* sudo systemctl status clock.service

To start the service
* sudo systemctl start clock.service

To stop the service
* sudo systemctl stop clock.service

