import flask 
import os
import logging
logging.basicConfig(filename='/var/log/webserver.log', encoding='utf-8', level=logging.DEBUG)

app = flask.Flask(__name__)

port = os.getenv("port")
if port.isdigit():
    app.run('0.0.0.0',port)
    logging.info("Started application")
else:
    app.logger.error("Can't start application provided wrong value: ",type(port))
    logging.error("The application wasn't started because there was wrong value of port ENV")

@app.route("/")
def _wellcome():
    return flask.send_file('index.html')
@app.route("/healthcheck")
def _healthcheck():
    return flask.send_file('health.html')
@app.route("/host_ip")
def host_ip():
    return flask.request.remote_addr
