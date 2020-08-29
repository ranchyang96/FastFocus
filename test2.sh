#!/bin/bash
for i in {0..250..25}
do
	#streamer -f jpeg -o image.jpeg
	#v4l2-ctl --set-ctrl=focus_absolute=${i}
	#A="${i}out.jpg"
	#echo "start taking photo with focus ${i}"
	date +%H:%M:%S:%N
	ffmpeg -f v4l2 -i /dev/video0 -vframes 1 > tmp 2>&1
	#echo "end taking photo with focus ${i}"
	#date +%H:%M:%S:%N
	#fswebcam -r 1920x1080 --jpeg 85 web-cam-shot.jpg
	date +%H:%M:%S:%N
	A="figures/${i}out.jpg"
	python laplacian.py $A
	date +%H:%M:%S:%N
	#echo "end of photo with focus ${i}"
done
