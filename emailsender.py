import smtplib
sendermail=input('enter the sendermail:')
receivermail=input('enter the receiver mail:')
password=input('enter the password:')
message='this mail is send my server using python'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sendermail,password)
print('login sucessful')#to login successful you must turn on the less secure app access in google.com

server.sendmail(sendermail,receivermail,message)
print('mail sent successsfully')

