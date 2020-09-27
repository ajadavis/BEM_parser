#!/usr/bin/env python3
import os
import sys
import json 
from collections import Counter
from datetime import datetime

# get current date
now = str(datetime.now()).replace(":", ".").replace(" ", "_")[:-7]

# INITIALIZE GLOBAL VARIABLE FOR SUB MENUS
choice_sub = 0


def main_menu():

    # COOL ASCII ART
    print("""
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\        
       /::::\    \              /::::\    \              /::::|   |        
      /::::::\    \            /::::::\    \            /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______  
 /:::/\:::\   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \ 
/:::/__\:::\   \:::|    |/:::/__\:::\   \:::\____\/:::/    |:::::::::\____\
\:::\   \:::\  /:::|____|\:::\   \:::\   \::/    /\::/    / ~~~~~/:::/    /
 \:::\   \:::\/:::/    /  \:::\   \:::\   \/____/  \/____/      /:::/    / 
  \:::\   \::::::/    /    \:::\   \:::\    \                  /:::/    /  
   \:::\   \::::/    /      \:::\   \:::\____\                /:::/    /   
    \:::\  /:::/    /        \:::\   \::/    /               /:::/    /    
     \:::\/:::/    /          \:::\   \/____/               /:::/    /     
      \::::::/    /            \:::\    \                  /:::/    /      
       \::::/    /              \:::\____\                /:::/    /       
        \::/____/                \::/    /                \::/    /        
         ~~                       \/____/                  \/____/         
        by Bryan Charbonneau, Evan Etienne, & Mike Crescenzi
        """)
    print("*******************BEM Log File Menu*******************")
    # print system or app log menu
    print()

    # GET USER INPUT
    choice = input ("""
                        1: System Logs
                        2: Application Logs
                        3: Quit/Log Out
                        Please make a selection: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice == "1":
        system_log_menu()
    elif choice == "2":
        application_log_menu()
    elif choice == "3":
        sys.exit
    else:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, or 3.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
# System Log Menu
def system_log_menu():
    print("*******************BEM System Log Menu*******************")
    # print system or app log menu
    print()
    # GET USER INPUT
    choice = input("""
                        1: Syslog
                        2: Kern.log
                        3: Auth.log
                        4: Back to Main Menu
                        Please enter your log file type: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice == "1":
        syslog_sub_menu()
    elif choice == "2":
        kern_log_sub_menu()
    elif choice == "3":
        auth_log_sub_menu()
    elif choice == "4":
        main_menu()
    else:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, or 3.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
# Syslog Sub-Menu User Interface
def syslog_sub_menu():
    print("*******************BEM Syslog Sub-Menu*******************")
    # print system or app log menu
    print()
    # CALL GLOBAL VARIABLE
    global choice_sub
    # GET USER INPUT
    choice_sub = input("""
                        1: Parse Log
                        2: Process Counter log
                        3: Both 
                        4: Back to Main Menu
                        Please enter your log file type: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice_sub == "4":
        main_menu()
    elif choice_sub not in ["1", "2", "3", "4"]:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
    syslog_parser()
# Kern.log Sub-Menu User Interface
def kern_log_sub_menu():
    print("*******************BEM Kern.log Sub-Menu*******************")
    # print system or app log menu
    print()
    # CALL GLOBAL VARIABLE
    global choice_sub
    # GET USER INPUT
    choice_sub = input("""
                        1: Parse Log
                        2: Message Counter log
                        3: Both 
                        4: Back to Main Menu
                        Please enter your log file type: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice_sub == "4":
        main_menu()
    elif choice_sub not in ["1", "2", "3", "4"]:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
    kern_log_parser()
# Auth.log Sub-Menu User Interface
def auth_log_sub_menu():
    print("*******************BEM Auth.log Sub-Menu*******************")
    # print system or app log menu
    print()
    # CALL GLOBAL VARIABLE
    global choice_sub
    # GET USER INPUT
    choice_sub = input("""
                        1: Parse Log
                        2: Info Counter log
                        3: Both 
                        4: Back to Main Menu
                        Please enter your log file type: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice_sub == "4":
        main_menu()
    elif choice_sub not in ["1", "2", "3", "4"]:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
    auth_log_parser()

# Application Log Menu
def application_log_menu():
    print("*******************BEM Application Log Menu*******************")
    # print system or app log menu
    print()
    # GET USER INPUT
    choice = input("""
                        1: Apache Access.log
                        2: Back to Main Menu
                        3: Quit/Log Out
                        Please enter your choice: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice == "1":
        apache_sub_menu()
    elif choice == "2":
        main_menu()
    elif choice == "3":
        sys.exit
    else:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, or 3.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()


# Access.log Sub-Menu User Interface
def apache_sub_menu():
    print("*******************BEM Access.log Sub-Menu*******************")
    # print system or app log menu
    print()
    # CALL GLOBAL VARIABLE
    global choice_sub
    # GET USER INPUT
    choice_sub = input("""
                        1: Parse Log
                        2: Source IP Counter log
                        3: Both 
                        4: Back to Main Menu
                        Please enter your log file type: """)
    # if the choice is 1, 2, or 3 go to the corresponding sub-menu
    if choice_sub == "4":
        main_menu()
    elif choice_sub not in ["1", "2", "3", "4"]:
        # error checking - if they put in nonsense, make sure they know what to do!
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")
        # Return to main menu for further options or to quit the program
        main_menu()
    apache_parser()

#SysLog Parser
def syslog_parser():

    # CALL GLOBAL VARIABLE
    global choice_sub

    #read log file in from commandline 
    file_path = sys.argv[1]
    # open the file
    with open(file_path, 'r') as log_file:

            # INITIATE LINE NUMBER COUNTER 
            LineNumber = 1

            # INITIATE DICTIONARIES
            my_dict = {}
            error_list = []
            
            #start parsing lines
            for line in log_file:

                    # STRIP LINES
                    line = line.strip()
                    if 'error' in line:
                        error_list.append(line)
                        
                    
                    # SPLIT LINES
                    parsed_lines = line.split(' ')

                    # SET VARIABLES
                    DT = parsed_lines[0] + ' ' + parsed_lines[1] + ' '+ parsed_lines[2]
                    MachineName = parsed_lines[3]
                    Process = parsed_lines[4]
                    Process = Process[:-1]
                    #info required an extra step
                    Info = parsed_lines[5:]
                    Info2 = ''
                    for x in Info:
                        Info2 = Info2 + ' ' + x
                    Info2 = Info2[1:]

                    # PUT VARIABLES INTO  DICTIONARY
                    dict1 = {"timeStamp": DT,"machineName": MachineName,"process": Process,"message": Info2}
                    my_dict [LineNumber] = dict1

                    # increment line number through loop
                    LineNumber = LineNumber + 1

            # counter dictionary
            syslogcounter = (Counter([i['process'] for i in my_dict.values()]))


            # OUTPUT TO JSON FILE BASED ON USER INPUT 
            if choice_sub == '1':
                out_file = open("syslog_" + now + ".json", "w")
                json.dump(my_dict, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '2':
                out_file = open("syslog_counter_" + now + ".json", "w")
                json.dump(syslogcounter, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '3':
                out_file = open("syslog_" + now + ".json", "w")
                json.dump(my_dict, out_file, indent = 6) 
                out_file.close() 
                out_file = open("syslog_counter_" + now + ".json", "w")
                json.dump(syslogcounter, out_file, indent = 6) 
                out_file.close() 
            else:
                print("User Input Error, Please verify user input")
            
            # OUTPUT ERROR FILE
            with open('syslog_errors_' + now + '.txt', 'w') as f:
                for item in error_list:
                    f.write("%s\n" % item)

def kern_log_parser():

    # CALL GLOBAL VARIABLE
    global choice_sub

    #read log file in from commandline 
    file_path = sys.argv[1]

    # open the file
    with open(file_path, 'r') as log_file:

            # INITIATE LINE NUMBER COUNTER 
            LineNumber = 1
            
            # INITIATE DICTIONARY
            my_dict = {}
            error_list = []

            #start parsing lines
            for line in log_file:

                # STRIP LINES
                line = line.strip()
                if 'error' in line:
                    error_list.append(line)

                ## SPLIT LINES
                parsed_lines = line.split(' ')

                # SET VARIABLES
                DT = parsed_lines[0] + ' ' + parsed_lines[1] + ' '+ parsed_lines[2]
                MachineName = parsed_lines[3]
                Process = parsed_lines[4]
                Process = Process[:-1]
                #info required an extra step
                Info = parsed_lines[5:]
                Info2 = ''
                for x in Info:
                    Info2 = Info2 + ' ' + x
                KernClock = Info2[0:15]
                Message = Info2[16:]
                

                # PUT VARIABLES INTO  DICTIONARY
                dict1 = {"timeStamp": DT,"machineName": MachineName,"process": Process,"kernelClock": KernClock,"message": Message}
                my_dict[LineNumber]=dict1

                # increment line number through loop
                LineNumber = LineNumber + 1

            # counter dictionary
            kernlogcounter = (Counter([i['message'] for i in my_dict.values()]))
                   
            # OUTPUT TO JSON FILE BASED ON USER INPUT
            if choice_sub == '1':
                out_file = open("kernlog_" + now + ".json", "w")
                json.dump(my_dict, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '2':
                out_file = open("kernlog_counter_" + now + ".json", "w")
                json.dump(kernlogcounter, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '3':
                out_file = open("kernlog_" + now + ".json", "w")
                json.dump(my_dict, out_file, indent = 6) 
                out_file.close() 
                out_file = open("kernlog_counter_" + now + ".json", "w")
                json.dump(kernlogcounter, out_file, indent = 6) 
                out_file.close() 
            else:
                print("User Input Error, Please verify user input")

            # OUTPUT ERROR FILE
            with open('kernlog_errors_' + now + '.txt', 'w') as f:
                for item in error_list:
                    f.write("%s\n" % item)
            
            
#AuthLog Parser
def auth_log_parser():

    # CALL GLOBAL VARIABLE
    global choice_sub

    #read log file in from commandline 
    file_path = sys.argv[1]

    # open the file
    with open(file_path, 'r') as log_file:

            #intiate line number counter to be used in future
            LineNumber = 1

            #initiate empty fields list to later append each variable during the for loop parsing process
            authlogDict = {}
            error_list = []

            #start parsing lines
            for line in log_file:
                # strip the line
                line = line.strip()
                if 'error' in line:
                    error_list.append(line)

                #split line on a space ' '
                parsed_lines = line.split(' ')

                #get the variables by referencing index position in the parsed_lines string
                DT = parsed_lines[0] + ' ' + parsed_lines[1] + ' '+ parsed_lines[2]
                MachineName = parsed_lines[3]
                Process = parsed_lines[4]
                Process = Process[:-1]
                #info required an extra step
                Info = parsed_lines[5:]
                Info2 = ''
                for x in Info:
                    Info2 = Info2 + ' ' + x
                Info2 = Info2[1:]

                dict1 = {"timestamp": DT, "machineName": MachineName, "process": Process, "info": Info2}
                authlogDict[LineNumber]=dict1

                # increment line number through loop
                LineNumber = LineNumber + 1

            # counter dictionary    
            authlogcounter = (Counter([i['info'] for i in authlogDict.values()]))
                 
            # OUTPUT TO JSON FILE BASED ON USER INPUT
            if choice_sub == '1':
                out_file = open("authlog_" + now + ".json", "w")
                json.dump(authlogDict, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '2':
                out_file = open("authlog_counter_" + now + ".json", "w")
                json.dump(authlogcounter, out_file, indent = 6) 
                out_file.close() 
            elif choice_sub == '3':
                out_file = open("authlog_" + now + ".json", "w")
                json.dump(authlogDict, out_file, indent = 6) 
                out_file.close()
                out_file = open("authlog_counter_" + now + ".json", "w")
                json.dump(authlogcounter, out_file, indent = 6) 
                out_file.close() 
            else:
                print("User Input Error, Please verify user input")

            # OUTPUT ERROR FILE
            with open('authlog_errors_' + now + '.txt', 'w') as f:
                for item in error_list:
                    f.write("%s\n" % item)
            

# Apache Access Parser
def apache_parser():

    # CALL GLOBAL VARIABLE
    global choice_sub

    # read log file in from commandline
    file_path = sys.argv[1]
    # open the file
    with open(file_path, 'r') as log_file:

        # intiate line number counter to be used in future
        Line_Number = 1

        # initiate empty dictionary to append separate dictionary for each line item in log
        apache_log_dict = {}
        error_list = []
        # start parsing lines
        for line in log_file:
            # strip the line
            line = line.strip()
            if 'error' in line:
                    error_list.append(line)

            # split line on a space ';'
            parsed_lines = line.split(';')

            # get the variables by referencing index position in the parsed_lines string
            LineNumber = parsed_lines[0]
            Date_Time = parsed_lines[1]
            Src_IP = parsed_lines[2]
            Src_Port = parsed_lines[3]
            Dest_IP = parsed_lines[4]
            Dest_Port = parsed_lines[5]
            IP_Proto = parsed_lines[6]
            IP_Length = parsed_lines[7]
            Proto = parsed_lines[8]
            Info = parsed_lines[9]

            # set dictionary Key:Value pairs for each line number
            dict1 = {"Time_Stamp": Date_Time, "Src_IP": Src_IP, "Src_Port": Src_Port, "Dest_IP" : Dest_IP, "Dest_Port" : Dest_Port, "IP_Proto" : IP_Proto, "IP_Length" : IP_Length, "Proto" : Proto, "Info" : Info}
            apache_log_dict [LineNumber] = dict1

            # increment line number through loop
            Line_Number = Line_Number + 1
        
        
        # counter dictionary
        apachelogcounter = (Counter([i['Src_IP'] for i in apache_log_dict.values()]))
            
        # OUTPUT TO JSON FILE BASED ON USER INPUT
        if choice_sub == '1':
            out_file = open("access_log_" + now + ".json", "w")
            json.dump(apache_log_dict, out_file, indent = 6) 
            out_file.close() 
        elif choice_sub == '2':
            out_file = open("accesslog_counter_" + now + ".json", "w")
            json.dump(apachelogcounter, out_file, indent = 6) 
            out_file.close() 
        elif choice_sub == '3':
            out_file = open("access_log_" + now + ".json", "w")
            json.dump(apache_log_dict, out_file, indent = 6) 
            out_file.close()
            out_file = open("accesslog_counter_" + now + ".json", "w")
            json.dump(apachelogcounter, out_file, indent = 6) 
            out_file.close() 
        else:
            print("User Input Error, Please verify user input")
        
        # OUTPUT ERROR FILE
        with open('accesslog_errors_' + now + '.txt', 'w') as f:
                for item in error_list:
                    f.write("%s\n" % item)
        
# Call Main Function
main_menu()