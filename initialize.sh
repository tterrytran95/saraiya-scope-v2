#!bin/bash

# set up virtual environment 
# install python3.9 
# create virtual environment 
# get into the virtual environment 

echo "starting front end..."
# use port 8889 to upload images to frontend
python3 manage.py runserver 127.0.0.1:8889 > frontend.log &

echo "uploading images for film1..."
python3 saraiyascope/utils/image_utils.py video=film1.mp4

echo "uploading images for film1..."
python3 saraiyascope/utils/image_utils.py video=film2.mp4

echo "making migrations..."
python3 manage.py migrate

# echo "starting up runserver..."
# python3 manage.py runserver 