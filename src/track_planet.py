from sys import argv
from datetime import datetime, timezone
from client import TrackPlanet, TrackSatellite
import click



def validate_time(ctx, param, value):
    return value

def validate_planet(ctx, param, value):
    if value.lower() not in ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'neptune', 'uranus']:
        raise click.BadParameter(f"The planet provided ({value}) is not a valid planet. Please provide a valid planet.")


@click.command('track_planet', short_help="Function to track planetary changes relative to a provided location.")
@click.option('--planet', required=True, type=str, default='mars', show_default=True, callback=validate_planet, help="Planet to track.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True, help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True, help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True, help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True, help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True, help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_planet_track(planet, latitude, longitude, initial_time, end_time, points, angle):
    print(f'Planet: {planet}\nInitial Time: {initial_time}\nEnd Time: {end_time}\n(Lat, Lon): ({latitude}, {longitude})\nPoints: {points}\nAngle: {angle}')
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    planet_client = TrackPlanet(lat=latitude, lon=longitude, planet=planet)
    planet_views = planet_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = planet_client.filter_for_elevation(planet_views, angle)
    return filtered_view



@click.command('track_sat', short_help="Function to track a satellite path relative to provided location.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True, help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True, help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True, help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True, help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True, help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_sat_track(latitude, longitude, initial_time, end_time, points, angle):
    initial_time = datetime.strptime(initial_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    end_time = datetime.strptime(end_time, '%Y/%m/%d-%H:%M:%S').replace(tzinfo=timezone.utc)
    line1 = "1 25544U 98067A   22101.34838098  .00010998  00000+0  20034-3 0  9997"
    line2 = "2 25544  51.6440 307.6369 0004493  11.0035 156.2993 15.50005149334810"
    sat_client = TrackSatellite(lat=latitude, lon=longitude, tle=[line1, line2])
    sat_views = sat_client.get_view(time_start=initial_time, time_stop=end_time, points=points)
    filtered_view = sat_client.filter_for_elevation(sat_views, min_angle=angle)
    return filtered_view






@click.group()
def main(): 
    pass


main.add_command(get_planet_track)


if __name__ == '__main__':
    main()

    

