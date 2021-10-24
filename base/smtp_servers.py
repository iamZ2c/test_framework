import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time


class SmtpServers:
    def __init__(self, mail_host=None, mail_port=None, send_account=None, password=None, title=None):
        if mail_host is None:
            self.mail_host = 'smtp.qq.com'
        else:
            self.mail_host = mail_host
        if mail_port is None:
            self.mail_port = '465'
        else:
            self.mail_host = mail_port
        if send_account is None:
            self.send_account = 'iam2cc@foxmail.com'
        else:
            self.send_account = send_account
        if send_account is None:
            self.password = 'dlivgvnclucobbgc'
        else:
            self.send_account = password
        if title is None:
            self.title = "一道云质保组自动化测试报告"
        else:
            self.title = title
        self.sendName = "iam2cc"

    # 参数是收件人
    def sendmail(self, receivers, e_text=None, files_names=None):
        """

        :param receivers: 收件人
        :param e_text: 邮件正文
        :param files_names: list类型传入多个文件路径参数
        :return:
        """
        if e_text:
            msg = MIMEMultipart()
            text = MIMEText(e_text, 'plain', 'utf-8')
            msg.attach(text)
        else:
            e_text = "尊敬的各位领导及同事：质量控制部测试组针对斗学网产品基础功能进行了自动化测试，" \
                     "发现问题详见测试报告，无流程阻塞，请尽快修复，详情请查看附件！谢谢！\n{}".format(
                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            msg = MIMEMultipart()
            text = MIMEText(e_text, 'plain', 'utf-8')
            msg.attach(text)

        if files_names:
            print(files_names)
            for file_name in files_names:
                doc_file = os.path.dirname(os.getcwd()) + "\\report\\{}".format(file_name)
                doc_apart = MIMEApplication(open(doc_file, 'rb').read())
                doc_apart.add_header('Content-Disposition', 'attachment', filename="质保部自动化测试报告,生成时间:{}.html".format(
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
                msg.attach(doc_apart)

        msg['From'] = formataddr([self.sendName, self.send_account])
        # 邮件的标题
        msg['Subject'] = self.title

        try:
            server = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            server.login(self.send_account, self.password)
            server.sendmail(self.send_account, [receivers, ], msg.as_string())
            server.quit()
            print("已发送到" + receivers + "的邮箱中！")
        except smtplib.SMTPException:
            print("Error 无法发送邮件,密码有误")

    def get_all_report(self):
        """
        获取所有report目录报告名字
        :return:list类型,report目录下所有文件名称
        """
        path = os.path.dirname(os.getcwd()) + "\\report\\"
        self.report_list = os.listdir(path)
        return self.report_list

