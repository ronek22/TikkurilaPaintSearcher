from collections import namedtuple
from utility import rgb2lab

Rgb = namedtuple('Rgb', ('r', 'g', 'b'))
LINK = 'https://www.tikkurila.pl/farby_dekoracyjne/kolory/wzorniki_kolorow_do_wnetrz/tikkurila_symphony_2436/{}.4374.xhtml'

class Color:
    def __init__(self, r, g, b, index):
        self.rgb = Rgb(r, g, b)
        self.cie = rgb2lab(self.rgb)
        self.index = index
        self.url = LINK.format(index)

    def __repr__(self):
        return "Color {}: {} \t {}".format(self.index, str(self.rgb), self.url)
    