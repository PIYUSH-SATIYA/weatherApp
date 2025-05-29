import requests
import sys

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key=f543a63e3e854d6eace164328252905&q={city}&aqi=no"

    try:
        data = requests.get(url)
        data.raise_for_status()
        return data.json()
    except requests.exceptions.HTTPError:
        if data.status_code == 400:
            sys.exit("City not found in weather data!!!") 

def main():
    city = input("Enter your city: ")
    final = get_weather(city)
    print(f"The temperature of your city is: {final["current"]["temp_c"]}")


if __name__ == "__main__":
    main()