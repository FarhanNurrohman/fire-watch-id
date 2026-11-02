import pytest
from app.core.geo import haversine

def test_geo():
    actual_disatance = 661
    messure_distance = haversine((-6.1751, 106.8272), (-7.2458, 112.7378))
    assert actual_disatance == pytest.approx(messure_distance, abs=5)