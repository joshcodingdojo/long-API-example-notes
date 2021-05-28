from django.shortcuts import render, HttpResponse


"""
========== INTRODUCTORY NOTES FOR LONG ==========

During Web Fundamentals, you learned about calling an API using AJAX/Javascript,
where you get this data from an API on the browser.

So instead of reaching out to get API data on the browser, you will get it on 
our django server. 

To do this, you will need to install requests in your virtual environments
on command line: pip install requests

The library is very easy to use. Look at the following:

r = requests.get("[URL_STRING]")

This is the code you have to write to make an http api request. That's it!

The variable r will be the api response. But r will be equal to <Request 200> if you print it out.

That's because we have to turn this response into JSON

We do that like this:
r = r.json()

That's it!

=====

SIGNING UP FOR API AND GETTING YOUR OWN API KEY

Go to this link and follow the instructions: https://developers.google.com/civic-information/docs/using_api 

If you need help on Monday I will gladly help you sign up for it

I will send you my API KEY via mattermost message so you can play around 
and have fun before having to deal with getting your own key

!! API_DOCS !! 
Below is the main piece of documentation you will need
https://developers.google.com/civic-information/docs/v2/representatives/representativeInfoByAddress

Additional: https://developers.google.com/civic-information/docs/using_api

It can be hard on the eyes to look at json data in the terminal, 
so you can use your browser and paste the code here: 
https://jsonformatter.org/json-pretty-print and click "Make Pretty"
"""
# !!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!
# you must install requests library into your virtual environment: i.e. pip install requests
import requests
# *** !TODO: take the api key i sent you on mattermost and 
# uncomment the line below and put it inside the string ***
# API_KEY = ''
# THEN COMMENT OUT LINE BELOW!
from .secret import API_KEY
# to change the address in the api request change the string below
address = "233WLantanaRd,Lantana,FL33462"
api_url = f"https://www.googleapis.com/civicinfo/v2/representatives?key={API_KEY}&address={address}"
# API_KEY = ''


# play with API data 
# *** YOU MUST START SERVER AND GO TO URL localhost:8000 to trigger this 
def index(request):
  # this gets the api data and response is saved to variable r
  # To change the address, just change the part of 
  r = requests.get(f"https://www.googleapis.com/civicinfo/v2/representatives?key={API_KEY}&address=233WLantanaRd,Lantana,FL33462&includeOffices=true")
  print(r) 
  print("=========================================================================================")
  print("=========================================================================================")
  print("=========================================================================================")
  # This prints "<Response [200]>", so we need to turn it into json
  json = r.json()
  print(json)
  print("=========================================================================================")
  print("=========================================================================================")
  print("=========================================================================================")
  # now the json variable stores a massive python dictionary
  # the data you need is located in json['offices'] and json['officials']
  # Below is how you get access to all of the different elected offices based on user address
  for i in json['offices']:
    print(i)
  print("=========================================================================================")
  # This gives us every elected official for person's current address 
  print(len(json['officials']))
  for i in json['officials']:
    print(i)
  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT INFO BELOW !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  # You will need to "massage" the API data because if you look closely, when looping through
  # json['officials'] above, the dictionaries DO NOT contain the office each official holds
  # i.e. Senator, President, Governor, etc...

  # Go to this official google API Q and A: https://groups.google.com/g/google-civicinfo-api/c/FCQsrFgqOh4/m/ptiR80hSAQAJ
  # And look at the first couple posts on the page and it gives you a very strong hint of how to solve the problem
  # where the office of the elected official is not included in json['officials'] with their name
  # Our goal as instructors is to guide you to the promise land so you can be a self sufficient developer
  # If you need help, reach out to a TA over the weekend or myself on Monday.
  print("=========================================================================================")
  print("=========================================================================================")
  print("=========================================================================================")
  return HttpResponse('yo')


x = [1, 2, 3]
for el, idx in enumerate(x):
  print(el, idx)
