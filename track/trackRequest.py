from track.track import Track
from utils.player import Player


class TrackRequest:
    def __init__(self, player: Player) -> None:
        self.player: Player = player
        self.track: Track = Track()

    def update(self) -> bool:
        temp = self.__get_current_track()

        if temp != self.track:
            self.track = temp
            return True

        return False

    def __get_current_track(self) -> Track:
        return self.player.get_current_track()
