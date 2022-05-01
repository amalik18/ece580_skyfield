from datetime import datetime, timezone
from client import TrackPlanet, TrackSatellite, TrackBodyT01, TrackBodyT21
import click


def print_views(views):
    for v in views:
        print("Time: %s Azimuth: %f Altitude: %f"%(v['time'].utc_iso(), v['az'].degrees, v['alt'].degrees))

def validate_time(ctx, param, value):
    return value


def validate_planet(ctx, param, value):
    if value.lower() not in ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'neptune', 'uranus', "pluto", "moon"]:
        raise click.BadParameter(f"The planet provided ({value}) is not a valid planet. Please provide a valid planet.")
    else:
        return value


@click.command('track_planet', short_help="Function to track planetary changes relative to a provided location.")
@click.option('--planet', required=True, type=str, default='mars', show_default=True, callback=validate_planet,
              help="Planet to track.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True,
              help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True,
              help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True,
              help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True,
              help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True,
              help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_planet_track(planet, latitude, longitude, initial_time, end_time, points, angle):
    print(
        f'Planet: {planet}\nInitial Time: {initial_time}\nEnd Time: {end_time}\n(Lat, Lon): ({latitude}, {longitude})\nPoints: {points}\nAngle: {angle}')
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    planet_client = TrackPlanet(lat=latitude, lon=longitude, planet=planet)
    planet_views = planet_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = filter_for_elevation(planet_views, angle)
    print_views(filtered_view)


@click.command('track_sat', short_help="Function to track a satellite path relative to provided location.")
@click.option('--norad_id', '--id', default=25544, type=int, show_default=True,
              help="The NORAD ID of the Satellite you'd like to track. By default it'll track the ISS (ZARYA)")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True,
              help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True,
              help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True,
              help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True,
              help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True,
              help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_sat_track(norad_id, latitude, longitude, initial_time, end_time, points, angle):
    print(
        f'NORAD ID: {norad_id}\nInitial Time: {initial_time}\nEnd Time: {end_time}\n(Lat, Lon): ({latitude}, {longitude})\nPoints: {points}\nAngle: {angle}')
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    # if not norad_id:
    #     line1 = "1 25544U 98067A   22101.34838098  .00010998  00000+0  20034-3 0  9997"
    #     line2 = "2 25544  51.6440 307.6369 0004493  11.0035 156.2993 15.50005149334810"
    #     sat_client = TrackSatellite(lat=latitude, lon=longitude, tle=[line1, line2])
    # else:
    sat_client = TrackSatellite(lat=latitude, lon=longitude, url=True, id=norad_id)
    sat_views = sat_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = filter_for_elevation(sat_views, min_angle=angle)
    print_views(filtered_view)


@click.command('track_voyager', short_help="Function to track the Voyager 1 space probe.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True,
              help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True,
              help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True,
              help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True,
              help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True,
              help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_voyager_track(latitude, longitude, initial_time, end_time, points, angle):
    print(
        f'Body: Voyager 1\nInitial Time: {initial_time}\nEnd Time: {end_time}\n(Lat, Lon): ({latitude}, {longitude})\nPoints: {points}\nAngle: {angle}')
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    voyager_client = TrackBodyT01(lat=latitude, lon=longitude)
    voyager_view = voyager_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = filter_for_elevation(views=voyager_view, min_angle=angle)
    print_views(filtered_view)


@click.command('track_asteroid', short_help="Function to track the orbit of the Didymos asteroid.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True,
              help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True,
              help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True,
              help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True,
              help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS",
              callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True,
              help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_asteroid_track(latitude, longitude, initial_time, end_time, points, angle):
    print(
        f'Body: 65803 Didymos\nInitial Time: {initial_time}\nEnd Time: {end_time}\n(Lat, Lon): ({latitude}, {longitude})\nPoints: {points}\nAngle: {angle}')
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    asteroid_client = TrackBodyT21(lat=latitude, lon=longitude)
    asteroid_view = asteroid_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = filter_for_elevation(views=asteroid_view, min_angle=angle)
    print_views(filtered_view)


def filter_for_elevation(views, min_angle):
    o = []
    for v in views:
        if v['alt'].degrees >= min_angle:
            o.append(v)
    return o


@click.group()
def main():
    pass


main.add_command(get_planet_track)
main.add_command(get_sat_track)
main.add_command(get_asteroid_track)
main.add_command(get_voyager_track)

if __name__ == '__main__':
    main()
