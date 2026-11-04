import os
import requests
from io import StringIO
import pandas as pd
import httpx
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(ROOT_DIR/".env")
MAP_KEY = os.getenv("MAP_KEY")

BASE_URL = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv"


async def get_hotspot(source="VIIRS_SNPP_NRT", area="94.0,-11.0,141.0,6.0", day_range=1)-> pd.DataFrame:
    if not MAP_KEY:
        raise ValueError("cannot get hotspot area")

    if not 1 <= day_range <= 5:
        raise ValueError("day_range harus antara 1 sampai 5")

    url = (f"{BASE_URL}/{MAP_KEY}/{source}/{area}/{day_range}")

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
    data = pd.read_csv(StringIO(response.text))
    location_hotspot = data[["latitude", "longitude"]]

    return location_hotspot
