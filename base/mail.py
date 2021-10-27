# 邮件模块
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import exists
from smtplib import SMTP


class Email:
    def __init__(
            self,
            sender: str,
            receiver: [str, list],
            # 主题
            title: str,
            server: str,
            auth_code: str,
            # 正文
            message: str = None,
            attachment_file: [str, list] = None,
    ):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.message = message
        self.attachment_file = attachment_file
        self.server = server
        self.auth_code = auth_code
        self.msg = MIMEMultipart('related')

    def send(self):
        self.msg["Subject"] = self.title
        self.msg["From"] = self.sender
        self.msg["To"] = self.receiver

        #  写入主题消息
        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.attachment_file:
            if isinstance(self.attachment_file, str):
                self._attach_file(self.attachment_file)
            if isinstance(self.attachment_file, list):
                for file in self.attachment_file:
                    self._attach_file(file)

        # 传入server对象
        smtp_server = SMTP(self.server)
        smtp_server.login(self.sender, self.auth_code)
        smtp_server.sendmail(self.sender, self.receiver, self.msg.as_string())
        smtp_server.quit()

    def _attach_file(self, file_path):
        if not exists(file_path):
            raise FileNotFoundError(
                f'{file_path}:附件文件不存在，或路径错误'
            )
        with open(file_path, 'r', encoding='utf-8') as f:
            att = MIMEText(f.read(), 'plain', 'utf-8')
            att["Content-type"] = 'application/octet-stream'

            file_name = re.split(r'[\\|/]', file_path)[-1]
            att["Content-Disposition"] = f'attachment; filename="{file_name}"'
            self.msg.attach(att)


mail = Email(
    title="TEST",
    sender='iam2cc@foxmail.com',
    receiver='1059995908@qq.com',
    server="smtp.qq.com",
    message="Test SMTP",
    auth_code='oqmnkweutuugbbcj',
    attachment_file=None
)

mail.send()