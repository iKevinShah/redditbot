# redditbot

Simple Image to technically run a python script in a separate container, but this one is specifically for a reddit bot based on `praw` (https://praw.readthedocs.io/en/latest/). Pretty easy to set it up. 

**Note:** The demo bot script in here is not mine. [/u/doug89](https://www.reddit.com/user/doug89 "/u/doug89") is the owner of the bot code.

Pull the image

````bash
[root@docker01 ~]# docker pull ikevinshah/redditbot
Using default tag: latest
latest: Pulling from ikevinshah/redditbot
...
Status: Downloaded newer image for ikevinshah/redditbot:latest
docker.io/ikevinshah/redditbot:latest

````

Check if the image exists.
````bash
[root@docker01 ~]# docker image ls ikevinshah/redditbot
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
ikevinshah/redditbot   latest              118f9e125487        2 minutes ago       119MB
[root@docker01 ~]#
````

Running the bot / container: 

# Method 1
The old fashioned way 
````bash
[root@docker01 ~]# docker run -dit --volume /path/to/bot.py:/scripts/bot.py ikevinshah/redditbot
[root@docker01 ~]# docker ps -a
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS                     PORTS                                                        NAMES
95ddf2b8162e        ikevinshah/redditbot          "python -u /scripts/…"   3 seconds ago       Up 2 seconds                                                                upbeat_galois

````
# Method 2
Running the bot via docker-compose. A Sample docker-compose file is provided. 
````bash
cd /path/to/directory
docker-compose up -d --force-recreate
````
---

Checking the bot output / logs:
````bash
[root@docker01 ~]# docker logs reddit-bot -f
Authenticating as SomeBot
Authenticated as SomeBot
---
Keyword matched keyword1
...
````


