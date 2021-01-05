from picamera import PiCamera
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import time
import storeFileFB
import sys
import uuid

camera = PiCamera()

chat_id = 'GET-YOUR-OWN-CHAT-ID' # This chat ID should be the same as the one within the dong-call.py file

from_email = 'FROM-EMAIL@EXAMPLE.com'
to_email = 'TO-EMAIL@EXAMPLE.com'

def send_mail(eFrom, to, subject, text, attachment):
    # SMTP Server details: update to your credentials or use class server
    smtpServer='GET-YOUR-OWN-SERVER'
    smtpUser='GET-YOUR-OWN-USER'
    smtpPassword='GET-YOUR-OWN-PASSWORD'
    port=587

    # open attachment and read in as MIME image
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msgImage['Content-Disposition'] = 'attachment; filename="image.jpg"'
    msg.attach(msgImage)
    msg['Subject'] = subject

    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()

camera.start_preview()
frame = str(uuid.uuid4()) # Creates unique ID for the image to avoid duplicates

if __name__ == '__main__':
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    fileLoc = f'YOUR-FILE-PATH-HERE/img/frame{frame}.jpg' # set location of image file
    camera.capture(fileLoc) # Camera takes a picture of anyone who rings the doorbell
    text= f'Dong! Someone rang your doorbell at {currentTime}, see who it is and talk with them at http://meet.jit.si/%s' % chat_id
    send_mail(from_email, to_email, 'Dong! Someone is at the door.', text, fileLoc) # Sends and email with the photo of the caller and a link to the meeting (in case the blynk app malfuctions
    print(f'frame {frame} taken at {currentTime}') # print frame number to console

    storeFileFB.store_file(fileLoc)
    storeFileFB.push_db(fileLoc, currentTime)
