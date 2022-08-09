FROM alpine:latest
ARG port
ARG production
ENV production=$production
ENV port=$port
RUN mkdir app
WORKDIR /app
COPY * .
RUN apk add python3 && apk add py3-pip && \
    pip3 install -r requirements.txt

VOLUME /var/log/

CMD /usr/bin/python3 app.py
