import smtplib

copy_writing_gmail = "WILLIAM.RIVERA2@STU.BMCC.CUNY.EDU"
copy_writing_gmail_password = "GodisanEngineer12!"
sendee_email = "theavenger16@gmail.com"

gmail_connection = smtplib.SMTP("outlook.office365.com")
gmail_connection.starttls()  # transport layer security
gmail_connection.login(user=copy_writing_gmail, password=copy_writing_gmail_password)
gmail_connection.sendmail(from_addr=copy_writing_gmail, to_addrs=sendee_email, msg="ay lmao")
gmail_connection.close()
