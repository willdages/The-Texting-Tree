The Texting Tree
================

This is a small Python application for controlling an internet-connected Christmas Tree. It receives an incoming SMS from Twilio, parses the color in the body of the message, and hits the Spark Core's API to deliver an RGB value. The Spark Core then changes the color of a strand of lights on a Christmas Tree. Note that this repo doesn't do anything by itself. You will need a registered [Spark Core](http://www.spark.io) with the right firmware, hooked up to a strand of RGB LEDs as documented in this tutorial: [The Texting Tree](http://willd.me/posts/the-texting-tree)

There are 2 methods for a quick setup (as opposed to the very detailed instructions in the full tutorial). The original quick setup listed the manual steps below to get up and running. The new quick setup employs the Heroku Button for an even easier deployment. That cut out 7 steps! Those steps are all listed below if the button doesn't work for you, or you'd like to set it up yourself.

## Easy Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

You can use the Heroku button above to quickly deploy this application!

## Manual Deployment with Heroku

The following steps are not necessary if you are using the Heroku Button to deploy the application. These manual steps assume that you have the [Heroku Toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python) installed and that you're logged in.

1. Clone this repo and `$ cd` into the directory
2. Initialize Heroku by running `$ heroku create`
3. Copy the `.env-sample` file and rename the new file to `.env`. Fill in your Spark tokens and save the file.
4. Install a plugin to sync these environment variables with Heroku: `$ heroku plugins:install git://github.com/ddollar/heroku-config.git`
5. Sync your credentials by running `$ heroku config:push`
6. Deploy the code to Heroku `$ git push heroku master`
7. When that finishes, open the application to make sure it's running. `$ heroku open` will open your application in the web browser -- you should see the text *Merry Christmas*.
8. Set `[your-app-url]/sms` as the Messaging Request URL in Twilio (click on your number from the Twilio dashboard, or go to Numbers > Twilio Numbers > [Your Number])
