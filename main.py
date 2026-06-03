"""
Requests  module providng APIS
I will be using it to access country information data, weather information and currency exchange 
"""
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()  # hides main window so it doesn't look messy

while True:

    # Ask the user for the country name
    country = simpledialog.askstring("Input", "Enter the country name:").strip()
    print()

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
    print()
    
    messagebox.showinfo("Country Info",
        f"Country: {country_name}\nCapital: {capital}\nPopulation: {population}\nRegion: {region}\nCurrency: {currency}\nLanguage: {language}"
    )

###############################################################################################################################

    # Currency exchange API

    # Ask user for currency information
    from_currency = simpledialog.askstring("Input", "Enter from currency:").upper().strip()
    to_currency = simpledialog.askstring("Input", "Enter to currency:").upper().strip()
    amount = float(simpledialog.askstring("Input", "Enter amount:"))
    print()

    # Enter your API key here (if needed )
    API_KEY = "122a76de7e1339ad9a91fb11"

    # Generate the URL you will be requesting (read the documentation on the API site)
    URL = f"https://v6.exchangerate-api.com/v6/122a76de7e1339ad9a91fb11/latest/{from_currency}"

    # Use Requests to get data from the URL back in JSON format
    # JSON = javascript object notation (you can also use XML but I prefer JSON)
    json_data = requests.get(URL, timeout=10).json()

    # Use brackets just like in lists and dictionaries to get the exact data you need
    # Use a JSON viewer like https:/ho/codebeautify.org/jsonviewer to read your JSON
    rate = json_data['conversion_rates'][to_currency]

    # Convert currency
    converted = amount * rate

    # Print the conversion
    print("Currency Exchange")
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
    print()

    messagebox.showinfo("Currency Exchange",
        f"{amount} {from_currency} = {converted:.2f} {to_currency}"
    )

###############################################################################################################################

# Weather API

# Ask user for the city name
    city = simpledialog.askstring("Input", "Enter the city name:").lower().strip()
    print()


    # API key

    API_KEY = "8841958517f8b11252ed847ec9994f78"

    # Generate the URL you will be requesting (read the documentation on the API site)

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Use Requests to get data from the URL back in JSON format
    # JSON = javascript object notation (you can also use XML but I prefer JSON)
    json_data = requests.get(URL, timeout=10).json()

    # Use brackets just like in lists and dictionaries to get the exact data you need
    # Use a JSON viewer like https://codebeautify.org/jsonviewer to read your JSON
    forecast = json_data['weather'][0]['description']
    windspeed = json_data['wind']['speed']
    temp = json_data['main']['temp']
    temp_min = json_data['main']['temp_min']
    temp_max = json_data['main']['temp_max']
    humidity = json_data['main']['humidity']
    feels_like = json_data['main']['feels_like']

    # Round it  to keleus to celsius

    temp_c = round(temp - 273.15, 1)
    feels_like_c = round(feels_like - 273.15, 1)


    # Prints the weather 
    print("Today the forecast is: " + forecast)
    print(f"The Wind Speed is {windspeed}km/h")
    print(f"It feels like: {feels_like_c}" + chr(176) + "C")
    print(f"The temperature is: {temp_c}" + chr(176) + "C")
    print(f"The minimum temperature is: {round(temp_min - 273.15, 1)}" + chr(176) + "C")
    print(f"The maximum temperature is: {round(temp_max - 273.15, 1)}" + chr(176) + "C")
    print(f"The humidity is: {humidity}%")
    
    print()

    messagebox.showinfo("Weather",
        f"{forecast}\nTemp: {temp_c}°C\nFeels like: {feels_like_c}°C\nHumidity: {humidity}%"
    )

    # Loop
    
    loop = simpledialog.askstring("Continue", "Do you want to run it again (Y/N):").lower().strip()

    if loop != "y":
        messagebox.showinfo("Goodbye", "Goodbye!")
        break