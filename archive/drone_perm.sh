#!/usr/bin/bash

# Makes it possible to use the USB Radio and Crazyflie 2 over USB without being root.
sudo groupadd plugdev
sudo usermod -a -G plugdev $USER

# Creates the file /etc/udev/rules.d/99-bitcraze.rules
cat <<EOF | sudo tee /etc/udev/rules.d/99-bitcraze.rules > /dev/null
# Crazyradio (normal operation)
SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE="0664", GROUP="plugdev"
# Bootloader
SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="0101", MODE="0664", GROUP="plugdev"
# Crazyflie (over USB)
SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE="0664", GROUP="plugdev"
EOF

# Reloads the udev-rules
sudo udevadm control --reload-rules
sudo udevadm trigger