import os
from termcolor import colored

try:
    #Select Sessions folder. This is recursive, all other folders down from here will also be queried
     path = "C:\\path\\HighestFolder"
except Exception as catchAllConnectionException:
    print('--------------------------------------------------------')
    print(colored(catchAllConnectionException, 'red'))
    print('--------------------------------------------------------')
else:
    print('--------------------------------------------------------')
    print(colored(f'Looking recursively for all files and folders under {path}', "green"))
    #Empty current Output.txt file
    with open(f'.\Output.txt', 'w'):
        pass
    try:
        #os.walk makes it recursive
        for path, dirs, files in os.walk(path):
            for filename in files:
                fullpath = os.path.join(path, filename)
                with open(fullpath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.find('"Hostname"=') != -1:
                            hostname = line.split('=',1)
                            hostname = hostname[1]
                            if len(hostname) > 1 :
                                #Write the output to a text file
                                with open(f'.\Output.txt', 'a') as outputFile:
                                    outputFile.write(hostname)
        print(colored(f'The hostnames were saved to .\Output.txt',"green"))
        print('--------------------------------------------------------') 
    except Exception as catchAllOutputException:
        print(colored(catchAllOutputException, 'red'))
        print('--------------------------------------------------------')                     