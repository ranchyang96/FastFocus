#!/bin/bash

# To understand the value range and tunable controls, use 
# v4l2-ctl --list-device
# v4l2-ctl --device=/dev/video0 --list-ctrls

# Value 1 disable auto exposure adjustment, 3 is enabled
v4l2-ctl --device=/dev/video0 --set-ctrl=exposure_auto=1
# if auto value set to 1, set the absolute value
v4l2-ctl --device=/dev/video0 --set-ctrl=exposure_absolute=333

# White balance temperature related settings
#v4l2-ctl --device=/dev/video0 --set-ctrl=white_balance_temperature_auto=0
#v4l2-ctl --device=/dev/video0 --set-ctrl=white_balance_temperature=4000

# Disable auto focus
v4l2-ctl --device=/dev/video0 --set-ctrl=focus_auto=0

# Adjust the brightness value
v4l2-ctl --device=/dev/video0 --set-ctrl=brightness=128

# Manually set the absolute focus position
v4l2-ctl --device=/dev/video0 --set-ctrl=focus_absolute=250
