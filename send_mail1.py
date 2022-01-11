import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("opcoc3@gmail.com", "Hello(2023)")

subject = "this is sending email using python"
body = "This is body part of email using python codes simple steps"

message = "Subject : {} \n {} ".format(subject,body)
# print(message)

listofaddress = ["opytc2@gmail.com","opcoc3@gmail.com"]
ob.sendmail("opcoc3@gmail.com",listofaddress,message)

ob.quit()
print("success")