# BEM_parser

BEM Parser is a log file parser for use on auth.log, syslog, kern.log, and Apache access.log files. This is a project for FullStack Academy Cybersecurity bootcamp and being so, this is only the initial version. There are many things that we would like to implement and the script is very scalable by design. In the current version, the parser will parse any of the 4 log file types specified and will output a JSON formatted file with date/time of the parse in the file name as well as an error.txt file if any errors are encountered.

Once downloading the file and giving execute permission, simply call the parser from the command line with the filepath of the log file you wish to parse: example: ./BEM_Parser.py /var/log/auth.log

Once running the script, there is a simple user interface to select the type of log file you are parsing and sub-menus for any/all parsing options.

The hope is that in the future, the script can be modified for real-world scenario business-use cases for detecting critical errors in any/all log file types and/or for use as another digital forensics tool to help correlate different log files by date and time.

Please Be Aware This script was only tested on Kali Linux 2020.3

Some log files between different operating systems could be either in different file/directory locations, have different log file names, or be in another format in which, this parser will not work as intended.
