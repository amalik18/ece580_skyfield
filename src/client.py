from skyfield.api import load, wgs84, EarthSatellite
from datetime import datetime
from skyfield.constants import AU_KM
from skyfield.vectorlib import VectorFunction
from spktype01 import SPKType01
from spktype21 import SPKType21


class TrackPlanet:
    def __init__(self, lat=0.0, lon=0.0, planet=None):
        self.ts = load.timescale()
        self.eph = load('data/de421.bsp')
        self.earth = self.eph['earth']
        self.planet = None
        if planet is not None:
            self.planet = self.eph[planet]
        self.lon = lon
        self.lat = lat
        self.loc = self.earth + wgs84.latlon(latitude_degrees=lat, longitude_degrees=lon)
        self.sat = None

    def get_view(self, time_start, time_stop=None, points=100):
        if isinstance(time_start, datetime):
            t1 = self.ts.from_datetime(time_start)
        else:
            raise ValueError('Time must be datetime.datetime object')
        if time_stop is not None:
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
                ret_list.append({'time': t, 'alt': alt, 'az': az, 'distance': distance})
            return ret_list
        else:
            difference = self.planet - self.loc
            topocentric = difference.at(t1)

            alt, az, distance = topocentric.altaz()
            return {'time': t1, 'alt': alt, 'az': az, 'distance': distance}


class TrackSatellite:
    def __init__(self, lat=0.0, lon=0.0, tle=None, url=False, id=None):
        self.lon = lon
        self.lat = lat
        self.loc = wgs84.latlon(latitude_degrees=lat, longitude_degrees=lon)
        self.ts = load.timescale()

        url_link = f'https://celestrak.com/satcat/tle.php?CATNR={id}'
        filename = f'data/tle-CANTR-{id}.txt'
        self.sat = load.tle_file(url=url_link, filename=filename, reload=True)[0]

    def get_view(self, time_start, time_stop=None, points=100):
        t1 = self.ts.from_datetime(datetime=time_start)

        if time_stop is not None:
            t2 = self.ts.from_datetime(datetime=time_stop)
            ret_list = []
            times = self.ts.linspace(t0=t1, t1=t2, num=points)
            for t in times:
                difference = self.sat - self.loc
                topocentric = difference.at(t=t)
                alt, az, distance = topocentric.altaz()
                ret_list.append({'time': t, 'alt': alt, 'az': az, 'distance': distance})
            return ret_list
        else:
            difference = self.sat - self.loc
            topocentric = difference.at(t=t1)

            alt, az, distance = topocentric.altaz()
            return {'time': t1, 'alt': alt, 'az': az, 'distance': distance}


class EphemeralClass(VectorFunction):
    def __init__(self, kernel, target, type_obj):
        self.kernel = kernel
        self.target = target

        if type_obj == "type01":
            self.center = 10
        else:
            self.center = 0

    def _at(self, t):
        if self.center == 10:
            r, v = self.kernel.compute_type01(self.center, self.target, t.whole, t.tdb_fraction)
        else:
            r, v = self.kernel.compute_type21(0, self.target, t.whole, t.tdb_fraction)

        return r / AU_KM, v / AU_KM, None, None


class TrackBodyT21:
    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon
        self.ts = load.timescale()
        self.eph = load('data/de421.bsp')
        self.earth = self.eph['earth']
        kernel = SPKType21.open('data/2065803.bsp')
        self.body_eph = EphemeralClass(kernel=kernel, target=2065803, type_obj="type21")

        self.loc = self.earth + wgs84.latlon(latitude_degrees=lat, longitude_degrees=lon)
        self.sat = None

    def get_view(self, time_start, time_stop=None, points=100):
        t1 = self.ts.from_datetime(datetime=time_start)
        if time_stop is not None:
            t2 = self.ts.from_datetime(datetime=time_stop)
            ret_list = []
            times = self.ts.linspace(t0=t1, t1=t2, num=points)
            for t in times:
                topocentric = self.body_eph.at(t=t) - self.loc.at(t=t)
                alt, az, distance = topocentric.altaz()
                ret_list.append({'time': t, 'alt': alt, 'az': az, 'distance': distance})
            return ret_list
        else:
            difference = self.body_eph - self.loc
            topocentric = difference.at(t=t1)

            alt, az, distance = topocentric.altaz()
            return {'time': t1, 'alt': alt, 'az': az, 'distance': distance}


class TrackBodyT01:
    def __init__(self, lat=0.0, lon=0.0):
        self.lat = lat
        self.lon = lon
        self.ts = load.timescale()
        self.eph = load('data/de421.bsp')
        self.earth = self.eph['earth']
        self.sun = self.eph['sun']
        kernel = SPKType01.open('data/Voyager_1.a54206u_V0.2_merged.bsp')
        self.body_eph = EphemeralClass(kernel=kernel, target=-31, type_obj="type01")
        self.sat = None
        self.loc = self.earth + wgs84.latlon(latitude_degrees=self.lat, longitude_degrees=self.lon)

    def get_view(self, time_start, time_stop=None, points=100):
        t1 = self.ts.from_datetime(datetime=time_start)
        if time_stop is not None:
            t2 = self.ts.from_datetime(datetime=time_stop)
            ret_list = []
            times = self.ts.linspace(t1, t2, points)
            for t in times:
                topocentric = self.body_eph.at(t) - self.loc.at(t)
                alt, az, distance = topocentric.altaz()
                ret_list.append({'time': t, 'alt': alt, 'az': az, 'distance': distance})
            return ret_list
        else:
            difference = self.body_eph - self.loc
            topocentric = difference.at(t1)

            alt, az, distance = topocentric.altaz()
            return {'time': t1, 'alt': alt, 'az': az, 'distance': distance}
