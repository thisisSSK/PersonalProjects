__author__ = 'thisisSSK'

import poplib
import pprint
import email
import string

# User input of server information
host = raw_input("Enter POP3 Host : ")
port = int(raw_input("Enter POP3 port: "))
username = raw_input("Enter username: ")
password = raw_input("Enter password: ")


server = poplib.POP3_SSL(host,port)
pp = pprint.PrettyPrinter(indent = 5)

# Just making sure that we are A-OK with the server
print server.getwelcome()

# Logging in
server.user(username)
server.pass_(password)

# Lets look at how many messages you have
stat = server.stat()
print "Unread Messages: %s (%s bytes" %stat

# Getting latest email (one-based)
last = server.retr(2)
# Convert gibberish into string
str_last = string.join(last[1], "\n")


msg = email.message_from_string(str_last)
str_msg = ''
#Printing Message details
str_msg += "Date : " + msg["Date"] + "\n"
str_msg += "From : " + msg["From"] + "\n"

for p in msg.walk():
    if p.is_multipart():
        continue
    print p.get_content_type()
    if p.get_content_type() == 'text/plain':
        print p.get_payload()
        body = "\n" + p.get_payload() + "\n"
    dtypes = p.get_params(None, 'Content-Disposition')
    if not dtypes:
        if p.get_content_type() == "text/plain":
            continue
        ctypes = p.get_params()
        if ctypes == False:
            continue
        for key,value in ctypes:
            if key.lower() == 'name':
                str_msg += "Attachment:" + value + "\n"
                break
    else:
        attachment,filename = None, None
        for key,val in dtypes:
            key = key.lower()
            if key == 'filename':
                filename = val
            if key == 'attachment':
                attachment = 1
        if not attachment:
            continue
    bod_exists = 'body' in locals() or 'body' in globals()
    if bod_exists:
        str_msg += body + "\n"
print str_msg



