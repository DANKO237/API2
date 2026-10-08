
import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
     "latitude": 11.5167,"longitude": 3.8667, 
     "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}
try:
     response = requests.get(url,params=params, timeout = 5) 
     print(response.status_code)
     print(response.url)
     response.raise_for_status()
     data = response.json()
     heure = data["current"]["time"]
     temperature = data["current"] ["temperature_2m"]
     humidite = data["current"] ["relative_humidity_2m"]
     vitesse_du_vent = data["current"]["wind_speed_10m"]
     print("===============================")
     print("         METEO YAOUNDE")
     print("================================")
     print("heure:", heure)
     print("temperature:",temperature,"C")
     print("humidite:", humidite,"%")
     print("vitesse_du_vent", vitesse_du_vent, "km/h")
     print("=================================")
except requests.Timeout:
        print("le serveur met trop de temps a repondre")
except requests.RequestException as erreur:
    print("Erreur reseau HTTP:", erreur)