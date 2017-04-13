from smtplib import SMTP


fromaddr = 'deveshbajaj46@gmail.com'
toaddrs  = 'deveshbajaj59@gmail.com'
msg = 'YOYO honey'



username = 'deveshbajaj46@gmail.com'
password = '123456789Q'


server = SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
