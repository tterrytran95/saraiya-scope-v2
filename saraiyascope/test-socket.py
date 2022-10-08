import time, sys, socket, json
HOST = sys.argv[1].split("=")[1]
PORT = 1234

## Step 1: Make socket connection to server ## 
ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))
    exit(1)
Response = ClientSocket.recv(1024)

### Step 2: Send a response going forward & backward
for i in range(100):    
    Input = 'forward' + ',' + 'frame'+str(i*10)+'.jpg'
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    time.sleep(.5)     

for i in range(10, -1, 1):    
    Input = 'backward' + ',' + 'frame'+str(i*10)+'.jpg'
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    time.sleep(.5)
### Step 3: Close the connection
ClientSocket.close()