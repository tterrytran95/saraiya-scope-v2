#!bin/bash

# check if anything is running on port 1234 and kill it
kill $(lsof -t -i:1234)

# run connector server
echo starting connector... # runs on port 1234 to talk with rasperry pi
python3 saraiyascope/server.py &


# run frontend server
echo starting frontend...
python3 manage.py runserver