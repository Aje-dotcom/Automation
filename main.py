'''
TITLE: AUTOMATING MESSAGE SENDING VIA 2 LINES OF CODE
Author Ekene Ajemba
URL: https://gist.github.com/Aje-dotcom/ee4b5ca48bda0aca4c682a1cf21729cb

First import the library using the command import pywhatkit as kit and then
proceed to call the functions

kit.sendwhatmsg()
This function can be used to send WhatsApp message at certain time
'''
import pywhatkit as eky
eky.sendwhatmsg('+2348032274561',
                'How are you doing Bae and why are you mot replying 2 my calls? ', 7, 53)
eky.text_to_handwriting("I love Bae")
eky.playonyt("From a distance")

# The parameters are phone_num (required)
#
# - Phone number of target with country code message (required)
# - Message that you want to sendwhatmsg time_hour (required)
# - Hours at which you want to send message in 24 hour format time_min (required)
# - Minutes at which you want to send message wait_time (optional, val=20)
# - Seconds after which the messa…



