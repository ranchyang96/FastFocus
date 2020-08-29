This repository includes all the scripts and documentations for FastFocus, which improves the speed of focus when capturing photos.

The folder draft includes the LaTex scripts for the documentation file.
Use "make" to get the result paper.pdf file in draft folder to compile the document.
Use "make clean" before recompile.

init.sh is used to initialize the camera to enable our evaluation scripts.
It includes some settings about exposure time, white balance and focus.

capture.py is the script used to collect photos at different focus positions.
Usage: python capture.py [GroupName]
We took five groups of photos, named ([GroupName]) human(1m), notebook(10cm), notemid(20cm), notefar(40cm), noteclose(5cm) respectively and the object distances are shown in brackets.
All the figures are in the folder "figures", and the photos are named [GroupName][FocusPosition].jpg.
For example, notebook215.jpg.

calculateall.py is used to calculate focus function for all photos in a group.
Usage: python calculateall.py [GroupName]
The results are saved in val\_[GroupName].txt and there is a figure for each group showing the relation between focus position and focus function value named [GroupName]plot.png.

hillclimb.py is the script used to collect timestamps and calculate the focus functions for one group of photos.
Usage: python hillclimb.py [GroupName]



collect.sh, test.sh, test2.sh includes some old backup methods for getting pictures with command-line tools.

photo.py, photo2.py, photo3.py includes some old backup python scripts for getting photos.

tmp is a temporary intermediate result and can be ignored.

Laplacian.cpp is the C-based method of Laplacian focus function calculation.

laplacian.py is the Python-based Laplacian focus function calculation.
