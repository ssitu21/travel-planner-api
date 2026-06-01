"""
Requests  module providng APIS
I will be using it to access country information data, weather information and currency exchange 
"""
import requests

# Ask the user for the country name
country = input("Enter the country name:").strip()

# Generate the URL
URL = f"https://restcountries.com/v3.1/name/{country}"  

# Use Requests to get data from the URL back in JSON format
# JSON = javascript object notation (you can also use XML but I prefer JSON)
jsondata = requests.get(URL).json()

# Get the country returned
data = jsondata[0]

# Use brackets just like in lists and dictionaries to get the exact data the user needs
country_name = data["name"]["common"]
capital = data["capital"][0]
population = data["population"]
region = data["region"]
currency = list(data["currencies"].keys())[0]
language = list(data["languages"].values())[0]

# Print the information
print("Country Information: ")
print()
print(f"Country:    {country_name}")
print(f"Capital:    {capital}")
print(f"Population: {population:,}")
print(f"Region:     {region}")
print(f"Currency:   {currency}")
print(f"Language:   {language}")
