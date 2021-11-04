# 邮件模块
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import exists
from smtplib import SMTP
from util.decorector import add_log
from config import settings


class Email:
    def __init__(
            self,
            sender: str = settings.SENDER,
            receivers=settings.RECEIVERS,
            # 主题
            title: str = settings.TITLE,
            server: str = settings.SERVER,
            auth_code: str = settings.AUTH_CODE,
            # 正文
            message: str = settings.MESSAGE,
            attachment_file: [str, list] = settings.ATTACHMENT_FILE,
    ):

        self.sender = sender
        self.receiver = receivers
        self.title = title
        self.message = message
        self.attachment_file = attachment_file
        self.server = server
        self.auth_code = auth_code
        self.msg = MIMEMultipart('related')

    @add_log
    def send(self):
        #  写入主题消息
        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.attachment_file:
            if isinstance(self.attachment_file, str):
                self._attach_file(self.attachment_file)
            if isinstance(self.attachment_file, list):
                for file in self.attachment_file:
                    self._attach_file(file)

        smtp_server = SMTP(self.server)
        smtp_server.login(self.sender, self.auth_code[0])

        self.msg["Subject"] = self.title
        self.msg["From"] = self.sender

        for receiver in self.receiver:
            self.msg["To"] = receiver
            # 传入server对象
            smtp_server.sendmail(self.sender, receiver, self.msg.as_string())

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
