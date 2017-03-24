#Rigreset_django

This is a django based server you can run on a raspberry pi in combination with a gpio relay or a custardpi v6 relayboard.

A small client will run on your miner that will post a Heartbeat to a rest api endpoint running on the server.

 The server will then trigger a reboot of the rig of a number of HB are missed.
 Also manually rebooting rigs will be possible.

 I created all starting from an API, so it's easily extensible and if needed it can be made distributed, with one server managing lots of relays.

 I also plan on putting a log monitoring feature in the client, to check the miner log is still adding lines, and if not alert the server.

Other ideas are to use the log file and/or any json ports (like Claymore's) and add the statistics to the gui.

#how to install

git clone this repo

needed python3
pip3 -r requirements.txt

python3 manage.py runserver

/webinterface : webgui
/api/miners : miner list
/admin : admin interface

default user and password for the admin gui
admin password1234!



#### extra stuff to include later:

Celery the background task runner needs rabbitmq as a transport backend
install rabbitmq
runs on
http://localhost:15672
user guest passwd guest

celery background process start:

celery -A rigreset_django worker -l info

