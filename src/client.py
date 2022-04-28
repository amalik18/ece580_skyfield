from skyfield.api import load, wgs84, EarthSatellite
from datetime import datetime

class TrackPlanet:
    def __init__(self, lat=0.0, lon=0.0, planet=None):
        self.ts = load.timescale()        
        self.sat = None
        self.eph = load('de421.bsp')
        self.earth = self.eph['earth']
        self.set_loc(lat, lon)
        if planet != None:
            self.set_planet(planet)

    def set_planet(self, name):
        self.planet = self.eph[name]

    def set_loc(self, lat, lon):
        if isinstance(lat, float) and isinstance(lon, float):
            self.lat = lat
            self.lon = lon
            self.loc = self.earth+wgs84.latlon(float(lat),float(lon))
        else:
            raise ValueError('Lat and Lon must be floats')

    def get_view(self, time_start, time_stop=None, points=100):
        if isinstance(time_start, datetime):    
            t1 = self.ts.from_datetime(time_start)
        else:
            raise ValueError('Time must be datetime.datetime object')
        if time_stop != None:
            if isinstance(time_stop, datetime):    
                t2 = self.ts.from_datetime(time_stop)
            else:
                raise ValueError('Time must be datetime.datetime object')
            
            ret_list = []
            times = self.ts.linspace(t1, t2, points)
            for t in times:
                difference = self.planet - self.loc
                topocentric = difference.at(t)
                alt, az, distance = topocentric.altaz()
                ret_list.append({'time':t, 'alt':alt, 'az':az, 'distance':distance})
            return ret_list
        else:
            difference = self.planet - self.loc
            topocentric = difference.at(t1)
            
            alt, az, distance = topocentric.altaz()
            return {'time':t1, 'alt':alt, 'az':az, 'distance':distance}
    def filter_for_elevation(self, views, min_angle):
        o=[]
        for v in views:
            if v['alt'].degrees >= min_angle:
                o.append(v)
        return o



class TrackSatellite:
    def __init__(self, lat=0.0, lon=0.0, tle=None):
        self.ts = load.timescale()
        self.set_loc(lat, lon)
        if tle != None:
            self.load_tle(tle)
        else:
            self.sat = None

    def load_tle(self, tle, name='satellite'):
        
        if isinstance(tle, list) and len(tle) == 2:
            self.sat = EarthSatellite(tle[0], tle[1], name, self.ts)
        else:
            raise ValueError('TLE data must be a list of two strings')

    def set_loc(self, lat, lon):
        if isinstance(lat, float) and isinstance(lon, float):
            self.lat = lat
            self.lon = lon
            self.loc = wgs84.latlon(float(lat),float(lon))
        else:
            raise ValueError('Lat and Lon must be floats')

    def get_view(self, time_start, time_stop=None, points=100):
        if isinstance(time_start, datetime):    
            t1 = self.ts.from_datetime(time_start)
        else:
            raise ValueError('Time must be datetime.datetime object')
        if time_stop != None:
            if isinstance(time_stop, datetime):    
                t2 = self.ts.from_datetime(time_stop)
            else:
                raise ValueError('Time must be datetime.datetime object')
            
            ret_list = []
            times = self.ts.linspace(t1, t2, count)
            for t in times:
                difference = self.sat - self.loc
                topocentric = difference.at(t)
                alt, az, distance = topocentric.altaz()
                ret_list.append({'time':t, 'alt':alt, 'az':az, 'distance':distance})
            return ret_list
        else:
            difference = self.sat - self.loc
            topocentric = difference.at(t1)
            
            alt, az, distance = topocentric.altaz()
            return {'time':t1, 'alt':alt, 'az':az, 'distance':distance}
    def filter_for_elevation(self, views, min_angle):
        o=[]
        for v in views:
            if v['alt'].degrees >= min_angle:
                o.append(v)
        return o