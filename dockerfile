FROM alpine:latest
ARG port
ARG flask_env
ENV flask_env=$flask_env
ENV port=$port
RUN mkdir app
WORKDIR /app
COPY * .
RUN apk add python3 && apk add py3-pip && \
    pip3 install -r requirements.txt

VOLUME /var/log/

CMD /usr/bin/python3 app.py
