import time

print ("Welcome to UN AND PW PROG") #put your own company, name or program between speech marks
print ("Press any key + ENTER to continue")
input()
print ("Enter Username:")

username = input()

if username == ("john-doe"): #put your own username between the speech marks
    time.sleep(2) #put your desired delay time (in seconds) in the brackets
    print ("User Identified as: " + username)
else: print ("Access Is Denied")

print ("Enter Password:")

password = input()

if password == ("j0hn-do3"): #put your own password between the speech marks
    time.sleep(2) #put your desired delay time (in seconds) in the brackets
    print ("Password Accepted, " + username)
else: print ("Password Is Incorrect. Session Terminated")


