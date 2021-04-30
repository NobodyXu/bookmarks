FROM alpine

ARG url="https://github.com/gilbertchen/duplicacy/releases/download/v2.7.2/duplicacy_linux_x64_2.7.2"

WORKDIR /root/dummy/

# /mnt/duplicacy/ is where the volume will be mounted
RUN mkdir -p /mnt/duplicacy && \
    wget "$url" -O /usr/local/bin/duplicacy && chmod +x /usr/local/bin/duplicacy
