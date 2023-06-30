#!bin/bash

# automate ssh into raspberry pi
# https://medium.com/@eanunez85/automate-your-ssh-login-to-remote-servers-28dbdc0ed28f

source "bioscope/bin/activate"

# check if anything is running on port 1234 and kill it
kill $(lsof -t -i:1234) # connector port
kill $(lsof -t -i:8000) # frontend port 

# run connector server
echo starting connector...

# silently run on the WSL VM host # port 1234 exposed 
python3 saraiyascope/server.py -HOSTNAME=$(hostname -I) > logs/connector.log & 


# run frontend server
echo starting frontend...
python3 manage.py runserver > logs/frontend.log &