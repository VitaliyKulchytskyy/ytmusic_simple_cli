from ytmusicapi import YTMusic
from track.track import Track
from utils.path import get_file_from_working_dir


class Player:
    def __init__(self) -> None:
        path = get_file_from_working_dir('user_data/youtube_music', 'oauth.json')
        self.player: YTMusic = YTMusic(str(path))

    def get_current_track(self) -> Track:
        output = Track()
        get_users_history = self.player.get_history()
        output.set_track_from_server_json(get_users_history[0])
        return output
