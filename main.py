import requests
import datetime as dt
import smtplib

MY_LAT=12.971599
MY_LNG=77.594566
# MY_LAT=30.316496
# MY_LNG=78.032188
MY_KEY="b4d419a569098ff6d14476b1a37e062e"
my_mail="subhnegipython@gmail.com"
my_password="poaxujigalppestq"
recipient_mail="subhnegipython@yahoo.com"

parameters={
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":MY_KEY,
}
response=requests.get("http://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()

data=response.json()
conditioncodes=[]

def weather():
    for i in range(8):
        weatherid=data['list'][i]['weather'][0]['id']
        conditioncodes.append(weatherid)

weather()
hour=0
for code in conditioncodes:
    if  code <=600:
        with smtplib.SMTP_SSL("smtp.gmail.com") as connect:
            connect.login(user=my_mail,password=my_password)
            connect.sendmail(from_addr=my_mail,to_addrs=recipient_mail,msg=f"Subject: rain ahead\n\n take umbrella with you, there is a chance of rain/snow in next {hour} hours")
    hour+=3
