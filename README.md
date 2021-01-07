**Dong Doorbell Readme**

Name: Ivan de Wergifosse Student Number: 20091388

Youtube demo and explanation video: [https://youtu.be/N-pjZc9Ibv8](https://youtu.be/N-pjZc9Ibv8)

Hello! Welcome to the readme for the Dong Doorbell, a video chat doorbell built using a Raspberry Pi 3b with some extra bits added on for good measure.

Below you will find a list of components and services needed, instructions on use and what script needs to be edited/changed for your own individual use. Also, below will be known bugs and issues, and credit for where script and code fragments were sourced.

**Components:**

This is a list of all components used in the construction of the Dong Doorbell:

- Raspberry Pi 3B+ (plus micro-USB power supply and micro-SD card)
- Sense HAT
- Raspberry Pi Camera V2 Camera Module
- CanaKit Breakout Board Bundle
- Mini black hat
- SunFounder USB 2.0 Mini Microphone
- Any speaker that connects using an audio jack (3.5mm for the Raspberry Pi)

Apps and services needed:

- Jitsi Meet (for mobile, available on iOS and Android)
- Blynk (for mobile, available on iOS and Android)
- Firebase (by google)
- Thingspeak
- Mailgun

**App Setup and Script Editing**

The script provided has several areas that need to be specific to the individual user. In this section we will do a brief run down of how to set up the required services for the app and what you need to take from each service to enter into the appropriate place within the script.

| Jitsi Meet | [Play Store](https://play.google.com/store/apps/details?id=org.jitsi.meet&amp;hl=en_IE&amp;gl=US) or[App Store](https://apps.apple.com/us/app/jitsi-meet/id1165103905) | This is the simplest part of the app, simply install the Jisti Meet app and it is ready for use, no need to creat an account.The chat ID will need to be entered into the chat\_id variable within the dong-call.py and dong-photo.py scripts. Please make sure this is the same in both scripts. |
| --- | --- | --- |
| Blynk | [Play Store](https://play.google.com/store/apps/details?id=cc.blynk&amp;hl=en_IE&amp;gl=US) or[App Store](https://apps.apple.com/us/app/blynk-iot-for-arduino-esp32/id808760481) | Download the app and start a new project. This will provide you with and Auth Token, which should be entered in to the BLYNK\_AUTH variable in the dong-call.py script. In the Blynk app, add the &quot;Notification&quot; Widget, then edit the widget settings: set the priority to &quot;High&quot; and in Customise Behavior make sure the &quot;Pop on screen&quot; option is enabled. Make sure to hit the play button to start the app when attempting to use it with your doorbell. |
| Firebase | [Website](https://firebase.google.com/) | Firebase is an online service that we will use as a cloud database for this project. Go to the website, click on &quot;Get Started&quot;, then &quot;Create a Project&quot;. Name your database, accept the terms and click &quot;Continue&quot;. Disable Google Analytics and click &quot;Create Project&quot;. Once the project is set up, click &quot;Continue&quot; to get to the dashboard. From here, click the \&lt;/\&gt; button, name your app and register it and continue to console. Open the settings of your app (the button under the title of your project that says 1 app, hit the gear). Go to the &quot;Services Accounts&quot; tab, select the Python option of the Firebase Admin SDK and generate and download the private key, name it serviceAccountKey.json and replace the file of the same name in this project with your own version.Also within Firebase, under the Build menu, go to the Realtime Database option and click &quot;Create Database&quot;, then next and in Security Rules select &quot;Start in test mode&quot; and then &quot;Enable&quot;. Copy the link that is displayed at the top of the database window and insert in as the Firebase link next to the databaseURL in the storeFileFB.py script. Similarly, under Build, then click on the Storage option and click &quot;Get Started&quot;. Hit next, and for the cloud storage option select your location from the drop-down menu and click done. Copy the link (minus the gs:// bit) and insert it in to the storageBucket variable in the storeFileFB.py script. |
| Thingspeak | [Website](https://thingspeak.com/login) | Thingspeak is an online service for data aggregation and analytics. In the Dong Doorbell all, we use ThingSpeak to track temperature, pressure and humidity. To use thingspeak, go to the website, sign up, log in and under Channels click on &quot;New Channel&quot;. Name your channel, and in Field 1 type Temp (or Temperature), in Field 2 type Press (or Pressure) and in Field 3 type Hum (or Humidity) and then click &quot;Save Channel&quot;. Then navigate to the &quot;API Keys&quot; and copy the Write API Key and insert it into the WRITE\_API\_KEY variable of the dawnreading.py |
| Mailgun | [Website](https://signup.mailgun.com/new/signup) | Mailgun is an API email service that can automatically send emails for you. For this project, go to the website, sign up (just use the free account, no need to provide card information). Once the service is set up, in the menu on the left, under Sending, click &quot;Overview&quot; and then under SMTP hit &quot;Select&quot;. This will display the SMTP credentials which you should enter into the appropriate fields under the def send\_mail in the dong-photo.py script. Also, within this script, set your own value for the from\_email and to\_email variables. Please note that the to email should be the same email with which you set up your Mailgun account. |
| Other individual script edits | There are only two other changes that needs to be made for the individual user. First, in the folder where the application files are saved, create a new folder called img. Lastly, insert the file path for the img folder in the dong-photo.py script on line 49 within the fileLoc variable. |

**Unit Build**

The Raspberry Pi build is relatively straightforward. See the video linked at the beginning of this document for a visual of what the construction looks like. Please not that if you change which GPIOs the button and LED are connected to you will need to change the GPIO number in the dong.py script.

**Program Use**

Once the unit has been built and the script and services set up as described above, simply execute the Dong-Doorbell.sh script to begin all the functions of the Dong Doorbell.

The Dong-Doorbell.sh script runs a while loop with two nested if loops that check if the dong.py and dawnreading.py scripts are running, if they are not then they are started (or restarted). The dawnreading.py script uses the Sense Hat each morning at 8 am to measure the temperature, pressure and humidity and this is uploaded to your Thingspeak channel.

The dong.py script is the main script that operates the doorbell itself. It waits for the button to be pressed, and once it is, if flashes the LED, it plays the Dong.wav sound bite, and then runs two further scripts one after the other, firstly the dong-photo.py script and then the dong-call.py script. The dong-photo.py script uses the attached camera to take a photo of the person who rang the doorbell, save that photo to the &quot;img&quot; folder (or wherever you have set the file destination to), uploads that photo to your Firebase storage and then email you that photo along with the notification that someone has rung the bell. The email will also contain a link to the video chat so that you can speak with the pesron at the door.

Once the dong-photo.py script has performed its functions the dong-call.py script is run. This script is responsible for starting the video chat using Jitsi Meet and sending a push notification to your phone via the Blynk app. The script allows the call to run for 1 minute (60 seconds) and then terminates the call. If you wish to allow the call to continue for longer simply adjust the number in the time.sleep(60) function on line 33 of this script.

Once the dong-call.py script has ended the dong.py script is terminated and then restarted by Dong-Doorbell.sh, if it is still running. This ensures that all the processes that are run during the dong.py execution are cleanely ended and that it is started again to a fresh session, reading for another doorbell press.

**Known Bugs and Issues**

While the call is clearly ended by the process, sometimes the video chat can take some time to actually end, so that if the doorbell is rung too quickly after the end of a call there will be two instances of the Raspberry Pi within the call, though the old one will be a muted black screen.

Ending the Dong-Doorbell.sh script does not end the dawnreading.py or dong.py programs. If you want to end them, you need to kill them from the terminal by finding their pi number and killing the process using that.

The dong.py process will end after each call, and so must be run through the Dong-Doorbell.sh script to ensure it continues to work. If you do not wish to use the dawnreading.sh part of this script, simply remove the nested if statement containing it.

**Improvement and Further Development Scope**

This app is prime for further development. Several things could be done with more time and testing, including voice activation of the app to avoid contact with the button itself, and motion sensing to detect motion and begin listening for voice activation so that it is not always listening. Another simple addition would be improvement of the Blynk app to display the most recent temperature reading so that it is more easily accessible.

**Credits and Refences**

Dong.wav was sourced from a clip found on [YouTube.com](https://www.youtube.com/watch?v=qaxTnh5zmFo&amp;ab_channel=SoundEffect)

Use of Blynk, Mailgun, Thingspeak and Firebase were inspired by practical work from Waterford IT. Code was also sourced from here for functinality.

Use of Jitsi Meet and some associated code inspired by and sourced from [HackerShack](https://www.hackster.io/hackershack)