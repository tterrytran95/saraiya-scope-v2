#!bin/bash
# initialize the bioscope # only run this once

# use port 8889 to upload images to frontend
echo "starting front end..."
python3 manage.py runserver 127.0.0.1:8889 > frontend.log &

echo "making migrations..."
python3 manage.py migrate

echo "uploading images..."
python3 saraiyascope/utils/image_utils.py -video=bioscope-bowes.mp4