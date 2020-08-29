#!/bin/bash
#v4l2-ctl --set-ctrl=exposure_auto=0
#v4l2-ctl --set-ctrl=exposure_absolute=333
#v4l2-ctl --set-ctrl=focus_auto=0
#v4l2-ctl --set-ctrl=white_balance_temperature_auto=0
for i in {0..250..50}
do
	#streamer -f jpeg -o image.jpeg
	#fswebcam -r 1920x1080 --jpeg 85 web-cam-shot.jpg
	sleep .5
	v4l2-ctl --device=/dev/video0 --set-ctrl=focus_absolute=${i}
	A="figures/closest${i}.jpg"
	#ffmpeg -f v4l2 -i /dev/video0 -vframes 1 $A
	#python laplacian.py figures/pen_0.jpg
	#ffmpeg -f v4l2 -i /dev/video0 -vframes 1
done
