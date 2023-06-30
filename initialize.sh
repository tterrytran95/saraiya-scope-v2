#!bin/bash
# initialize the bioscope # only run this once
echo "setting up virtual environment"
python3 -m venv bioscope
source bioscope/bin/activate
pip install -r requirements.txt

# use port 8889 to upload images to frontend
echo "starting front end..."
python3 manage.py runserver 127.0.0.1:8889 > logs/initialize.log &

echo "making migrations..."
python3 manage.py migrate

echo "uploading images..."
python3 saraiyascope/utils/image_utils.py -video=bioscope-bowes.mp4

echo "done! next steps..."
echo "       sh server.sh"