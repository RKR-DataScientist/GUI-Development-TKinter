import smtplib
 
sender_address = "weblinkravi01@gmail.com" # Replace this with your Gmail address
 
receiver_address = "ravikrrahul0@gmail.com" # Replace this with any valid email address
 
account_password = "Ravi@#$1995" # Replace this with your Gmail account password
 
subject = "Test Email using Python"
 
body = "Hello from AskPython!\n\nHappy to hear from you!\nWith regards,\n\tDeveloper"
 
# We can use a context manager
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
    # Login with your Gmail account using SMTP
    smtp_server.login(sender_address, account_password)
 
    # Let's combine the subject and the body onto a single message
    message = f"Subject: {subject}\n\n{body}"
 
    # We'll be sending this message in the above format (Subject:...\n\nBody)
    smtp_server.sendmail(sender_address, receiver_address, message)