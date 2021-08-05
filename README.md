## Installation
These instructions require you to have Docker installed, and have a discord developer portal with your developer bot.

```
$ git clone https://github.com/ChrisWeldon/SpottyMusicSaver.git

```

1. Configure environment variables

```
$ touch SpottyMusicSaver/spottyd/.env
$ echo  DISCORD_TOKEN="<The Bots token ID from Discord portal>"
```

2. Build the container with the docker images

```
$ cd SpottyMusicSaver
$ docker-compose up --build
```

3. Run the service

```
$ docker-compose up
// OR to run in detached mode
$ docker-compose up -d
// Then when done
$ docker-compose down spotty
```

Put all code in `src`, check TODO's to see what can be done.
