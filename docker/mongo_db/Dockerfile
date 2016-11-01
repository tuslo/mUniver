FROM mongo:3.2

RUN apt-get update && \
    apt-get -y install python python-pip vim && \
    pip install bottle pymongo && \
    apt-get autoremove -y

ENTRYPOINT ["/entrypoint.sh", "--smallfiles"]