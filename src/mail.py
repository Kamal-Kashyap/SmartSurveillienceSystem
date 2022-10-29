import smtplib as s

ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("abc@gmail.com","abcd")

subject="TCDS Smart survillance"
body="Your Report has been forwarded Successfully  \n  It is an comformation email****"

message="Subject:{}\n\n{}".format(subject,body)

listofAddress=["xyz@gmail.com"]

ob.sendmail("abc",listofAddress,message)
print("send successfully...")
ob.quit()
