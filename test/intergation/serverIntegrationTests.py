import unittest
from time import sleep

from utils.player import Player
from utils.serverSender import load_server
from track.track import Track, TrackESPFormatted
from track.trackRequest import TrackRequest


class ServerRespondTests(unittest.TestCase):
    def test_get_track_from_youtube_music(self):
        server_track = Player().get_current_track()
        server_track_json = server_track.get_track_json()

        track = Track()
        track.set_track_from_track_json(server_track_json)

        print(f"Get track: {track}")
        self.assertEqual(track, server_track)

    def test_send_one_track_to_esp32(self):
        server = load_server()
        server_track = Player().get_current_track()

        esp_track = TrackESPFormatted(server_track)
        esp_track_json = esp_track.get_formatted_track_json()

        server.send(esp_track_json)

        print(f"Transmitted track (original):\t{server_track}\n"
              f"Transmitted track (formatted):\t{esp_track}")

        self.assertTrue(True)

    def test_do_requests_to_youtube_music_player_until_new_track_had_appear(self):
        trackRequest = TrackRequest(Player())
        server = load_server()
        counter = 0

        while counter < 1:
            is_new_track = trackRequest.update()
            if is_new_track:
                esp_track = TrackESPFormatted(trackRequest.track)
                esp_track_json = esp_track.get_formatted_track_json()
                server.send(esp_track_json)

                counter += 1
                print(f"Transmitted track (original):\t{trackRequest.track}\n"
                      f"Transmitted track (formatted):\t{esp_track}\n"
                      f"In order to pass the test change a track in the YouTube Music Player to another one (it may take time for validation)")
                sleep(20)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
