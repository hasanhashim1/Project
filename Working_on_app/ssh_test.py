# import paramiko

# host = "192.168.229.134"
# port = 22
# username = "kali"
# password = "kali"

# try:
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
#     ssh.connect(host, port, username, password)

#     while True:
#         cmd = input("S> ")
#         if cmd == "exit": break
#         stdin, stdout, stderr = ssh.exec_command(cmd)
#         print(stdout.read().decode())
        
# except Exception as err:
#     print(str(err))
import os
try:
    os.system('cmd /k "cmd.exe"')
except:
    print("try")