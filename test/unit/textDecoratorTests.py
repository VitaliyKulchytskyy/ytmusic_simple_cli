import unittest
from track.track import Track, TrackESPFormatted
from utils.textDecorator import SafeSymbolsDecode, SafeSymbols,  TransliterationUkr


class TextDecoratorsTests(unittest.TestCase):
    def test_transliteration(self):
        cyrillic_symbols = ''.join(TransliterationUkr.replace_dict.keys())
        json = {'artist': 'None',
                'track_name': cyrillic_symbols,
                'album_name': 'None',
                'thumb_url': "None"}

        track = Track()
        track.set_track_from_track_json(json)
        track_json = TrackESPFormatted(track).get_track_json()
        cyrillic_track_name = str(SafeSymbolsDecode(track_json['track_name']))

        cyrillic_transliteration = ''.join(TransliterationUkr.replace_dict.values())
        self.assertEqual(cyrillic_transliteration, cyrillic_track_name)

    def test_safe_symbols_code(self):
        sample = "\'test\""

        expected = sample.replace('\'', SafeSymbols.quote_symbol)\
                         .replace('\"', SafeSymbols.quote_symbol)

        self.assertEqual(expected, str(SafeSymbols(sample)))

    def test_safe_symbols_decode(self):
        sample = f"{SafeSymbols.quote_symbol}test{SafeSymbols.quote_symbol}"

        expected = sample.replace(SafeSymbols.quote_symbol,
                                  SafeSymbolsDecode.replace_dict[SafeSymbols.quote_symbol])

        self.assertEqual(expected, str(SafeSymbolsDecode(sample)))

    def test_safe_symbols_code_and_decode(self):
        sample = "\'test\'"

        sampleCode = str(SafeSymbols(sample))

        self.assertEqual(sample, str(SafeSymbolsDecode(sampleCode)))


if __name__ == '__main__':
    unittest.main()
