#!/usr/bin/env python
from skyfield.api import load, wgs84, EarthSatellite
from datetime import datetime

class TrackSatellite:
    def __init__(self, lat=0.0, lon=0.0):
        self.ts = load.timescale()        
        if isinstance(lat, float) and isinstance(lon, float):
            self.lat = lat
            self.lon = lon
            self.loc = wgs84.latlon(float(lat),float(lon))
        else:
            raise ValueError('Lat and Lon must be floats')
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
            

if __name__ == '__main__':
    from sys import argv
    from datetime import datetime, timezone

    print(argv)
    t2=0
    count=10
    min_angle=None
    if len(argv)>1:
        print("Loc: %s"%argv[1])
        lat,lon = argv[1].split(',')
    if len(argv)>2:
        print("Time: %s"%argv[2])
        t1 = datetime.strptime(argv[2], '%Y/%m/%d-%H:%M:%S')
        t1 = t1.replace(tzinfo=timezone.utc)
    if len(argv)>3:
        print("Time 2: %s"%argv[3])
        t2 = datetime.strptime(argv[3], '%Y/%m/%d-%H:%M:%S')
        t2 = t2.replace(tzinfo=timezone.utc)
    if len(argv)>4:
        print("Points: %s"%argv[4])
        count = int(argv[4])
    if len(argv)>5:
        print("Min Angle: %s"%argv[5])
        min_angle = int(argv[5])
    line1 = "1 25544U 98067A   22101.34838098  .00010998  00000+0  20034-3 0  9997"
    line2 = "2 25544  51.6440 307.6369 0004493  11.0035 156.2993 15.50005149334810"


    sat_track = TrackSatellite(float(lat), float(lon))
    sat_track.set_loc(float(lat), float(lon))
    sat_track.load_tle([line1,line2])
    views = sat_track.get_view(t1,t2,count)
    filtered = sat_track.filter_for_elevation(views,min_angle)
    for f in filtered: 
        print(f)

