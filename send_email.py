# Send Emails using Python SMTP
'''
Python has an SMTP client library (smtplib), 
which it will use to send emails to an SMTP server (Gmail).
'''
import smtplib

'''
Any email using SMTP must have the following contents:

The Sender address
The receiver address
A subject (Optional)
The body of the mail
'''
sender_address = "weblinkravi01@gmail.com" #Replace this with your Gmail address
receiver_address = "ravikrrahul0@gmail.com"
account_password = "Ravi@#$1995"
subject = "Test email using python"
body = "Hello this is Ravi Rahul, \nA developer. \n\nSeding email through python!\nWith regards,\n\tDeveloper"

# Endpoint for the SMTP Gmail server (Don't change this!)
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Login with your Gmail account using SMTP
smtp_server.login(sender_address, account_password)

# Let's combine the subject and the body onto a single message
message = (f"Subject : {subject} \n\n {body}")

# We'll be sending this message in the above format (Subject:...\n\nBody)
smtp_server.sendmail(sender_address, receiver_address, message)

print(" Email has been sent")
# Close our endpoint
smtp_server.close()