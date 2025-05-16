# temps.py
import requests
import json
from datetime import datetime

# Coordenades de la ciutat (exemple: Barcelona)
latitude = 41.3888
longitude = 2.159

# Consulta a l’API d’Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    f"&hourly=temperature_2m&timezone=Europe%2FMadrid"
)

response = requests.get(url)
data = response.json()

# Obtenir les temperatures horàries
temperatures = data['hourly']['temperature_2m']

# Càlculs
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

# Crear JSON
today = datetime.now().strftime('%Y%m%d')
filename = f"temp_{today}.json"

with open(filename, 'w') as f:
    json.dump({
        "data": today,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "avg_temp": round(avg_temp, 2)
    }, f, indent=4)

print(f"Dades guardades a {filename}")
