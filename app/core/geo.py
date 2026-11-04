import numpy as np
import logging
logger = logging.getLogger(__name__)

def haversine(point1:tuple, point2:tuple) -> float:
    lat1, lon1  = point1
    lat2, lon2  = point2
    sigma = np.pi/180.0

    #convert degree to radiant
    d_lat = (lat2-lat1)*sigma
    d_lon = (lon2-lon1)*sigma

    lat1 = lat1*sigma
    lat2 = lat2*sigma

    formula = (np.power(np.sin(d_lat/2),2)+np.power(np.sin(d_lon/2),2)*np.cos(lat1)*np.cos(lat2))

    r = 6371
    c = 2*np.arcsin(np.sqrt(formula))
    return r*c
