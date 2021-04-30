FROM alpine

WORKDIR /root/dummy/

ADD https://github.com/gilbertchen/duplicacy/releases/download/v2.7.2/duplicacy_linux_x64_2.7.2 \
    /usr/local/bin/duplicacy
# /mnt/duplicacy/ is where the volume will be mounted
RUN mkdir -p /mnt/duplicacy && chmod +x /usr/local/bin/duplicacy
