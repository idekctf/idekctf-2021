FROM python:3.9-slim

RUN apt-get update && apt-get -y install socat

WORKDIR /

COPY *.py ./

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:'/main.py',pty,ctty,echo=0

