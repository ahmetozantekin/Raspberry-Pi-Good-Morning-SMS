Raspberry Pi Good Morning SMS
=============================

An automated SMS sent every morning with Bitcoin prices, weather forecast, clothing recommendations, and more.

<img src="http://chaseacton.com/cdn/SMS.png" width=400px>

Overview
-----------------------------

Raspberry Pi Good Morning SMS uses Python and various REST APIs to obtain Bitcoin prices, weather information, make clothing reccomendations, and then text me all of the information at 7:00 AM each morning before I start my day.

Requirements
-----------------------------
For this setup, you will need:
+   An always-on, internet-connected computer capable of running a Python cron job. I found a Raspberry Pi to be the perfect fit for this.
+   Twilio, or another web-based SMS provider. It's possible to use email to send the messages through your carrier's SMS gateway, but Twilio is simple and very cheap.
