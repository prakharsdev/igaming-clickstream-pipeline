from fastapi import FastAPI
from mimesis import Person, Generic
from random import choice, randint
from datetime import datetime, timedelta
import pandas as pd
import os

app = FastAPI()
generic = Generic('en')
person = Person('en')

# Static config
games = ["blackjack", "poker", "slots", "roulette", "baccarat"]
event_types = ["game_start", "bet_placed", "bet_result", "game_end"]
devices = ["mobile", "desktop", "tablet"]
countries = ["EE", "FI", "SE", "LV", "LT"]
output_dir = "generated_clickstreams"

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

def generate_click_event(user_id):
    event_type = choice(event_types)
    game_name = choice(games)
    bet_amount = randint(10, 200) if event_type == "bet_placed" else 0
    win_amount = randint(0, bet_amount * 2) if event_type == "bet_result" else 0
    timestamp = datetime.now() - timedelta(seconds=randint(0, 86400))

    return {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": user_id,
        "event_type": event_type,
        "game_name": game_name,
        "bet_amount": bet_amount,
        "win_amount": win_amount,
        "device": choice(devices),
        "country": choice(countries)
    }

@app.get("/generate")
def generate_data(records: int = 500):
    data = [generate_click_event(person.identifier()) for _ in range(records)]
    df = pd.DataFrame(data)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"clickstream_{timestamp}.csv"
    file_path = os.path.join(output_dir, file_name)
    df.to_csv(file_path, index=False)

    return {"message": "Data generated", "file_path": file_path}
