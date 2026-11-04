from fastapi import APIRouter
from app.integrations.nasa_firms import get_hotspot
from app.core.geo import haversine
import logging
logger = logging.getLogger(__name__)

routers = APIRouter()

# Endpoint menerima parameter lat dan lon dari URL
@routers.get("/hotspots")
async def get_filtered_hotspots(lat: float, lon: float, radius_km: float = 50):
    data_nasa = await get_hotspot()
    if data_nasa.empty:
        logger.info("dataframe is empty, get data from 2 days before")
        data_nasa = await get_hotspot(day_range=2)
    data_lat = data_nasa["latitude"].values
    data_lon = data_nasa["longitude"].values

    logger.info("calculate distacne using haversine")
    distance  = haversine((data_lat, data_lon), (lat, lon))
    data_nasa["distance"] = distance

    logger.info("looking for hotspot undet 50 km")
    data_nasa = data_nasa[data_nasa["distance"]<=radius_km]


    lat_hotspot = data_nasa["latitude"].values.tolist()
    lon_hotspot = data_nasa["longitude"].values.tolist()
    
    return {"latitude":lat_hotspot, "longitude":lon_hotspot}