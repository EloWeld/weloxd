from random import choice, randrange


def default_brim(x):
    return x


class TextStylist:
    def __init__(self, main_text: str = 'Sample text'):
        self.main_text = main_text
        self.styles = {
            'square_black':
                {
                    'dict': '🅰 🅱 🅲 🅳 🅴 🅵 🅶 🅷 🅸 🅹 🅺 🅻 🅼 🅽 🅾 🅿 🆀 🆁 🆂 🆃 🆄 🆅 🆆 🆇 🆈 🆉 🅰 🅱 🅲 '
                            '🅳 🅴 🅵 🅶 🅷 🅸 🅹 🅺 🅻 🅼 🅽 🅾 🅿 🆀 🆁 🆂 🆃 🆄 🆅 🆆 🆇 🆈 🆉 0⃣ 1⃣ 2⃣ 3⃣ 4⃣ 5⃣ '
                            '6⃣ 7⃣ 8⃣ 9⃣'.split(),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'old_english':
                {
                    'dict': '𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'outline':
                {
                    'dict': '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'cursive-bold':
                {
                    'dict': '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'upside_down':
                {
                    'dict': "Ɐ ꓭ Ɔ ꓷ Ǝ Ⅎ ꓨ H I ſ ꓘ ꓶ Ā N O Ԁ Ò ꓤ S ꓕ ꓵ ꓥ M X ⅄ Z ɐ ā ɔ Ă ǝ ɟ ƃ ɥ ı̣ ɾ̣ ʞ ן ɯ ă o d b "
                            "ɹ s ʇ n ʌ ʍ x ʎ z 0 1 2 3 4 5 6 7 8 9؛".split(" "),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'bold':
                {
                    'dict': "𝗔 𝗕 𝗖 𝗗 𝗘 𝗙 𝗚 𝗛 𝗜 𝗝 𝗞 𝗟 𝗠 𝗡 𝗢 𝗣 𝗤 𝗥 𝗦 𝗧 𝗨 𝗩 𝗪 𝗫 𝗬 𝗭 𝗮 𝗯 𝗰 "
                            "𝗱 𝗲 𝗳 𝗴 𝗵 𝗶 𝗷 𝗸 𝗹 𝗺 𝗻 𝗼 𝗽 𝗾 𝗿 𝘀 𝘁 𝘂 𝘃 𝘄 𝘅 𝘆 𝘇 𝟬 𝟭 𝟮 𝟯 𝟰 𝟱 "
                            "𝟲 𝟳 𝟴 𝟵".split(" "),
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'zalgo':
                {
                    'dict': "𝗔 𝗕 𝗖 𝗗 𝗘 𝗙 𝗚 𝗛 𝗜 𝗝 𝗞 𝗟 𝗠 𝗡 𝗢 𝗣 𝗤 𝗥 𝗦 𝗧 𝗨 𝗩 𝗪 𝗫 𝗬 𝗭 𝗮 𝗯 𝗰 "
                            "𝗱 𝗲 𝗳 𝗴 𝗵 𝗶 𝗷 𝗸 𝗹 𝗺 𝗻 𝗼 𝗽 𝗾 𝗿 𝘀 𝘁 𝘂 𝘃 𝘄 𝘅 𝘆 𝘇 𝟬 𝟭 𝟮 𝟯 𝟰 𝟱 "
                            "𝟲 𝟳 𝟴 𝟵".split(" "),
                    'func': lambda x: self.zalgo_style(x),
                    'brim': lambda text: self.default_brim(text),
                },
            'cursive-brim':
                {
                    'dict': '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃0123456789',
                    'func': lambda x: self.default_style(x),
                    'brim': lambda text: self.emoji_brim(text),
                },
        }
        self.zalgodict = {
            'up': ["̀", "́", "̂", "̃", "̄", "̅", "̆", "̇", "̈", "̉", "̊", "̋", "̌", "̍", "̎", "̏", "̐", "̑", "̒", "̓", "̔", "̚", "̽", "̾", "̿", "̀", "́", "͂", "̓", "̈́", "͆", "͊", "͋", "͌", "͐", "͑", "͒", "͗", "͛"],
            'mid': ["̴", "̵", "̶", "̷", "̸", "҈", "҉"],
            'down': ["̖", "̗", "̘", "̙", "̜", "̝", "̞", "̟", "̠", "̣", "̤", "̥", "̦", "̩", "̪", "̫", "̬", "̭", "̮", "̯", "̰", "̱", "̲", "̳", "ͅ", "͇", "͈", "͉", "͍", "͎", "͓", "͔", "͕", "͖", "͙", "͚"],
            'under': ["̡", "̢", "̧", "̨", "͜", "͢"],
            'above': ["̕", "̛", "͝", "͞", "͠", "͡", "҇"],
            'other': ["͏", "͘", "ͣ", "ͤ", "ͥ", "ͦ", "ͧ", "ͨ", "ͩ", "ͪ", "ͫ", "ͬ", "ͭ", "ͮ", "ͯ"]
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
        return f'✔{x}✔'


Stylist = TextStylist()
