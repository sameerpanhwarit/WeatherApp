import re
from urllib import response
import requests
from time import sleep
import os

#paste your api key here
api_key='d50190e5106c4c54ae8171225222310'

def menu():
    os.system('cls')
    print("-"*10,"Weather App","-"*10)
    menu = ['1.Weather Updates of Your City','2.Weather Updates of Another City/Country','3.Exit']
    for i in menu:
        print(i)
    print('-'*33)
    option = int(input("Enter Option: "))
    if option == 1:
        checkMyCity()
    elif option == 2:
        checkCity()
    elif option ==3:
        exit
    else:
        print("invalid Input")

def checkMyCity():
    os.system('cls')
    myip = requests.get('https://api.ipify.org').text 
    r = requests.get(f'https://ipapi.co/{myip}/json/').json()
    city = r.get('city')
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes")
    jsonData=response.json()
    data ={
        "City": jsonData['location']['name'],
        "Region":jsonData['location']['region'],
        "Country":jsonData['location']['country'],
        "latitude":jsonData['location']['lat'],
        "Longitude":jsonData['location']['lon'],
        "Local Time":jsonData['location']['localtime'],
        "Last Updated":jsonData['current']['last_updated'],
        "Temprature in Celsius":jsonData['current']['temp_c'],
        "Temprature in Fahrenheit":jsonData['current']['temp_f'],
        "Wind Miles/hour":jsonData['current']['wind_mph'],
        "Wind kph": jsonData['current']['wind_kph'],
        "Wind Direction":jsonData['current']['wind_dir'],
        "Humidity":jsonData['current']['humidity'],
        "Cloud":jsonData['current']['cloud'],
        "FeelsLike Celsius":jsonData['current']['feelslike_c'],
        "FeelsLike Fahrenheit":jsonData['current']['feelslike_f']
    }
    print('-'*10,"Weather Details",'-'*10)
    for key, value in data.items():
        print(key," : ",value )
    print('-'*37)
    option = input("Want back to Menu? y/n: ")
    if 'y' in option:
        menu()
    else:
        exit

def checkCity():
    os.system('cls')
    print('-'*10,"Weather Details",'-'*10)
    city = input("Enter City ot Country: ")
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes")
    jsonData=response.json()
    data ={
        "City": jsonData['location']['name'],
        "Region":jsonData['location']['region'],
        "Country":jsonData['location']['country'],
        "latitude":jsonData['location']['lat'],
        "Longitude":jsonData['location']['lon'],
        "Local Time":jsonData['location']['localtime'],
        "Last Updated":jsonData['current']['last_updated'],
        "Temprature in Celsius":jsonData['current']['temp_c'],
        "Temprature in Fahrenheit":jsonData['current']['temp_f'],
        "Wind Miles/hour":jsonData['current']['wind_mph'],
        "Wind kph": jsonData['current']['wind_kph'],
        "Wind Direction":jsonData['current']['wind_dir'],
        "Humidity":jsonData['current']['humidity'],
        "Cloud":jsonData['current']['cloud'],
        "FeelsLike Celsius":jsonData['current']['feelslike_c'],
        "FeelsLike Fahrenheit":jsonData['current']['feelslike_f']
    }
    os.system('cls')
    print('-'*10,"Weather Details",'-'*10)
    for key, value in data.items():
        print(key," : ",value )
    print('-'*37)
    option = input("Want back to Menu? y/n: ")
    if 'y' in option:
        menu()
    else:
        exit

menu()