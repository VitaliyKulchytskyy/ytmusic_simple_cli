import re
import cyrtranslit


class TextDecoratorBase:
    def __init__(self, data: str, replace_dict: dict) -> None:
        self.data: str = data
        self.replace_dict: dict = replace_dict

    def replace(self) -> str:
        regex = re.compile('|'.join(map(re.escape, self.replace_dict)))
        return regex.sub(lambda match: self.replace_dict[match.group(0)], self.data)

    def __str__(self) -> str:
        return self.replace()


class SafeSymbols(TextDecoratorBase):
    quote_symbol = '[^@^]'
    replace_dict = {'\'': quote_symbol,
                    '\"': quote_symbol}

    def __init__(self, data: str) -> None:
        super().__init__(data, self.replace_dict)


class SafeSymbolsDecode(TextDecoratorBase):
    replace_dict = {SafeSymbols.quote_symbol: '\''}

    def __init__(self, data: str) -> None:
        super().__init__(data, self.replace_dict)


class TransliterationUkr(TextDecoratorBase):
    replace_dict = {'Č': 'Ch',
                    'č': 'ch',
                    'Ć': 'S',
                    'ć': 's',
                    'Š': 'Sh',
                    'š': 'sh',
                    'Ž': 'Z',
                    'ž': 'z',
                    'Ï': 'Yi',
                    'ï': 'yi',
                    'Ё': 'Jo',
                    'ё': 'jo',
                    'Ы': 'U',
                    'ы': 'u',
                    'ъ': ''}

    def __init__(self, data: str) -> None:
        convert_to_cyrillic: str = cyrtranslit.to_latin(data, 'ua')
        super().__init__(convert_to_cyrillic, self.replace_dict)
