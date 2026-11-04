from app.integrations.nasa_firms import get_hotspot
import pytest
import pandas as pd

@pytest.mark.asyncio
async def test_get_hotspot():
    data  = await get_hotspot()
    assert isinstance(data, pd.DataFrame)

