from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from time import sleep, time
from bs4 import BeautifulSoup as bs
import urllib.request 
import pandas as pd
#from tours_settings import CITIES, BASE_URL, DRIVER_PATH, COOKIE_BTN

DRIVER_PATH = "C:/Users/admin/Desktop/chromedriver.exe"

class MoviesScraper:

    # chrome_options.add_argument('--window-size=1420,1080')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    def __init__(self):
        self.driver_path = DRIVER_PATH
        self.url = 'https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=26ENPSP3CPZMW3XZC4C0&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3'
        service = Service(self.driver_path)
        chrome_options = Options()
        
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-setuid-sandbox")
        # chrome_options.add_argument("--remote-debugging-port=9222")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("enable-features=NetworkServiceInProcess")
        # chrome_options.add_argument("disable-features=NetworkService")
        # chrome_options.add_argument("window-size=1920,1080")
        # chrome_options.add_argument("--ignore-certificate-errors")
        # chrome_options.add_argument("--ignore-ssl-errors")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--log-level=3")
        # chrome_prefs = {}
        # chrome_options.experimental_options["prefs"] = chrome_prefs
        # chrome_prefs["profile.default_content_settings"] = {"images": 2}
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def get_urls(self):
        """
            The function takes a list of cities and returns a list of urls of each city.


            Returns:
                city_names (List): List of strings of popular city names.


        """

        self.driver.get(self.url)
        sleep(5)
        soup = bs(self.driver.page_source, "lxml")
        movies = soup.find_all('tbody', class_="lister-list") 
        #images = soup.find_all('img')

        
        
    #filename = "pics/picture{}.jpg"
    # for i in range(len(imgdata)):
    #     print(f"img {i+1} / {len(imgdata)+1}")
    # # try block because not everything in the imgdata list is a valid url
    # try:
    #     r = requests.get(imgdata[i], stream=True)
    #     with open(filename.format(i), "wb") as f:
    #         f.write(r.content)
    # except:
    #     print("Url is not an valid")
     
        # urls = []
        image_urls = []
        titles = []
        movies_urls = []
        genres = []
        descs = []
        for movie in movies:
            title_links = movie.find_all('td', class_="titleColumn")
            image_links = movie.find_all('td', class_="posterColumn")
            #print(title_links)


        for title_link in title_links:
            link = title_link.find('a').get('href')
            title = title_link.find('a').text
            link = 'https://imdb.com' + link
            movies_urls.append(link)
            titles.append(title)

       

        for image_link in image_links:
            img_link = image_link.find('img')
            image_urls.append(img_link.get('src'))
        #print(len(image_urls))
        
        
        # counter = 0
        # while counter < len(image_urls):
        #     for img in image_urls:
        #         img_str = img.split('/')
        #         counter += 1
        #         filename = f'{str(counter)}.{img_str[5][6:11]}'
        #         urllib.request.urlretrieve(img, f"images/{filename}.jpg")
        
            

        for m_url in movies_urls:
            self.driver.get(m_url)
            sleep(5)
            soup = bs(self.driver.page_source, "lxml")
            genre = soup.find('span', class_="ipc-chip__text").text
            genres.append(genre)
            desc = soup.find('span', class_="sc-16ede01-1 kgphFu").text
            descs.append(desc)
        
        

        df = pd.DataFrame({
            'title': titles,
            'movie link': movies_urls,
            'description': descs,
            'genre': genres,
            'image_url': image_urls
        })
        all_movies = df.to_dict(orient='index')
        #print(all_movies)

        with open('data.txt','w') as data: 
            data.write(str(all_movies))

        return all_movies


if __name__ == '__main__':
    scraper = MoviesScraper()
    scraper.get_urls()
    scraper.driver.quit()