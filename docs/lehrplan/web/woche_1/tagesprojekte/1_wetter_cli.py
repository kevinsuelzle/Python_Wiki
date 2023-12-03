import requests

def get_weather_data(api_url, params):
    """Holt Wetterdaten von der API."""
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 429:
            print("Rate-Limit erreicht. Bitte später erneut versuchen.")
        else:
            print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def geocode_city(city_name):
    """Konvertiert einen Stadtnamen in geografische Koordinaten."""
    geocode_url = "https://geocode.maps.co/search"
    params = {'q': city_name}
    response = get_weather_data(geocode_url, params)
    if response:
        return response[0]['lat'], response[0]['lon']
    return None, None

def get_current_weather(city):
    """Ruft das aktuelle Wetter für eine Stadt ab."""
    lat, lon = geocode_city(city)
    if lat and lon:
        api_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': 'true'
        }
        weather_data = get_weather_data(api_url, params)
        if weather_data:
            return weather_data['current_weather']
    return None

def get_weather_forecast(city):
    """Ruft die Wettervorhersage für die nächsten 7 Tage für eine Stadt ab."""
    lat, lon = geocode_city(city)
    if lat and lon:
        api_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'daily': ['temperature_2m_max', 'temperature_2m_min', 'weathercode', 'precipitation_sum'],
            'timezone': 'auto'
        }
        weather_data = get_weather_data(api_url, params)
        if weather_data:
            return weather_data['daily']
    return None

def wmo_weather_interpretation(weather_code):
    """ Interpretiert den WMO-Wettercode in lesbare Wetterbedingungen. """
    wmo_codes = {
        0: 'Klarer Himmel',
        1: 'Hauptsächlich klar',
        2: 'Teilweise bewölkt',
        3: 'Bewölkt',
        45: 'Nebel',
        48: 'Nebel mit Reifbildung',
        51: 'Leichter Nieselregen',
        53: 'Mäßiger Nieselregen',
        55: 'Dichter Nieselregen',
        56: 'Leichter gefrierender Nieselregen',
        57: 'Dichter gefrierender Nieselregen',
        61: 'Leichter Regen',
        63: 'Mäßiger Regen',
        65: 'Starker Regen',
        66: 'Leichter gefrierender Regen',
        67: 'Starker gefrierender Regen',
        71: 'Leichter Schneefall',
        73: 'Mäßiger Schneefall',
        75: 'Starker Schneefall',
        77: 'Schneegriesel',
        80: 'Leichte Regenschauer',
        81: 'Mäßige Regenschauer',
        82: 'Starke Regenschauer',
        85: 'Leichte Schneeschauer',
        86: 'Starke Schneeschauer',
        95: 'Gewitter',
        96: 'Gewitter mit leichtem Hagel',
        99: 'Gewitter mit starkem Hagel'
    }
    return wmo_codes.get(weather_code, 'Unbekannte Bedingungen')

def get_weather_emoji(weather_condition, temperature):
    """ Gibt passende Emojis für Wetterbedingungen zurück. """
    if temperature > 25:
        temperature_emoji = "🌡️☀️"  # Warm
    elif temperature < 5:
        temperature_emoji = "🌡️❄️"  # Kalt
    else:
        temperature_emoji = "🌡️🌥️"  # Mild

    weather_emojis = {
        'Klarer Himmel': '☀️',
        'Hauptsächlich klar': '🌤️',
        'Teilweise bewölkt': '⛅',
        'Bewölkt': '☁️',
        'Nebel': '🌫️',
        'Nebel mit Reifbildung': '🌫️❄️',
        'Leichter Nieselregen': '🌦️',
        'Mäßiger Nieselregen': '🌧️',
        'Dichter Nieselregen': '🌧️',
        'Leichter gefrierender Nieselregen': '🌧️❄️',
        'Dichter gefrierender Nieselregen': '🌧️❄️',
        'Leichter Regen': '🌦️',
        'Mäßiger Regen': '🌧️',
        'Starker Regen': '🌧️☔',
        'Leichter gefrierender Regen': '🌧️❄️',
        'Starker gefrierender Regen': '🌧️❄️',
        'Leichter Schneefall': '🌨️',
        'Mäßiger Schneefall': '🌨️',
        'Starker Schneefall': '❄️',
        'Schneegriesel': '🌨️',
        'Leichte Regenschauer': '🌦️',
        'Mäßige Regenschauer': '🌧️',
        'Starke Regenschauer': '🌧️☔',
        'Leichte Schneeschauer': '🌨️',
        'Starke Schneeschauer': '❄️',
        'Gewitter': '⛈️',
        'Gewitter mit leichtem Hagel': '⛈️🌨️',
        'Gewitter mit starkem Hagel': '⛈️🧊'
    }
    weather_emoji = weather_emojis.get(weather_condition, '🌈')

    return f"{temperature_emoji} {weather_emoji}"

def print_current_weather(weather_data, city):
    """Druckt das aktuelle Wetter in einem lesbaren Format."""
    if weather_data:
        weather_condition = wmo_weather_interpretation(weather_data['weathercode'])
        emoji = get_weather_emoji(weather_condition, weather_data['temperature'])
        print(f"\nAktuelles Wetter in {city}: {emoji}")
        print(f"Temperatur: {weather_data['temperature']}°C")
        print(f"Wetterzustand: {weather_condition}")
        print(f"Niederschlag: {weather_data.get('precipitation', '0')} mm\n")
    else:
        print("Keine Wetterdaten verfügbar.")

def print_weather_forecast(weather_data, city):
    """Druckt die Wettervorhersage in einem lesbaren Format."""
    if weather_data:
        print(f"\nWettervorhersage für {city} für die nächsten 7 Tage:")
        for i, day in enumerate(weather_data['time']):
            max_temp = weather_data['temperature_2m_max'][i]
            weather_condition = wmo_weather_interpretation(weather_data['weathercode'][i])
            emoji = get_weather_emoji(weather_condition, max_temp)
            print(f"Datum: {day} {emoji}")
            print(f"Max Temperatur: {max_temp}°C")
            print(f"Min Temperatur: {weather_data['temperature_2m_min'][i]}°C")
            print(f"Wetterzustand: {weather_condition}")
            print(f"Niederschlag: {weather_data['precipitation_sum'][i]} mm\n")
    else:
        print("Keine Wetterdaten verfügbar.")

def main():
    while True:
        print("\nWetter CLI Anwendung")
        print("1. Wetter Aktuell")
        print("2. Wetter Vorhersage 7-Tage")
        print("3. Beenden")
        choice = input("Wähle eine Option: ")

        if choice == '1':
            city = input("Gib den Namen einer Stadt ein: ")
            weather_data = get_current_weather(city)
            print_current_weather(weather_data, city)
        elif choice == '2':
            city = input("Gib den Namen einer Stadt ein: ")
            weather_data = get_weather_forecast(city)
            print_weather_forecast(weather_data, city)
        elif choice == '3':
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")

if __name__ == "__main__":
    main()
