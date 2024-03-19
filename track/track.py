from utils.textDecorator import SafeSymbols, SafeSymbolsDecode, TransliterationUkr


class Track:
    def __init__(self) -> None:
        self.artist: str = "None"
        self.track_name: str = "None"
        self.album_name: str = "None"
        self.album_cover_url: str = "None"

    def set_track_from_track_json(self, track_json: dict) -> None:
        self.artist: str = track_json['artist']
        self.track_name: str = track_json['track_name']
        self.album_name: str = track_json['album_name']
        self.album_cover_url: str = track_json['thumb_url']

    def set_track_from_server_json(self, server_json: dict) -> None:
        self.artist: str = server_json['artists'][0]['name']
        self.track_name: str = server_json['title']
        self.album_name: str = server_json['album']['name']
        self.album_cover_url: str = server_json['thumbnails'][0]['url']

    def get_track_json(self) -> dict:
        return {'artist': self.artist,
                'track_name': self.track_name,
                'album_name': self.album_name,
                'thumb_url': self.album_cover_url}

    def __eq__(self, o: object) -> bool:
        return self.artist == o.artist \
            and self.track_name == o.track_name \
            and self.album_name == o.album_name \
            and self.album_cover_url == o.album_cover_url

    def __str__(self) -> str:
        return f"{self.artist} - {self.track_name} | {self.album_name} ({self.album_cover_url})"


class TrackESPFormatted(Track):
    @staticmethod
    def __get_formatted_track_data(data: str) -> str:
        convert_to_cyrillic = str(TransliterationUkr(data))
        output = SafeSymbols(convert_to_cyrillic)
        return str(output)

    def __init__(self, track: Track) -> None:
        super().__init__()
        self.track = track
        self.__convert_to_esp_format()

    def __convert_to_esp_format(self) -> None:
        self.artist = self.__get_formatted_track_data(self.track.artist)
        self.track_name = self.__get_formatted_track_data(self.track.track_name)
        self.album_name = self.__get_formatted_track_data(self.track.album_name)
        self.album_cover_url = self.__get_formatted_track_data(self.track.album_cover_url)

    def get_formatted_track_json(self) -> str:
        track_json = self.get_track_json()
        esp_json_format = str(track_json).replace('\'', '\"')
        return str(SafeSymbolsDecode(esp_json_format))
