
import mysql.connector
import random
import config

db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)
cursor = db.cursor(dictionary=True)



def start_game():
    print("🌍 ECO-BUILDER: THE GREEN MACHINE MISSION 🌍")


    screen_name = input("Enter your name: ")
    print(f"\n🚀 Welcome, Captain {screen_name}!")
    print("🌍 The world is facing a lot of pollutions, our last hope is you, only you can save us.")
    print("🛠 You need to build an eco-friendly machine to refine our atmosphere.")
    print("To build that machine you need to find 5 parts and visit at least 10 NEW airports.")

    print("⚡ Remember captain, your CO2 budget is limited. So, take every step wisely!")

    CO2_budget = 10000
    current_location = 'EFHK'
    visited_airports = set()

    required_parts = ["Electric Motor", "Battery", "Air Filter", "Propeller", "Solar Panel"]
    collected_parts = []

while len(visited_airports) < 10 and CO2_budget > 0:

    cursor.execute(
        f"SELECT name, iso_country, latitude_deg, longitude_deg FROM airport WHERE ident = '{current_location}'")
    current_airport = cursor.fetchone()

    lat = current_airport['latitude_deg']
    lon = current_airport['longitude_deg']

    print(f"\n📍 Location: {current_airport['name']} ({current_airport['iso_country']})")
    print(f"💰 Budget: {CO2_budget}")
    print(f"🚩 Visited Airports: {len(visited_airports)}/10")
    print(f"🛠 Collected Parts: {len(collected_parts)}/5 - {collected_parts}")
