# RaspberryBinaryClock Description
Raspberry Pie Binary Clock School Task

A Binary clock project for sensehat for raspberry pie made in python. 


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
* sudo nano hello.service

To set up the service first run following command to path to the system folder
* cd /lib/systemd/system/

after that create the service by typing the following command
* sudo nano clock_script.service

After that copy the context of Service Setup into clock_script.service.

After that type the following commands in the bash terminal
* sudo chmod 644 /lib/systemd/system/clock_script.service
* chmod +x /home/pi/script.py
* sudo systemctl daemon-reload
* sudo systemctl enable clock_script.service
* sudo systemctl start clock_script.service

# Closing and starting service

To check the status of the service
* sudo systemctl status clock_script.service

To start the service
* sudo systemctl start clock_script.service

To stop the service
* sudo systemctl stop clock_script.service

