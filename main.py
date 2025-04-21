"""
Concert Itinerary Builder

This module provides functionality to build an itinerary of upcoming concerts.
"""

import math
from datetime import datetime

class Concert:
    """
    Represents a concert event.
    
    Attributes:
        artist (str): The name of the artist performing.
        date (str): The date of the concert in 'YYYY-MM-DD' format.
        location (str): The location where the concert will take place.
        latitude (float): Latitude coordinate of the concert location.
        longitude (float): Longitude coordinate of the concert location.
    """
    
    def __init__(self, artist, date, location, latitude, longitude):
        self.artist = artist
        self.date = date
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

class ItineraryBuilder:
    """
    A class to build concert itineraries. 
    """
    
    def build_itinerary(self, concerts):
        artist_concerts = {}
        for concert in concerts:
            if concert.artist not in artist_concerts or datetime.strptime(concert.date, "%Y-%m-%d") < datetime.strptime(artist_concerts[concert.artist].date, "%Y-%m-%d"):
                artist_concerts[concert.artist] = concert
        unique_concerts = list(artist_concerts.values())
        unique_concerts.sort(key=lambda c: datetime.strptime(c.date, "%Y-%m-%d"))

        final_itinerary = []
        used_dates = set()
        for concert in unique_concerts:
            if concert.date not in used_dates:
                final_itinerary.append([
                    concert.artist,
                    concert.date,
                    concert.location
                ])
                used_dates.add(concert.date)
        return final_itinerary

if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()