import math
from .scraper import Scraper
import os.path
import jsonpickle
from .core.color import Color
from .utility import cie94
from pathlib import Path
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
DATA_PATH = os.path.join(APP_ROOT, 'data.json')
colors = []
scrap = Scraper()

if not os.path.exists(DATA_PATH):
    scrap.run_multi()
    colors = scrap.colors
    frozen = jsonpickle.encode(colors)
    with open(DATA_PATH, 'w') as text_file:
        print(frozen, file=text_file)
else:
    with open(DATA_PATH, 'r') as text_file:
        colors = jsonpickle.decode(text_file.read())

def search_for_colors(r, g, b):
    point = Color(r,g,b, 0)
    closest_colors = sorted(colors, key=lambda color: cie94(point.cie, color.cie))
    closest_color = closest_colors[0:6]
    return closest_color
