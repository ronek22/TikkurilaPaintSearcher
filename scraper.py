import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
from core.color import Color
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from concurrent.futures import ThreadPoolExecutor


LINK = 'https://www.tikkurila.pl/farby_dekoracyjne/kolory/wzorniki_kolorow_do_wnetrz/tikkurila_symphony_2436/{}.4374.xhtml'
LETTERS = ['F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'S', 'V']
START_INDEX = 300
END_INDEX = 502
COLORS = []

class Scraper:
    def __init__(self):
        self.colors_index = []
        self.colors = []
        self.get_indexes()

    def run(self):
        for index in tqdm(self.colors_index, total=len(self.colors_index)):
            self.colors.append(self.get_rgb(index))

    def run_multi(self):
        with ThreadPool(30) as pool:
            for result in tqdm(pool.imap(self.get_rgb, self.colors_index, chunksize=1), total=len(self.colors_index)):
                self.colors.append(result)

    def run_parralel(self):
        pool = Pool()
        for x in tqdm(pool.imap_unordered(self.get_rgb, self.colors_index), total=len(self.colors_index)):
            self.colors.append(x)


    def get_rgb(self, index):
        page = self._get_page(index)
        content = page.find('div', class_='colormap-col colormap_detailinfo span6')
        rgb = content.find_all('p')[0].text[14:-9].strip().split(',')
        rgb = [int(col) for col in rgb]
        return Color(*rgb, index)
        

    def _get_page(self, index):
        page = requests.get(LINK.format(index))
        return BeautifulSoup(page.text, 'html.parser')  

    def get_indexes(self):
        for row in range(START_INDEX, END_INDEX + 1):
            for letter in LETTERS: 
                self.colors_index.append(letter + str(row))

        # last row
        for letter in LETTERS[:-2]:
            self.colors_index.append(letter + '503')
                