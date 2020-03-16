FROM python:alpine

LABEL maintainer="me@ikevinshah.com"

RUN pip install praw beautifulsoup4 \
&& echo "Creating 'python' user" \
&& adduser -u 1007 -S -D -H python \
&& echo "Switching to pyton user" \
&& mkdir -pv /scripts \
&& touch /scripts/bot.py \
&& chown -R python /scripts \
&& echo "Changed ownership to python user"; 

USER python

CMD ["python", "-u", "/scripts/bot.py"]
