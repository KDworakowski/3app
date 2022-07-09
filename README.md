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

## HTTPBIN
to run HTTP Bin simply run the command `docker run -p 80:80 kennethreitz/httpbin`
## ERRORS
In case of any errors, plase make sure you have the correct version of the packages listed in `requirements.txt`.
Since pika has changed their arguments u can expect errors on older versions.
