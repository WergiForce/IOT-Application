import os
import datetime, time
from time import sleep
import signal
import subprocess
import blynklib

BLYNK_AUTH = 'GET-YOUR-OWN-BLYNK-AUTH-KEY'

blynk = blynklib.Blynk(BLYNK_AUTH)

chat_id = 'SET-YOUR-OWN-CHAT-ID' # Chat ID can be changed for different users of the service, please ensure it is the same in the dong-photo.py file

meetinglink = 'http://meet.jit.si/%s' % chat_id

# Create a video chat class to cleanly run the call and end it.
class VideoChat:
    def __init__(self):
        self._process = None

    def start(self):
        self._process = subprocess.Popen(["chromium-browser", "--display=:0", meetinglink]) # Opens the Chormium browser with the chat window to allow for the video chat

    def end(self):
        if self._process:
            os.kill(self._process.pid, signal.SIGTERM)

if __name__ == '__main__':
    video_chat = VideoChat()
    blynk.run()
    blynk.notify(meetinglink) # Sends push notification to the Blynk app with the link for the chat so it can be quickly opened.
    video_chat.start()
    time.sleep(60) # After the chat has started, let it run for one minute and then end it.
    video_chat.end()

