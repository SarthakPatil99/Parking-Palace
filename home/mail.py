from smtplib import SMTP
server = SMTP('smtp.gmail.com',587)
server.starttls()
server.login('parkersplace00@gmail.com','picyvzasvezpelgz')
try:
    mes = '''hello how are you.....
    just checking for email'''
    server.sendmail('parkersplace00@gmail.com','patilsarthak999@gmail.com',mes)
    print("mailsent")
finally:
    server.close()