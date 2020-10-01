#!/usr/bin/env python

__author__ = 'Andrew Canter'

import requests
import turtle
import time

def main():
    '''Collects and prints the names of people currently in space'''
    astronauts = requests.get('http://api.open-notify.org/astros.json').json()
    
    print('Currently ' + str(astronauts['number']) + ' people in space')
    for person in astronauts['people']:
        print(person['name'] + ' on the ' + person['craft'])

    '''Gets ISS lat/lon position and show on a map'''
    issPosition = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat = float(issPosition['iss_position']['latitude'])
    lon = float(issPosition['iss_position']['longitude'])

    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')

    t = turtle.Turtle()
    t.shape('iss.gif')
    t.penup()
    t.goto(lon , lat)
    t.stamp()

    '''Shows when ISS will be over Indianapolis next'''
    indyLat = 39.768403
    indyLong = -86.158068
    indyISS = requests.get('http://api.open-notify.org/iss-pass.json?lat=' + str(indyLat) + '&lon=' + str(indyLong)).json()

    t.shape('circle')
    t.color('blue')
    t.goto(indyLong, indyLat)
    t.dot(3)
    t.hideturtle()
    t.write(time.ctime(indyISS['response'][0]['risetime']))

    screen.exitonclick()

if __name__ == '__main__':
    main()
