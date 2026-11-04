import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.route import hotspots
import pandas as pd

app = FastAPI()
app.include_router(hotspots.routers)
client = TestClient(app)

def test_endpoint_mock(mocker):
    df_mock = pd.DataFrame({"latitude": [-2.2], "longitude": [113.9]})

    mocker.patch("app.route.hotspots.get_hotspot", return_value=df_mock)

    response = client.get("/hotspots?lat=-2.2&lon=113&radius_km=150")

    assert response.status_code == 200
    assert response.json() == {"latitude": [-2.2], "longitude": [113.9]}