# This program is intended to use only with chat_history.json files that are from snapchats user data
# Program is set to run file name "chat_history.json" and it will fail if file name changes, so keep that in mind
# if using vscode, all files must be in same folder and python be set to run in folder where files are located
# if there is letters such as ä or ö, they are replaced with "\u00e4" and "\u00f6" because I were too lazy to implement replacement system


import json
import re


def main():
    # opening files and creating log file if it doesn't exist yet
    filename = "chat_history.json"
    file = open(filename, "r")
    file_data = json.load(file)
    log = open("chat_log.txt", "a")
    
    # writing data to log file
    log.write("")
    log.write("---Received Saved Chat History---\n")
    log.write("")
    for i in file_data['Received Saved Chat History']:
        date = i.pop('Created') 
        type = i.pop('Media Type')
        line = json.dumps(i)

        line = re.sub('["}{]', '', line)

        print(line + " || date:" + date)
        log.write("\n"+line + " || date:" + date)

    # writing data to log file
    log.write("")
    log.write("\n\n---Sent Saved Chat History---\n")
    log.write("")
    for i in file_data['Sent Saved Chat History']:
        date = i.pop('Created') 
        type = i.pop('Media Type')
        line = json.dumps(i)

        line = re.sub('["}{]', '', line)

        print(line + " || date:" + date)
        log.write("\n"+line + " || date:" + date)

    # writing data to log file
    log.write("")
    log.write("\n\n---Received Unsaved Chat History---\n")
    log.write("")
    for i in file_data['Received Unsaved Chat History']:
        date = i.pop('Created') 
        type = i.pop('Media Type')
        line = json.dumps(i)

        line = re.sub('["}{]', '', line)

        print(line + " || date:" + date)
        log.write("\n"+line + " || date:" + date)
    
    # writing data to log file
    log.write("")
    log.write("\n\n---Sent Unsaved Chat History---\n")
    log.write("")
    for i in file_data['Sent Unsaved Chat History']:
        date = i.pop('Created') 
        type = i.pop('Media Type')
        line = json.dumps(i)

        line = re.sub('["}{]', '', line)

        print(line + " || date:" + date)
        log.write("\n"+line + " || date:" + date)

    # closing file
    log.close()
    


main()
