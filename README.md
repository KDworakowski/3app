# 3app
![Optional Text](../master/docs/docs.drawio.png)
## RabbitMQ Installation
You can install it using any package manager like apt or brew on macOS.

You also need to enable RabbitMQ Management Console, you can do it running `sudo rabbitmq-plugins enable rabbitmq_management` command.

Using homebrew you might need to add RabbitMQ and CLI scripts to the path.
You can do that adding below config to your shell config file
```
export HOMEBREW_RABBITMQ=/opt/homebrew/Cellar/rabbitmq/(version)/sbin/
export PATH=$PATH:$HOMEBREW_RABBITMQ
```
**IMPORTANT: Location of the homebrew may be different on your device, you can also try /usr/local/Cellar/rabbitmq/(version)/sbin/**

Then simply run `rabbitmq-server` or `homebrew services start rabbitmq`, default username and passwords are guest
## MongoDB Community Edition Installation
You can install it using any package manager like apt or brew on macOS.
[Here is the installation tutorial for some distros including Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

On macOS with homebrew simply run these commands
```
brew tap mongodb/brew
brew update
brew install mongodb-community@5.0
```

Then you can run it using `mongod` or `homebrew services start mongodb-community`.
## HTTPBIN
to run HTTP Bin simply run the command `docker run -p 80:80 kennethreitz/httpbin`
## Usage
After you installed all requirements and turned on HTTPBIN you should first run receiver by running command `./receive.py`.
Then you can send request using `./send.py` command. If you want to check the amount of object in the MongoDB database simply run `./getSize.py` command.

If you'll have any permissions issues try changing the files permissions using [chmod](https://linuxcommand.org/lc3_man_pages/chmod1.html).
## ERRORS
In case of any errors, plase make sure you have the correct version of the packages listed in `requirements.txt`.
Since pika has changed their arguments u can expect errors on older versions.
