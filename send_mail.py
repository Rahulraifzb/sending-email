import os

# This is gmail library for sending some infomartion to gmail
import smtplib

# This is use for formating the email message
from email.message import EmailMessage

# It is used for checking image type
import imghdr

email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")


# with smtplib.SMTP("smtp.gmail.com",587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(email_address,email_password)

#     subject = "Grab dinner this weekend?"
#     body = "How about dinner at 6pm this saturday?"

#     msg = f"Subject: {subject}\n\n{body}"
#     smtp.sendmail(email_address,"rrai06125@gmail.com",msg)


#------------ Debuggung server -----------#

# with smtplib.SMTP("localhost",1025) as smtp:
#     subject = "Grab dinner this weekend?"
#     body = "How about dinner at 6pm this saturday?"
#     msg = f"Subject: {subject}\n\n{body}"
#     smtp.sendmail(email_address,"rrai06125@gmail.com",msg)

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login(email_address,email_password)
#     subject = "Grab dinner this weekend?"
#     body = "How about dinner at 6pm this saturday?"

#     msg = f"Subject: {subject}\n\n{body}"
#     smtp.sendmail(email_address,"rrai06125@gmail.com",msg)

# msg = EmailMessage()
# msg["Subject"] = "Grab dinner this weekend?"
# msg["From"] = email_address
# msg["to"] = "rrai06125@gmail.com"
# msg.set_content("How about dinner at 6pm this Saturday?")

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login(email_address,email_password)
#     smtp.send_message(msg)


# msg = EmailMessage()
# msg["Subject"] = "Check out Bronx as a puppy!"
# msg["From"] = email_address
# msg["To"] = "rrai06125@gmail.com"
# msg.set_content("Image attached...")

# with open("avatar.png","rb") as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name

# msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login(email_address,email_password)
#     smtp.send_message(msg)

# msg = EmailMessage()
# msg["Subject"] = "Checkout Bronx as puppy!"
# msg["From"] = email_address
# msg["To"] = "rrai06125@gmail.com"
# msg.set_content("Image attached..")

# files = ["avatar.png","puppy.jpg"]

# for file in files:
#     with open(file,"rb") as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login(email_address,email_password)
#     smtp.send_message(msg)




# msg = EmailMessage()
# msg["Subject"] = "Checkout Bronx as puppy!"
# msg["From"] = "rahul.rai@shepple.com"
# msg["To"] = "rrai06125@gmail.com"
# msg.set_content("Image attached..")

# files = ["result.pdf"]

# for file in files:
#     with open(file,"rb") as f:
#         file_data = f.read()
#         file_name = f.name

#     msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login("rahul.rai@shepple.com","iznhixsimnzoctcf")
#     smtp.send_message(msg)

# msg = EmailMessage()
# msg["Subject"] = "This is mailed by Rahul from shepple Technologies"
# msg["From"] = email_address
# msg["To"] = "rrai06125@gmail.com"
# msg.set_content("This is a plain text email")
# msg.add_alternative('''\
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Document</title>
#     </head>
#     <body>
#         <h3 style="color: aqua;">Hello Rahul</h3>
#     </body>
#     </html>
# ''',subtype="html")

# with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
#     smtp.login(email_address,"iznhixsimnzoctcf")

#     smtp.send_message(msg)















