# pylog-python-keylogger

## A Linux Keylogger that sends to email.
This is a simple python keylogger that demonstrates how a victims keystrokes can be recorded and sent back to an attacker without the victim knowing. It is set to start at startup so it ensures that all keystrokes is logged. It has been modified to check if there is an internet connection and if not -record all keystrokes to a text file.

## Objectives
1. The keylogger must allow you to send the keystrokes of the victim to a specified email
2. On startup:
   1. check if python is installed
   2. if so then install requirements
   3. Then run main file
3. Check if there is an internet connection.
4. if so then:
   1. then record keystrokes to a file for 30 minutes and then send that file via email
   2. Name that file with random filename that increments. and has a timestamp.
5. If not then copy the key strokes to a text file
6. if there is a pause for 30 seconds then skip next 2 lines
7.  


## Workflow
1. Listen for keystorkes in the background
2. If keystroke is entered, record the keystrokes in a list and then if the activity stops for 5 seconds push the saved text to a text/log file with a filename that has a non-suspicious filename with a timestamp.
3. After every 30 minutes, check if there is an internet connection
   1. If so then attach the saved log file to the email and send, then delete file in local storage.
   2. If there is no internet connection, then push text  ("Victim is still offline at {timestamp}) and continue the cycle.


### Questions that arises?
1. How to send the keystrokes to an email?
2. How to ensure that it is continuously running in the background?
3. Save keystrokes to a file in current directory
4. When it reaches the 25 minute cycle, another program takes the file and sends it to the email.

## How to run

### References

[Keyboard Logger on pyinput](https://pypi.org/project/pynput/)

[Send Emails using Python](https://realpython.com/python-send-email/)
[pyxhook- library for linux](https://pypi.org/project/pyxhook/)