
# Email Reader Using Python
# Note: To use this you have to turn on the low secure app access from the google account
# We make do changes like to give speech access to the mail fetching from gmail., we can read and write the message in text file.

# import imaplib
# import email
# import traceback

# from_email='Enter your email address'
# from_password='Enter your password'
# smtp_server='imap.gmail.com'
# smtp_port=993

# def read_email():
#     # here we will use exception handling (try and except)
#     try:
#         # to connect to the server
#         mail=imaplib.IMAP4_SSL(smtp_server,smtp_port)
#         mail.login(from_email,from_password)
#         mail.select('inbox')
#         data=mail.search(None,'ALL')
#         mail_ids=data[1]
#         # print(mail_ids)
#         id_list=mail_ids[0].split()
#         first_email_id=int(id_list[0])
#         latest_email_id=int(id_list[-1])
#         for (index,i) in enumerate(range(latest_email_id,first_email_id,-1)):
#             data=mail.fetch(str(i),'(RFC822)')
#             for response in data:
#                 arr=response[0]
#                 if isinstance(arr,tuple):
#                     msg=email.message_from_string(str(arr[1],'utf-8'))
#                     # print(msg.keys())
#                     email_subject=msg['subject']
#                     email_from=msg['from']
#                     date=msg['Date']
#                     print(index+1)
#                     print("Date: \n",date)
#                     print("From: = \n"+email_from)
#                     print("Subject: \n"+str(email_subject))
#                     print("-"*10)
#             if index>15:
#                 break

#     except Exception as e:
#         traceback.print_exc()
#         print(str(e))

# read_email()
