# Paramiko shoul be installed firstly
# win cmd >  pip install paramiko  
from paramiko import SSHClient, AutoAddPolicy
import time

with SSHClient() as client:
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(
        # Ip address of the inews server
        '1.1.1.1',
        port=22,
        username='type user name here',
        password='type pass here'
    )
    with client.open_sftp() as sftp:
       sftp.get('/home/so/licenses.txt', 'D:/licenses.txt')
sftp.close()


#open file
file = open(u'D:/licenses.txt', 'r')
#read file
content = file.read()

#count total lenght
print("Total chars: ", len(content))

#count number of row
print("Total lines: ", len(content)/30)

#vars for counts
counta=0
counts=0
countg=0

#var for cycle
i = 0


while i < (len(content)-29):
	
	if content[i] == 'A':
		counta += 1;
	if content[i] == 'S':
		counts += 1;
	if content[i] == 'G':
		countg += 1;
	i += 30

		
print("A in use", counta) 
print("G in use", countg)
print("S in use", counts)
#print(content)

time.sleep(60)