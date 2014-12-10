import os
import requests
import tinycss2
from tinycss2 import color3
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def merry_christmas():
  return 'Merry Christmas!'


@app.route('/deployed', methods=['GET'])
def deployed():
  # Used to help with automatic deployments using the Heroku Button
  # Upon successful deployment, this URL is brought up
  return '<h1>Great! This application is ready.</h1><p>Now you just need to hook it \
  up to your Twilio account. Go to your Twilio dashboard, click on your phone number \
  to get to its settings page, and enter this in the Message Request URL Field: \
  <strong id="js-url"></strong> (also make sure the method is set to HTTP POST).</p>\
  <script>document.getElementById("js-url").innerHTML = document.URL.split("deployed")[0] + "sms"</script>'


@app.route('/sms', methods=['POST'])
def sms():
    body = request.values.get('Body', None)

    if body is None:
      return Response(mimetype='text/plain')

    sms = body.lower()
    print sms

    rgba = tinycss2.color3.parse_color(sms)

    if rgba is None:
      return Response("Sorry, I don't recognize that color.", mimetype='text/plain')

    if len(rgba) == 4:
      red = int(round(255*rgba[0]))
      green = int(round(255*rgba[1]))
      blue = int(round(255*rgba[2]))
      rgb_string = '[{0:03d},{1:03d},{2:03d}]'.format(red, green, blue)
      payload = {'access_token': os.environ['SPARK_ACCESS_TOKEN'], 'command': rgb_string}
      r = requests.post("https://api.spark.io/v1/devices/{0}/color".format(os.environ['SPARK_CORE_ID']), data=payload)
      return Response(mimetype='text/plain')


if __name__ == '__main__':
  app.run()
