#!bin/bash

echo "starting front end..."
# use port 8889 to upload images to frontend
python3 manage.py runserver 127.0.0.1:8889 > frontend.log &

echo "uploading images..."
python3 saraiyascope/utils/image_utils.py

