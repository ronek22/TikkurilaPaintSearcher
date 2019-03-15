import math
from scraper import Scraper
import os.path
import jsonpickle
from core.color import Color
from utility import cie94


if __name__ == "__main__":

    colors = None
    scrap = Scraper()

    if not os.path.exists("./data.json"):
        scrap.run_multi()
        colors = scrap.colors
        frozen = jsonpickle.encode(colors)
        with open('data.json', 'w') as text_file:
            print(frozen, file=text_file)
    else:
        with open('data.json', 'r') as text_file:
            colors = jsonpickle.decode(text_file.read())



    while(True):
        choose = int(input("\n\n[1] Szukaj farby\n[2] Zakoncz dzialania\n>> "))
        if choose == 1:
            rgb = input("Podaj rgb po spacji: ")
            rgb = [int(col) for col in rgb.split(' ')] 
            point = Color(*rgb, 0)
            closest_colors = sorted(colors, key=lambda color: cie94(point.cie, color.cie))
            closest_color = closest_colors[0:5]
            print(*closest_color, sep="\n")
        elif choose == 2:
            exit(0)
        else:
            print("Musisz wybrac 1 lub 2\n")
