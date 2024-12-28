import smtplib,ssl #smtplib是郵件相關套件，ssl是加密套件,通常已經包含在電腦裡面
from email.mime.text import MIMEText # M大小寫有差別
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "yuhung.lin.lj@gmail.com"
receiver = ["cathy2000tw@gmail.com","cathy.lin.bt@gmail.com"]
passwd = "wybx zkaq uuep rxmn"
for i in receiver:
    msg = MIMEMultipart() # MIMEMultipart和input一樣，（msg作承接變數，可改）
    msg["From"] = sender # 概念同 a={"key": 123, "key2" : 345} ，新增至字典 a["key3"]=567
    msg["To"] = i
    msg["Subject"] = Header("Test send email","utf-8").encode() #若沒有設utf-8會出現亂碼，預設ASCII編碼)

    body = "This is email content, send by python"

    msg_text = MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com",587) as server: #google連線的port用587連線，是固定的
        server.starttls()
        server.login( sender,passwd)
        server.sendmail(sender,i,msg.as_string())
    print("success sent email")