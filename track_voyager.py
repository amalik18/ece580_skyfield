#!/usr/bin/env python
from skyfield.api import load, wgs84, EarthSatellite
from datetime import datetime
from skyfield.constants import AU_KM
from skyfield.vectorlib import VectorFunction
from spktype01 import SPKType01


# class Type01Object(VectorFunction):
#     def __init__(self, kernel, target):
#         self.kernel = kernel
#         self.center = 10
#         self.target = target

#     def _at(self, t):
#         k = self.kernel
#         print(t)
#         r, v = k.compute_type01(self.center, self.target, t.whole, t.tdb_fraction)
#         return r / AU_KM, v / AU_KM, None, None

# class TrackBody:
#     def __init__(self, lat=0.0, lon=0.0):
#         self.ts = load.timescale()        
#         self.sat = None
#         self.eph = load('de421.bsp')
#         self.earth = self.eph['earth']
#         self.sun = self.eph['sun']
#         kernel = SPKType01.open('Voyager_1.a54206u_V0.2_merged.bsp')
#         print(kernel)
#         self.body_eph = Type01Object(kernel, -31)
#         self.set_loc(lat, lon)
#         self.set_body()

#     def set_body(self):
#         self.body = self.body_eph

#     def set_loc(self, lat, lon):
#         if isinstance(lat, float) and isinstance(lon, float):
#             self.lat = lat
#             self.lon = lon
#             self.loc = self.earth+wgs84.latlon(float(lat),float(lon))
#         else:
#             raise ValueError('Lat and Lon must be floats')

#     def get_view(self, time_start, time_stop=None, points=100):
#         if isinstance(time_start, datetime):    
#             t1 = self.ts.from_datetime(time_start)
#         else:
#             raise ValueError('Time must be datetime.datetime object')
#         if time_stop != None:
#             if isinstance(time_stop, datetime):    
#                 t2 = self.ts.from_datetime(time_stop)
#             else:
#                 raise ValueError('Time must be datetime.datetime object')
            
#             ret_list = []
#             times = self.ts.linspace(t1, t2, count)
#             for t in times:
#                 topocentric = self.body.at(t) - self.loc.at(t)
#                 alt, az, distance = topocentric.altaz()
#                 ret_list.append({'time':t, 'alt':alt, 'az':az, 'distance':distance})
#             return ret_list
#         else:
#             difference = self.body - self.loc
#             topocentric = difference.at(t1)
            
#             alt, az, distance = topocentric.altaz()
#             return {'time':t1, 'alt':alt, 'az':az, 'distance':distance}
#     def filter_for_elevation(self, views, min_angle):
#         o=[]
#         for v in views:
#             if v['alt'].degrees >= min_angle:
#                 o.append(v)
#         return o
            

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

    body_track = TrackBody(float(lat), float(lon))
    views = body_track.get_view(t1,t2,count)
    filtered = body_track.filter_for_elevation(views,min_angle)
    for f in filtered: 
        print(f)

