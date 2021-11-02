import smtplib
import subprocess
from datetime import datetime #Import libraries
from email.message import EmailMessage


def time():
    output = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #Format new Time
    splited = output.split(" ")
    splited = splited[1].split(":") 
    return f"[{splited[0]}:{splited[1]}:{splited[2]}]" #Return formated time

def time_e():
    output = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Format new Time
    splited = output.split(" ")
    splited = splited[1].split(":")
    return f"{splited[0]}:{splited[1]}:{splited[2]}" #Return formated time without []

def main():
    print(f"{time()} Start")
    while True: #Start while-loop
        output = str(subprocess.check_output(['screen', '-ls']))
        if "<name>" not in output: #Set name
            print(f"{time()} Server reboot")
            send_mail("Enter a text which send if the server is crashed") #Send mail with custom text
            subprocess.run("cd ./server/ && screen -d -m -S <name> ./script.sh", shell=True) #Run command to start the screen
            print(f"{time()} Server started")


def send_mail(type, content):
    me = "<sender-account>"
    you = "<you>"

    msg = EmailMessage() #Get new EmailMessage
    msg['Subject'] = type
    msg['From'] = me #Set Email settings
    msg['To'] = you

    msg.set_content(content) #Set content

    # Send the message via local SMTP server.
    mail = smtplib.SMTP('<SMPT Server>', 587) #SMPT Port

    mail.ehlo()

    mail.starttls() # Connect

    mail.login("<sender-account>", "<password>") #Login
    mail.send_message(msg) #Send Email


if __name__ == "__main__":
    main() #Start
