"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts
from datetime import datetime

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """The itinerary should return a list of concerts that state the artist, date, and location of each concert."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        self.assertIsInstance(itinerary, list)
        self.assertTrue(all(isinstance(concert, list) and len(concert) == 3 for concert in itinerary))

    def test_manual_2(self):
        """The itinerary should return a list of concerts sorted in chronological order (by date from earliest to latest)."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        sorted_itinerary = sorted(itinerary, key=lambda x: x[1])
        self.assertEqual(itinerary, sorted_itinerary)

    def test_manual_3(self):
        """Some artists may have no concerts on the list. In that case, that should be indicated in the itinerary."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        all_artists = {concert.artist for concert in self.all_concerts}
        itinerary_artists = {concert[0] for concert in itinerary}
        missing_artists = all_artists - itinerary_artists
        self.assertTrue(len(missing_artists) == 0 or all(artist not in itinerary_artists for artist in missing_artists))

    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.

    def test_ai_assisted_no_duplicate_dates(self):
        """The itinerary should not include two concerts on the same date."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        dates = [concert[1] for concert in itinerary]
        self.assertEqual(len(dates), len(set(dates)), "Itinerary contains duplicate dates.")

    def test_ai_assisted_sort_by_date(self):
        """Concerts should be sorted by date, and by artist name alphabetically if dates are the same."""
        # Create mock data for testing
        concerts = [
            Concert("Artist B", "2025-05-01", "Location 2", 0.0, 0.0),
            Concert("Artist A", "2025-05-01", "Location 1", 0.0, 0.0),
            Concert("Artist C", "2025-05-02", "Location 3", 0.0, 0.0)
        ]
        itinerary = self.builder.build_itinerary(concerts)
        self.assertEqual(itinerary[0][0], "Artist B", "Concerts were not sorted by date and artist name alphabetically.")
        self.assertEqual(itinerary[1][0], "Artist C", "Concerts were not sorted by date and artist name alphabetically.")

    def test_ai_assisted_closest_concert_on_same_date(self):
        """If two concerts are on the same date, the one closest to the last concert should be included."""
        # Create mock data for testing
        concerts = [
            Concert("Artist A", "2025-05-01", "Location 1", 10.0, 10.0),
            Concert("Artist B", "2025-05-01", "Location 2", 20.0, 20.0),
            Concert("Artist C", "2025-05-02", "Location 3", 30.0, 30.0)
        ]
        itinerary = self.builder.build_itinerary(concerts)
        self.assertEqual(itinerary[0][0], "Artist A", "Closest concert on the same date was not selected.")

if __name__ == "__main__":
    unittest.main()