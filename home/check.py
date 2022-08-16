# import smtplib
# import qrcode 
# from email.message import EmailMessage
# tick='''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
#     integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
#     <script src="https://kit.fontawesome.com/15a00c5ce9.js" crossorigin="anonymous"></script>
#     <style>
#         body{
#             background-color: rgb(255, 178, 34);
#             height: auto;
#             width: auto;
#         }
#         .aboutus{
#             height: 100%;
#             width: 100%;
#         }

#         .aboutus h1{
#             text-align: center;
#         }

#         .aboutus h5{
#             text-align: center;
#         }

#         .aboutus h6{
#             text-align: center;
#             color: black;
#         }

#         .aboutus .card{
#             width: 100%;
#             background-color: rgb(255, 178, 34);;
#             border-radius: 20px;
#             border-color: rgb(255, 183, 0);
#             padding: 5%;
#         }

#     </style>
# </head>
# <body>
#     <div class="aboutus">
#         <div class="card">
#             <h1><B>PARKING TICKET</B></h1>
#             <h5>
#                 <h6>PARKING NAME : {{Parking_name}}</h6>
#                 <h6>PARKING TIME : {{Time}}</h6>
#                 <h6>PARKING DURATION : {{duration}}</h6>
#                 <h6>PARKING TOKEN : {{Token}}</h6>
#             </h5>
#         </div>
#     </div>
# </body>
# </html>'''
# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# try:
#     em = EmailMessage()
#     em['from'] = "parkersplace00@gmail.com"
#     em['To'] = 'patilsarthak999@gmail.com'
#     em['Subject'] = "Check this out"
   

#     em.add_alternative(tick,subtype='html')
#     if(server.login('parkersplace00@gmail.com','zvjyqgctatqdzszb')):
#         print("login successful")
#         server.sendmail('parkersplace00@gmail.com','patilsarthak999@gmail.com',em.as_string()) 
#         print ("Email Send")

        
#     else:
#         print ("Email not Send")
# finally:
#     server.quit()


from turtle import up
from .models import Users, Booking
from django.contrib.auth.models import User
up_users = User.objects.all()
for up_user in up_users:
    up_user.Profile.isOwner = "Yes"