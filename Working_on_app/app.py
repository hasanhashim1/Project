 

from getpass import getpass
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import paramiko
import paramiko, os, re
from datetime import datetime

root = Tk()
root.geometry("400x400")
hh = Label(root, text="Enter the host or IP for ssh:")
hh.pack()
hh = Entry(root, width=50)
hh.pack()

po = Label(root, text="Enter the port for ssh:")
po.pack()
po = Entry(root, width=50)
po.pack()

un = Label(root, text="Enter the username for ssh:")
un.pack()
un = Entry(root, width=50)
un.pack()

pp = Label(root, text="Enter the Password for ssh:")
pp.pack()
pp = Entry(root, width=50, show = '*')
pp.pack()

def write(output):
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"),("Python File", ".py")])
    file.write(output)
def main():
    ppp=pp.get()
    h=hh.get()
    p=po.get()
    u=un.get()
    #Create the password prompt
    #thePass = getpass(prompt="Please enter your SSH password: ")
 
    # Host information
    # host = h
    # port = p
    # username = u
    # password = ppp


    host = "192.168.74.130"
    port = 22
    username = "kali"
    password = "kali"
    try:



        # def write(s, output):
        #     # Here we trying to name the file and let the user write the first half of the name.
        #     with open(f"{s}_output.txt", "a") as f:
        #         f.write(f"\n### {s} output - ")
        #         f.write(output)


        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        ssh.connect(host, port, username, password)

        def ssh_connection():
                top = Toplevel()
                top.title('Coomand Execution') 
                top.geometry("400x400")     
                cmd = Entry(top, width=50)
                cmd.pack()
                def send_cmd():
                    hello = cmd.get()
                    command = [hello]

                    for eachCMD in command:
                        # Get the output from the command
                        stdin, stdout, stderr = ssh.exec_command(eachCMD)

                        # Get results from stdout
                        lines = stdout.readlines()
                        #print(lines)

                        # Convert the lsiti to a string
                        output = ''.join(lines)

                        # Header
                        sepHeader = '' + '### BEGIN ' + eachCMD + ' ###\n\n'

                        # Footer
                        sepFooter = '' + '### END ' + eachCMD + ' ###\n\n'

                        # Concatenate the header, output, and footer
                        cmd_output = sepHeader + output + sepFooter

                        # Save the cmd_output to a file
                        # with open(file, 'a') as f:
                        #     f.write(cmd_output)
                        #print(cmd_output)
                        def save():
                            write(cmd_output)
            
                        btn = Button(top, text = 'Save', command = lambda : save())
                        btn.pack(side = TOP, pady = 20)

                myButton = Button(top, text="Enter a command", command=send_cmd)
                myButton.pack()
                def ssh_close():
                     ssh.close()
                ssh_close=Button(top, text="close ssh conncetino", command= ssh_close).pack()

 
        
      
            # ssh.close()
        

        # create a toplevel menu  
        #menubar.add_command(label="Hello!", command=send_cmd)  
        


        # display the menu          
        
    
        pp1 = Label(root, text="Choose what you want to do: ")
        pp1.pack()

            # pp1 = Entry(root, width=50)
            # pp1.pack()
            
            
        
        # create a toplevel menu  
        menubar = Menu(root)  
        #menubar.add_command(label="Hello!", command=send_cmd)  
        menubar.add_command(label="Quit!", command=root.quit)  
        # display the menu  
        root.config(menu=menubar) 
    
    except paramiko.AuthenticationException:
        #print("Authentication Failed.")
        myLabel = Label(root, text="Authentication Failed.")
        myLabel.pack()
    ssh_connect = Button(root, text="Command Execution", command=ssh_connection)
    ssh_connect.pack()
    
Button(root, text="Submit", command=main,).pack()


root.mainloop()