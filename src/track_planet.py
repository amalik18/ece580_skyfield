from sys import argv
from datetime import datetime, timezone
from client import TrackPlanet
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
    print(*filtered_view, sep="\n")



@click.command('track_sat', short_help="Function to track a satellite path relative to provided location.")
@click.option('--latitude', '--lat', required=True, default='', type=float, show_default=True, help="Latitude of the location from which you want to track.")
@click.option('--longitude', '--lon', required=True, default='', type=float, show_default=True, help="Longitude of the locaiton from which you want to track.")
@click.option('--initial_time', required=True, default='2022/05/01-00:00:00', type=str, show_default=True, help="Start time from which you'd like to observe the planetary track. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--end_time', required=True, default='2022/05/2-00:00:00', type=str, show_default=True, help="End time for which you'd like to observe the planetary track till. Of the form YYYY/MM/DD-HH:MM:SS", callback=validate_time)
@click.option('--points', '-p', required=True, default=100, type=int, show_default=True, help="Number of samples to collect.")
@click.option('--angle', '-a', required=True, default=0, type=int, show_default=True, help="The minimum viewing angle.")
def get_sat_track(latitude, longitude, initial_time, end_time, points, angle):



@click.group()
def main(): 
    pass
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


    sat_track = TrackSatellite(float(lat), float(lon), [line1,line2])
    views = sat_track.get_view(t1,t2,count)
    filtered = sat_track.filter_for_elevation(views,min_angle)
    for f in filtered: 
        print(f)


main.add_command(get_planet_track)


if __name__ == '__main__':
    main()

    

