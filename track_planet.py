#!/usr/bin/env python
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
            times = self.ts.linspace(t1, t2, count)
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
            

if __name__ == '__main__':
    from sys import argv
    from datetime import datetime, timezone

    print(argv)
    t2=0
    count=10
    min_angle=None
    planet = 'mars'
    if len(argv)>1:
        print("Planet: %s"%argv[1])
        planet = argv[1]
    if len(argv)>2:
        print("Loc: %s"%argv[2])
        lat,lon = argv[2].split(',')
    if len(argv)>3:
        print("Time: %s"%argv[3])
        t1 = datetime.strptime(argv[3], '%Y/%m/%d-%H:%M:%S')
        t1 = t1.replace(tzinfo=timezone.utc)
    if len(argv)>4:
        print("Time 2: %s"%argv[4])
        t2 = datetime.strptime(argv[4], '%Y/%m/%d-%H:%M:%S')
        t2 = t2.replace(tzinfo=timezone.utc)
    if len(argv)>5:
        print("Points: %s"%argv[5])
        count = int(argv[5])
    if len(argv)>6:
        print("Min Angle: %s"%argv[6])
        min_angle = int(argv[6])

    planet_track = TrackPlanet(float(lat), float(lon), planet)
    views = planet_track.get_view(t1,t2,count)
    filtered = planet_track.filter_for_elevation(views,min_angle)
    for f in filtered: 
        print(f)

