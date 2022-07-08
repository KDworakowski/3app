# 3app

## RabbitMQ Installation
To run any of the apps properly you should have rabbitmq installed on your machine. You can install it using any package manager like apt or brew on macos.

You also need to enable RabbitMQ Management Console, you can do it running `sudo rabbitmq-plugins enable rabbitmq_management` command.

Using homebrew you might need to add RabbitMQ and CLI scripts to the path.
You can do that adding below config to your shell config file
```
export HOMEBREW_RABBITMQ=/opt/homebrew/Cellar/rabbitmq/(version)/sbin/
export PATH=$PATH:$HOMEBREW_RABBITMQ
```
**IMPORTANT: Location of the homebrew may be different on your device, you can also try /usr/local/Cellar/rabbitmq/(version)/sbin/**

Then simply run `rabbitmq-server`, default username and passwords are guest
