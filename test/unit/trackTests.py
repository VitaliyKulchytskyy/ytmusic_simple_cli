import unittest
from track.track import Track, TrackESPFormatted
from utils.textDecorator import TransliterationUkr


class MyTestCase(unittest.TestCase):
    def test_set_from_another_track_json(self):
        sample = {'artist': 'Portishead',
                  'track_name': 'All Mine',
                  'album_name': 'Portishead',
                  'thumb_url': "None"}
        track = Track()
        track.set_track_from_track_json(sample)

        self.assertEqual(sample, track.get_track_json())

    def test_set_track_from_player_server(self):
        server_json = {'videoId': '_siJRgDlddY',
                       'title': 'Nutshell',
                       'artists': [{'name': 'Alice In Chains',
                                    'id': 'UCjtMrcJSQnXyE0rGfQlr8MA'}],
                       'album': {'name': 'Jar Of Flies',
                                 'id': 'MPREb_jvZuuciy5uA'},
                       'likeStatus': 'LIKE',
                       'thumbnails': [{'url': 'https://lh3.googleusercontent.com/3ZIo-Lh1lTgGqhWmt77m2H-PuU8h9FUjlV-reHBJ0dlKXl7duFN1p1bAeRMHo2j3Uf31F-duBDCBnz1E=w60-h60-l90-rj',
                                       'width': 60,
                                       'height': 60},
                                      {'url': 'https://lh3.googleusercontent.com/3ZIo-Lh1lTgGqhWmt77m2H-PuU8h9FUjlV-reHBJ0dlKXl7duFN1p1bAeRMHo2j3Uf31F-duBDCBnz1E=w120-h120-l90-rj',
                                       'width': 120,
                                       'height': 120}],
                       'isAvailable': True,
                       'isExplicit': False,
                       'videoType': 'MUSIC_VIDEO_TYPE_ATV',
                       'duration': '4:20',
                       'duration_seconds': 260,
                       'feedbackTokens': {'add': 'AB9zfpIlxFwhPY8ndkhw6wCwk2pRuZetNbvpdqYZJzGWUmAX4xX1-d2tNKS9953WzFvVZsLAgDKXPYiCYvfCLijDe2V1Nwwh-w',
                                          'remove': 'AB9zfpKfFUK_xyemBxWa5Lj1HrJAxYpxAyshup8Wg7iulXBf-BqMNQpTXD4N870WkOhNdj2BqFrWTVdW9osZH2aSrx8USLI9HA'},
                       'feedbackToken': 'AB9zfpIvg61yMJM5BCb3JRQYoru57zhxMYX9cjWVJmc6PimCIJBvon2yXTnbZcEYF2OWwfbJ1fpXzVW3dXYj0HPuCkLJnvYZtQ',
                       'played': 'Today'}
        server_track = Track()
        server_track.set_track_from_server_json(server_json)

        track_json = {'artist': 'Alice In Chains',
                      'track_name': 'Nutshell',
                      'album_name': 'Jar Of Flies',
                      'thumb_url': 'https://lh3.googleusercontent.com/3ZIo-Lh1lTgGqhWmt77m2H-PuU8h9FUjlV-reHBJ0dlKXl7duFN1p1bAeRMHo2j3Uf31F-duBDCBnz1E=w60-h60-l90-rj'}
        track = Track()
        track.set_track_from_track_json(track_json)

        self.assertEqual(track, server_track)

    def test_tracks_equality(self):
        sample_1 = {'artist': 'Portishead',
                    'track_name': 'All Mine',
                    'album_name': 'Portishead',
                    'thumb_url': "None"}
        track_1 = Track()
        track_1.set_track_from_track_json(sample_1)

        sample_2 = {'artist': 'Portishead',
                    'track_name': 'All Mine',
                    'album_name': 'Portishead',
                    'thumb_url': "None"}
        track_2 = Track()
        track_2.set_track_from_track_json(sample_2)

        self.assertEqual(track_1, track_2)

    def test_set_formatted_track_for_esp32(self):
        sample = {'artist': 'Бумбокс',
                  'track_name': 'Почути',
                  'album_name': 'Меломанія',
                  'thumb_url': "None"}
        track = Track()
        track.set_track_from_track_json(sample)

        trackFormatted = TrackESPFormatted(track)
        convertedSample = {'artist': str(TransliterationUkr(sample['artist'])),
                           'track_name': str(TransliterationUkr(sample['track_name'])),
                           'album_name': str(TransliterationUkr(sample['album_name'])),
                           'thumb_url': "None"}

        self.assertEqual(convertedSample, trackFormatted.get_track_json())


if __name__ == '__main__':
    unittest.main()
