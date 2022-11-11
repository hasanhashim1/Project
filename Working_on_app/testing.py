 

from getpass import getpass
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import paramiko
import paramiko, os, re
from datetime import datetime


root=Tk()



def write(output):
            file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"),("Python File", ".py")])
            file.write(output)
def ssh_connection():
        top = Tk() 
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

myButton = Button(root, text="Enter a command", command=ssh_connection)
myButton.pack()   
