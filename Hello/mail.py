import smtplib
# from email.message import EmailMessage

server = smtplib.SMTP_SSL('smtp.gmail.com',25)
# server.starttls()
# try:
#     em = EmailMessage()
#     em['from'] = "parkersplace00@gmail.com"
#     em['To'] = "suyashsv47@gmail.com"
#     em['Subject'] = "Check this out"
#     body='''This is an email for checking'''
#     em.set_content(body)
#     if(server.login('parkersplace00@gmail.com','zvjyqgctatqdzszb')):
#         print("login successful")
#     abc= server.sendmail('parkersplace00@gmail.com','suyashsv47@gmail.com',em.as_string()) 
#         # print ("Email Send") 
#     # else:
#         # print ("Email  not Send") 
#     print(abc)


# finally:

#     server.quit()