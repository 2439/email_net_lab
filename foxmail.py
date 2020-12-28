from socket import *
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
#in
subject = "I love computer networks!"
# contenttype = "text/plain"
contenttype = "multipart/related"
# message
msg = MIMEMultipart()
body = """
<p>I love computer networks!</p>
<p>
<br><img src = "cid:image1"></br>
</p>
"""
mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
msg.attach(mail_body)
fp = open("test.jpg",'rb')
image = MIMEImage(fp.read())
fp.close()
image.add_header('Content-ID', '<image1>')
msg.attach(image)

endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server)
# and call it mailserver
# Fill in start
mailserver = "smtp.qq.com"
# Fill in end
# Sender and reciever
# Fill in start
sender = "2439504029@qq.com"
receiver = "marcia_zms@163.com"
# Fill in end

# Auth information (Encode with base64)
# Fill in start
senderName = base64.b64encode(sender.encode())
# senderCode = base64.b64encode(b"JGTHQLDNJNQMLCZE")
senderCode = base64.b64encode(b"ofajdimfcwejebee")
# Fill in end

# Create socket called clientSocket
# and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Auth
# login
login = 'auth login\r\n'
clientSocket.send(login.encode())
recv = clientSocket.recv(1024).decode()
clientSocket.send(senderName + b'\r\n')
recv = clientSocket.recv(1024).decode()
clientSocket.send(senderCode + b'\r\n')
recv = clientSocket.recv(1024).decode()
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
senderCommand = 'mail from:<' + sender + '>\r\n'
clientSocket.send(senderCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
receiverCommand = 'rcpt to:<' + receiver + '>\r\n'
clientSocket.send(receiverCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'data\r\n'
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
msgCommand = 'SUBJECT:' + subject + '\r\n'
msgCommand += 'contenttype:' + contenttype + '\r\n'
msgCommand += msg.as_string()
clientSocket.send(msgCommand.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250' and recv[:3] != '554':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '221':
    print('221 reply not received from server.')
# Fill in end
# Close connection
# Fill in start
clientSocket.close()
# Fill in end