#coding=gbk
# @Time : 2020/5/10 20:30
# @Author : lifangfang

##����OK


import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join( current_path , '..' , 'reports/�����Զ������Ա���.zip' )

smtp_server = 'smtp.qq.com'  # �ʼ���������ַ
smtp_sender = '2560482332@qq.com'  # ������
smtp_senderpassword = 'zyuwlttrrrzgecaj' # ��Ȩ��
smtp_receiver = '1280113591@qq.com' #�ռ���
smtp_cc = '1280113591@qq.com'  #������
smtp_subject = '�Զ������Ա��棨���԰棩' #�ʼ�����
smtp_body = '����python�ʼ�����' # �ʼ�����
smtp_file = dri_path

# msg = MIMEText(smtp_body, "html", "utf-8") #�ʼ���Ϣ����
# msg['from'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject

msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    # / Users / liuqingjun / PycharmProjects / PO_UI_Test_Framework /reports/�����Զ������Ա���V2.3/�����Զ������Ա���.zip
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', smtp_file.split('/')[-1]) )
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body, "html", "utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject


smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())






