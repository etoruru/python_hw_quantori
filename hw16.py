#!/usr/bin/env python3


from geopy.geocoders import Nominatim
import urllib.parse


geolocator = Nominatim(user_agent='find-location')


def convert_to_decimal(coord):
    if len(coord) == 1:
        return coord[0]
    elif len(coord) == 2:
        return str(int(coord[0]) + int(coord[1][:-1]) / 60 )
    elif len(coord) == 3:
        return str(int(coord[0]) + int(coord[1][:-1]) / 60 + int(coord[2][:-1]) / 3600 )


def create_query(coord):
    params = {'api': 1, 'query': coord}
    return urllib.parse.urlencode(params)


def create_url(coordinaties):
    scheme = 'https'
    netloc = 'www.google.com'
    path = '/maps/search/'
    params = ''
    query = create_query(coordinaties)
    fragment = ''
    tuple_url = (scheme, netloc, path, params, query, fragment)
    return urllib.parse.urlunparse(tuple_url)


with open('gps_file.txt', 'r') as fl:
    coords = fl.readlines()

for coord in coords:
    latitude, longitude = coord[:-1].split(';')
    lat_parts = latitude.split(',')
    long_parts = longitude.split(',')
    decimal_coord = convert_to_decimal(lat_parts) + ',' + convert_to_decimal(long_parts)  

    location = geolocator.reverse(decimal_coord)
    print(f'Location: {location}')
    print(f'Google Maps URL:  {create_url(decimal_coord)}')





