"""
This is largely taken from the following:
https://www.textsendr.com/emailsms.php
https://automatetheboringstuff.com/chapter16/
Ethan Kendal at elkend@hot mail.com
"""
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os;

gmail_user = "";#this is the email of the junk account
gmail_pwd = "";#this is the password for the above account.

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

#add every known SMS server to loop through
GateWays = {'@msg.acsalaska.com','@message.alltel.com','@paging.acswireless.com','@archwireless.net','@txt.att.net','@txt.bellmobility.ca','@blueskyfrog.com','@myboostmobile.com','@cwwsms.com','@mobile.celloneusa.com'}
GateWays.add('@csouth1.com')
GateWays.add('@gocbw.com')
GateWays.add('@mobile.mycingular.com')
GateWays.add('@mmode.com')
GateWays.add('@clarotorpedo.com.br')
GateWays.add('@sms.comviq.se')
GateWays.add('@mms.mycricket.com')
GateWays.add('@sms.edgewireless.com')
GateWays.add('@einsteinsms.com')
GateWays.add('@fido.ca')
GateWays.add('@immixmail.com')
GateWays.add('@mymetropcs.com')
GateWays.add('@m1.com.sg')
GateWays.add('@sms.co.za')
GateWays.add('@messaging.nextel.com')
GateWays.add('@pcs.ntelos.com')
GateWays.add('@optusmobile.com.au')
GateWays.add('@orange.net')
GateWays.add('@orange.pl')
GateWays.add('@text.plusgsm.pl')
GateWays.add('@qwestmp.com')
GateWays.add('@pcs.rogers.com')
GateWays.add('@pcs.sasktelmobility.com')
GateWays.add('@mysmart.mymobile.ph')
GateWays.add('@mysmart.mymobile.ph')
GateWays.add('@page.southernlinc.com')
GateWays.add('@messaging.sprintpcs.com')
GateWays.add('@tms.suncom.com')
GateWays.add('@mobile.surewest.com')
GateWays.add('@bluewin.ch')
GateWays.add('@tmomail.net')
GateWays.add('@T-D1-SMS.de')
GateWays.add('@t-mobile.uk.net')
GateWays.add('@tbayteltxt.net')
GateWays.add('@mobilpost.no')
GateWays.add('@msg.telus.com')
GateWays.add('@timnet.com')
GateWays.add('@utext.com')
GateWays.add('@vmobile.ca')
GateWays.add('@vtext.com')
GateWays.add('@vmobl.com')
GateWays.add('@voda.co.za')
GateWays.add('@vodafone.net')
GateWays.add('@sms.vodafone.it')
GateWays.add('@sms.welcome2well.com')

def text(phoneNumber, subject, text):
   text += "  ";
   """for some reason the last two characters always get cut off.
    So adding two spaces at the end makes up for it."""
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = phoneNumber
   msg['Subject'] = subject
   text = MIMEText(text)
   msg.attach(text)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   for each in GateWays:
       mailServer.sendmail(gmail_user, phoneNumber + each, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()
