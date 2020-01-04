'''
Simple Port Scanner v1.0
Pyton 3.x

Phillip Kittelson
@gaterunner341
Created for educational and training purposes only
'''

import socket
import sys
from datetime import datetime

print('Simple Port Scanner v1.0')
print('-' * 50)

# Ask for a host name or IP address to scan
remoteServer = input('Enter a remote host to scan: ')

# Input and validation for starting and ending port numbers
while True:
    try:
        startPort = int(input('Sarting port? : '))
        break
    except ValueError:
        print('ERROR: Please enter a whole number')
while True:
    try:
        endPort = int(input('Ending port? : '))
        endPort = endPort + 1
        break
    except ValueError:
        print('ERROR: Please enter a whole number')

remoteServerIP = socket.gethostbyname(remoteServer)

# Letting the user know the scan in inprogress and starting date and time
print('-' * 50)
print('Please wait, scanning remote host ' + remoteServerIP)
t1 = datetime.now()
print('Scan started on ' + str(t1))
print('Press CTRL + C to quit')
print('-' * 50)

# Iterate through port numbers with connections and print if port open
try:
    for port in range(startPort,endPort):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0: # Closed port reports number other than 0
            print('Port {}:\t\tOPEN'.format(port))
        sock.close() # Close each connection before starting new connection
except KeyboardInterrupt: # Allow a user to interrupt process
    input('Scan did not complete due to user intervention.  Press ENTER to close window.')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
except socket.error:
    print('Could not connect to server')

# Check time again, calculate differance and allow user to see duration of scan
t2 = datetime.now()
total =  t2 - t1
print('\nScanning completed in: ' + str(total))

# Needs user input to close terminal window
input('\nComplete, press ENTER key to exit')