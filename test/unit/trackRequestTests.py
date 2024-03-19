import unittest
from unittest.mock import MagicMock
from track.track import Track
from track.trackRequest import TrackRequest
from utils.player import Player


class TrackRequestTest(unittest.TestCase):
    def test_track_request_if_there_is_no_new_track(self):
        sample_1 = {'artist': 'Portishead',
                    'track_name': 'All Mine',
                    'album_name': 'Portishead',
                    'thumb_url': "None"}
        track_1 = Track()
        track_1.set_track_from_track_json(sample_1)

        player_mock = MagicMock(spec=Player)
        player_mock.get_current_track.return_value = track_1

        trackRequest = TrackRequest(player_mock)
        trackRequest.update()
        trackRequest.update()
        status = trackRequest.update()

        self.assertFalse(status)

    def test_track_request_if_there_is_new_track(self):
        sample_1 = {'artist': 'Portishead',
                    'track_name': 'All Mine',
                    'album_name': 'Portishead',
                    'thumb_url': "None"}
        track_1 = Track()
        track_1.set_track_from_track_json(sample_1)

        sample_2 = {'artist': 'Queen',
                    'track_name': 'My Melancholy Blues',
                    'album_name': 'News Of the World',
                    'thumb_url': "None"}
        track_2 = Track()
        track_2.set_track_from_track_json(sample_2)

        player_mock = MagicMock(spec=Player)
        player_mock.get_current_track.return_value = track_1

        trackRequest = TrackRequest(player_mock)
        trackRequest.update()
        trackRequest.update()
        player_mock.get_current_track.return_value = track_2
        status = trackRequest.update()

        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
