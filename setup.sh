sudo mv RaspberryBinaryClock/clock.py /home/
sudo mv RaspberryBinaryClock/clock.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/clock.service
chmod +x /home/clock.py
sudo systemctl daemon-reload
sudo systemctl enable clock.service
sudo systemctl start clock.service
