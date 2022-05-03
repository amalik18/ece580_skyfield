# Overview
This project serves as proof that the [Skyfield](https://rhodesmill.org/skyfield/) library is a viable option
to track planets, satellites, and other celestial bodies. This work aims to provide a proof of concept to the
George Mason University's satellite research division by providing the Time, Altitude, Azimuth, and the Distance
of each body.

# Setup
To get started using this library you need to ensure that Python3.5+ is installe don the host system. Additionally, to install the Skyfield Python package, as well as, the two packages that deal with the differing types of ephemeris data. 

```bash
$ python -m pip install skyfield spktype01 spktype21
```

The command up above will downlaod all necessary dependencies for this library to work properly. 

# Usage
This library is created as a CLI tool, that can be invoked with inputs. Below are examples of using this library
as a CLI to determine certain calculations. Below are the supported commands which can be accessed by running 

```bash
$ python track.py --help

Usage: track.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  track_asteroid  Function to track the orbit of the Didymos asteroid.
  track_planet    Function to track planetary changes relative to a provided
                  location.
  track_sat       Function to track a satellite path relative to provided
                  location.
  track_voyager   Function to track the Voyager 1 space probe.
```

Below we'll cover the commands and their usage.

### **Tracking an Asteroid**
This command, presently, only tracks the orbit of the 6583 Didymos asteroid. The inputs to this command are
as follows:
* `latitude`: latitude of the location from where you want to track.
* `longitude`: longitude of the location from where you want to track.
* `initial_time`: the start time of your tracking, when you want to track from.
* `end_time`: the end time of your tracking, when you want to track till.
* `points`: number of samples or points you want to collect.
* `angle`: the minimum viewing angle.

The output of this command:
* This command prints the time, altitude, azimuth, and distance for each point from [0, points)

Below is the help menu for this command, which provides all of the inputs, the constraints, and requirements.

```bash
$ python track.py track_asteroid --help
Usage: track.py track_asteroid [OPTIONS]

Options:
  --latitude, --lat FLOAT   Latitude of the location from which you want to
                            track.  [required]
  --longitude, --lon FLOAT  Longitude of the locaiton from which you want to
                            track.  [required]
  --initial_time TEXT       Start time from which you'd like to observe the
                            planetary track. Of the form YYYY/MM/DD-HH:MM:SS
                            [default: 2022/05/01-00:00:00; required]
  --end_time TEXT           End time for which you'd like to observe the
                            planetary track till. Of the form YYYY/MM/DD-
                            HH:MM:SS  [default: 2022/05/2-00:00:00; required]
  -p, --points INTEGER      Number of samples to collect.  [default: 100;
                            required]
  -a, --angle INTEGER       The minimum viewing angle.  [default: 0; required]
  --help                    Show this message and exit.
```

Below is an example usage of this command:

```bash
$ python track.py track_asteroid --lat 38.827480 --lon -77.305472 --initial_time "2022/05/01-00:00:00" --end_time "2022/05/2-00:00:00" --points 1000 --angle 0
```

---

### **Tracking a Planet**
This commands tracks the orbit of any given planet within our Solar System. The inputs to this command are
as follows:
* `planet`: the planet whose orbit will be tracked.
* `latitude`: latitude of the location from where you want to track.
* `longitude`: longitude of the location from where you want to track.
* `initial_time`: the start time of your tracking, when you want to track from.
* `end_time`: the end time of your tracking, when you want to track till.
* `points`: number of samples or points you want to collect.
* `angle`: the minimum viewing angle.

The output of this command:
* This command prints the time, altitude, azimuth, and distance for each point from [0, points)

Below is the help menu for this command:

```bash
$ python track.py track_planet --help
Usage: track.py track_planet [OPTIONS]

Options:
  --planet TEXT             Planet to track.  [default: mars; required]
  --latitude, --lat FLOAT   Latitude of the location from which you want to
                            track.  [required]
  --longitude, --lon FLOAT  Longitude of the locaiton from which you want to
                            track.  [required]
  --initial_time TEXT       Start time from which you'd like to observe the
                            planetary track. Of the form YYYY/MM/DD-HH:MM:SS
                            [default: 2022/05/01-00:00:00; required]
  --end_time TEXT           End time for which you'd like to observe the
                            planetary track till. Of the form YYYY/MM/DD-
                            HH:MM:SS  [default: 2022/05/2-00:00:00; required]
  -p, --points INTEGER      Number of samples to collect.  [default: 100;
                            required]
  -a, --angle INTEGER       The minimum viewing angle.  [default: 0; required]
  --help                    Show this message and exit.
```

Below is an example usage of the command:

```bash
$ python track.py track_planet --planet mars --lat 38.827480 --lon -77.305472 --initial_time "2022/05/01-00:00:00" --end_time "2022/05/2-00:00:00" --points 1000  --angle 0
```

---

### **Tracking a Satellite**
This command tracks the orbit of the International Space Station (ISS) ZARYA.
The inputs to this command are as follows:

* `latitude`: latitude of the location from where you want to track.
* `longitude`: longitude of the location from where you want to track.
* `initial_time`: the start time of your tracking, when you want to track from.
* `end_time`: the end time of your tracking, when you want to track till.
* `points`: number of samples or points you want to collect.
* `angle`: the minimum viewing angle.

The output of this command:
* This command prints the time, altitude, azimuth, and distance for each point from [0, points)

Below is the help menu for this command:

```bash
$ python track.py track_sat --help
Usage: track.py track_sat [OPTIONS]

Options:
  --latitude, --lat FLOAT   Latitude of the location from which you want to
                            track.  [required]
  --longitude, --lon FLOAT  Longitude of the locaiton from which you want to
                            track.  [required]
  --initial_time TEXT       Start time from which you'd like to observe the
                            planetary track. Of the form YYYY/MM/DD-HH:MM:SS
                            [default: 2022/05/01-00:00:00; required]
  --end_time TEXT           End time for which you'd like to observe the
                            planetary track till. Of the form YYYY/MM/DD-
                            HH:MM:SS  [default: 2022/05/2-00:00:00; required]
  -p, --points INTEGER      Number of samples to collect.  [default: 100;
                            required]
  -a, --angle INTEGER       The minimum viewing angle.  [default: 0; required]
  --help                    Show this message and exit.
```

Below is an example usage of the command:

```bash
$ python track.py track_sat --lat 38.827480 --lon -77.305472 --initial_time "2022/05/01-00:00:00" --end_time "2022/05/2-00:00:00" --points 1000 --angle 0
```

---

### **Tracking the Voyager 1**
This command tracks the orbit of the Voyager 1 space probe. The inputs for this command
are as follows:

* `latitude`: latitude of the location from where you want to track.
* `longitude`: longitude of the location from where you want to track.
* `initial_time`: the start time of your tracking, when you want to track from.
* `end_time`: the end time of your tracking, when you want to track till.
* `points`: number of samples or points you want to collect.
* `angle`: the minimum viewing angle.

The output of this command:
* This command prints the time, altitude, azimuth, and distance for each point from [0, points)

Below is the help menu for this command:

```bash
$ python track.py track_voyager --help
Usage: track.py track_voyager [OPTIONS]

Options:
  --latitude, --lat FLOAT   Latitude of the location from which you want to
                            track.  [required]
  --longitude, --lon FLOAT  Longitude of the locaiton from which you want to
                            track.  [required]
  --initial_time TEXT       Start time from which you'd like to observe the
                            planetary track. Of the form YYYY/MM/DD-HH:MM:SS
                            [default: 2022/05/01-00:00:00; required]
  --end_time TEXT           End time for which you'd like to observe the
                            planetary track till. Of the form YYYY/MM/DD-
                            HH:MM:SS  [default: 2022/05/2-00:00:00; required]
  -p, --points INTEGER      Number of samples to collect.  [default: 100;
                            required]
  -a, --angle INTEGER       The minimum viewing angle.  [default: 0; required]
  --help                    Show this message and exit.
```

Below is an example usage of the command:
```bash
$ python track.py track_voyager --lat 38.827480 --lon -77.305472 --initial_time "2022/05/01-00:00:00" --end_time "2022/05/2-00:00:00" --points 1000 --angle 0
```

---