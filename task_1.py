import os
import json
import random
import time
import numpy as np
import heapq
from collections import defaultdict
from datetime import datetime, timedelta


def random_date():
    return (datetime.today() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")


def generate_flight():
    null_prob = random.uniform(0.001, 0.005)
    return {
        "date": random_date() if random.random() > null_prob else None,
        "origin_city": random.choice(CITIES) if random.random() > null_prob else None,
        "destination_city": random.choice(CITIES) if random.random() > null_prob else None,
        "flight_duration_secs": random.randint(1800, 54000) if random.random() > null_prob else None,
        "passengers": random.randint(1, 400) if random.random() > null_prob else None
    }


def generate_files():
    os.makedirs(TMP_DIR, exist_ok=True)
    for _ in range(TOTAL_FILES):
        origin = random.choice(CITIES)
        month_year = datetime.today().strftime("%m-%y")
        file_path = os.path.join(TMP_DIR, f"{month_year}-{origin}-flights.json")
        flights = [generate_flight() for _ in range(random.randint(50, 100))]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(flights, f, indent=2, ensure_ascii=False)


def analyze_files():
    start_time = time.time()
    total_records, dirty_records = 0, 0
    duration_data, passenger_inflow, passenger_outflow = defaultdict(list), defaultdict(int), defaultdict(int)

    for filename in os.listdir(TMP_DIR):
        with open(os.path.join(TMP_DIR, filename), 'r') as f:
            flights = json.load(f)
            total_records += len(flights)
            for flight in flights:
                if None in flight.values():
                    dirty_records += 1
                if flight["destination_city"] and flight["flight_duration_secs"]:
                    duration_data[flight["destination_city"]].append(flight["flight_duration_secs"])
                if flight["origin_city"] and flight["passengers"]:
                    passenger_outflow[flight["origin_city"]] += flight["passengers"]
                if flight["destination_city"] and flight["passengers"]:
                    passenger_inflow[flight["destination_city"]] += flight["passengers"]

    top_25_cities = heapq.nlargest(25, duration_data, key=lambda x: len(duration_data[x]))
    stats = {}
    for city in top_25_cities:
        if duration_data[city]:
            stats[city] = {
                "AVG": np.mean(duration_data[city]),
                "P95": np.percentile(duration_data[city], 95)
            }

    max_arrival_city = max(passenger_inflow, key=passenger_inflow.get, default="No data")
    max_departure_city = max(passenger_outflow, key=passenger_outflow.get, default="No data")

    print("Total Records Processed:", total_records)
    print("Dirty Records:", dirty_records)
    print("Total Run Duration:", time.time() - start_time, "seconds")
    print("Top 25 Destination Cities (AVG & P95 Flight Duration):", stats)
    print("City with Max Passengers Arrived:", max_arrival_city)
    print("City with Max Passengers Departed:", max_departure_city)


if __name__ == "__main__":
    TMP_DIR = "/flights"
    CITY_COUNT = random.randint(100, 200)
    TOTAL_FILES = 5000
    CITIES = [f"City_{i}" for i in range(CITY_COUNT)]
    generate_files()
    analyze_files()
