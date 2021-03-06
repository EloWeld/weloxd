from random import choice, randrange


def default_brim(x):
    return x


class TextStylist:
    def __init__(self, main_text: str = 'Sample text'):
        self.main_text = main_text
        self.styles = {
            'square_black':
                {
                    'dict': '๐ฐ ๐ฑ ๐ฒ ๐ณ ๐ด ๐ต ๐ถ ๐ท ๐ธ ๐น ๐บ ๐ป ๐ผ ๐ฝ ๐พ ๐ฟ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฐ ๐ฑ ๐ฒ '
                            '๐ณ ๐ด ๐ต ๐ถ ๐ท ๐ธ ๐น ๐บ ๐ป ๐ผ ๐ฝ ๐พ ๐ฟ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ 0โฃ 1โฃ 2โฃ 3โฃ 4โฃ 5โฃ '
                            '6โฃ 7โฃ 8โฃ 9โฃ'.split(),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'old_english':
                {
                    'dict': '๐๐โญ๐๐๐๐โโ๐๐๐๐๐๐๐๐โ๐๐๐๐๐๐๐โจ๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'outline':
                {
                    'dict': '๐ธ๐นโ๐ป๐ผ๐ฝ๐พโ๐๐๐๐๐โ๐โโโ๐๐๐๐๐๐๐โค๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐๐๐๐๐๐๐๐๐ ๐ก',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'cursive-bold':
                {
                    'dict': '๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'upside_down':
                {
                    'dict': "โฑฏ ๊ญ ฦ ๊ท ฦ โฒ ๊จ H I ลฟ ๊ ๊ถ ฤ N O ิ Oฬ ๊ค S ๊ ๊ต ๊ฅ M X โ Z ษ ฤ ษ ฤ ว ษ ฦ ษฅ ฤฑฬฃ ษพฬฃ ส ื ษฏ ฤ o d b "
                            "ษน s ส n ส ส x ส z 0 1 2 3 4 5 6 7 8 9ุ".split(" "),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'bold':
                {
                    'dict': "๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐  ๐ก ๐ข ๐ฃ ๐ค ๐ฅ ๐ฆ ๐ง ๐จ ๐ฉ ๐ช ๐ซ ๐ฌ ๐ญ ๐ฎ ๐ฏ ๐ฐ "
                            "๐ฑ ๐ฒ ๐ณ ๐ด ๐ต ๐ถ ๐ท ๐ธ ๐น ๐บ ๐ป ๐ผ ๐ฝ ๐พ ๐ฟ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฌ ๐ญ ๐ฎ ๐ฏ ๐ฐ ๐ฑ "
                            "๐ฒ ๐ณ ๐ด ๐ต".split(" "),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'zalgo':
                {
                    'dict': "๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐  ๐ก ๐ข ๐ฃ ๐ค ๐ฅ ๐ฆ ๐ง ๐จ ๐ฉ ๐ช ๐ซ ๐ฌ ๐ญ ๐ฎ ๐ฏ ๐ฐ "
                            "๐ฑ ๐ฒ ๐ณ ๐ด ๐ต ๐ถ ๐ท ๐ธ ๐น ๐บ ๐ป ๐ผ ๐ฝ ๐พ ๐ฟ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฌ ๐ญ ๐ฎ ๐ฏ ๐ฐ ๐ฑ "
                            "๐ฒ ๐ณ ๐ด ๐ต".split(" "),
                    'func': lambda x: self.zalgo_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'cursive-brim':
                {
                    'dict': '๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ ๐ก๐ข๐ฃ๐ค๐ฅ๐ฆ๐ง๐จ๐ฉ๐ช๐ซ๐ฌ๐ญ๐ฎ๐ฏ๐ฐ๐ฑ๐ฒ๐ณ๐ด๐ต๐ถ๐ท๐ธ๐น๐บ๐ป๐ผ๐ฝ๐พ๐ฟ๐๐๐๐0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.emoji_brim(text),
                },
        }
        self.zalgodict = {
            'up': ["ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬฝ", "ฬพ", "ฬฟ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ"],
            'mid': ["ฬด", "ฬต", "ฬถ", "ฬท", "ฬธ", "า", "า"],
            'down': ["ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ", "ฬ ", "ฬฃ", "ฬค", "ฬฅ", "ฬฆ", "ฬฉ", "ฬช", "ฬซ", "ฬฌ", "ฬญ", "ฬฎ", "ฬฏ", "ฬฐ", "ฬฑ", "ฬฒ", "ฬณ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ", "อ"],
            'under': ["ฬก", "ฬข", "ฬง", "ฬจ", "อ", "อข"],
            'above': ["ฬ", "ฬ", "อ", "อ", "อ ", "อก", "า"],
            'other': ["อ", "อ", "อฃ", "อค", "อฅ", "อฆ", "อง", "อจ", "อฉ", "อช", "อซ", "อฌ", "อญ", "อฎ", "อฏ"]
        }

    def get_stylized(self):
        result = []
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

        for style in self.styles.values():
            stylized_text = ''
            for x in self.main_text:
                if x in letters:
                    let = style['dict'][letters.index(x)]
                    stylized_text += style['func'](let)
                else:
                    stylized_text += x
            result += [style['brim'](stylized_text)]
        return result

    def set_main_text(self, new_text):
        self.main_text = new_text

    def zalgo_style(self, x):
        res = x
        for i in range(randrange(1,10)):
            res += choice(self.zalgodict[choice(['up', 'mid', 'down', 'under', 'other', 'above'])])
        return res

    def default_style(self, x):
        return x

    def default_brim(self, x):
        return x

    def emoji_brim(self, x):
        return f'โ{x}โ'


Stylist = TextStylist()
