# -*- encoding : utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import utils.readConfig as rc


localConfig = rc.ReadConfig()

class emailConf:
    def __init__(self):
        global shost, sUser, sPassword, sport, fromUser, toUser, subject, text, attachfile, on_off, ListToUser
        shost = localConfig.get_email("mail_host")
        sUser = localConfig.get_email("mail_user")
        sPassword = localConfig.get_email("mail_pass")
        sport = localConfig.get_email("mail_port")
        fromUser = localConfig.get_email("sender")
        # toUser = list(localReadConfig.get_email("receiver").__str__().split(";"))
        toUser = localConfig.get_email("receiver")
        ListToUser = localConfig.get_email("receiver").split(",")
        subject = localConfig.get_email("subject")
        on_off = int(localConfig.get_email("on_off"))
    def configEmail(self, text_bugs):
        msg = MIMEMultipart()
        #邮件头信息
        msg['From'] = fromUser
        msg['TO'] = toUser
        msg['subject'] = Header(subject, "utf-8")

        # 组织文本信息，邮件正文信息
        msgtext = MIMEText(text_bugs, _subtype='html', _charset='utf-8')
        msg.attach(msgtext)
        return msg

    def sendMail(self, text):
        msg = self.configEmail(text)
        smtp = smtplib.SMTP()

        if on_off == 1:
            try:
                smtp.connect(host=shost, port=sport)
                smtp.login(user=sUser, password=sPassword)
                smtp.sendmail(from_addr=fromUser, to_addrs=ListToUser, msg=msg.as_string())
                print(toUser)

            except smtp.SMTPException as e:
                print(e)
            finally:
                print("邮件已发送成功")
                smtp.quit()
        elif on_off == 0:
            print("邮件未发送")


#
# if __name__ == "__main__":
#     text = "gulinjie,wqeqeqeerew"
#     emailConf().sendMail(text)
