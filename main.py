"""
Requests  module providng APIS
I will be using it to access country information data, weather information and currency exchange 
"""
import requests

# Ask the user for the country name
country = input("Enter the country name:").strip()

# Generate the URL
URL = f"https://restcountries.com/v3.1/name/{country}?fullText=true"  

# Use Requests to get data from the URL back in JSON format
# JSON = javascript object notation (you can also use XML but I prefer JSON)
jsondata = requests.get(URL).json()

# Get the country returned
data = jsondata[0]

