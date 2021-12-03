# RaspberryBinaryClock
Raspberry Pie Binary Clock School Task

A Binary clock project for sensehat for raspberry pie made in python. 

Simply download the repository to the pie. 

# Setting up as service

go to the init.d file on the raspberry pie via SSH 
- cd /etc/init.d

after that create a new python script file.
- sudo nano script.py
and copy the content of the script file into that

in the top add lines from service data to the top of the file.

After that save the context of the script by pressing ctrl+x and save the file.

run the following commands after
-sudo chmod +x script.py
-sudo update-rc.d script.py defaults

and after that reboot the pie to ensure it works
- sudo reboot
