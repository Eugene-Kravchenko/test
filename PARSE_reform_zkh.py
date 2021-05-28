import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random


# КОДИРОВКА ------------------------------------------------------------------
# enable debugging
import cgitb
cgitb.enable()
 
import sys
import codecs
 
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
 
print("Content-Type: text/html; charset=utf-8")
print()
#------------------------------------------------------------------------------

# URL = 'https://www.reformagkh.ru/search/houses?query=%D1%82%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C'
HOST = 'https://www.reformagkh.ru'

def get_data(url):
  HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'accept': '*/*'} 

  houses = []
  iteration_count = 55
  print(f'всего итераций: #{iteration_count}')

  for item in range (1,55):  # ИТЕРАИРУЕМ ВСЕ СТРАНИЦЫ

    req = requests.get(url + f'page={item}&limit=50', HEADERS)
    # print(req.text)
    time.sleep(3)

    # для каждой итерации цикла создадим отдельную папку и назовем в соответствии со счетом  итерации
    folder_name = f'data/data_{item}'

    if os.path.exists(folder_name):
      print(" folder is alredy exists")
    else:
      os.mkdir(folder_name)

    # with open('index_reform.html', 'w', encoding='utf-8') as file:
    #   file.write(req.text)

    # with open('index_reform.html', encoding='utf-8') as file:
    #   src = file.read()

    with open(f'{folder_name}/projects{item}.html', 'w', encoding='utf-8') as file:
      file.write(req.text)

    with open(f'{folder_name}/projects{item}.html', encoding='utf-8') as file:
      src = file.read()
    
    soup = BeautifulSoup(src, 'lxml')

    items = soup.find_all('a', class_='text-dark')
    proj_urls = []

    for item in items:
      link = HOST+item.get('href')
      # adr = item.text
      # print(item)
      proj_urls.append(link)
      # print(HOST+link, '   ', adr)

    for proj_url in proj_urls: ## получаем инфу с ССЫЛОК  !!!!!!!!!!
      req = requests.get(proj_url, HEADERS ) 
      proj_name = proj_url.split("/")[-1]  # смотри в split.py

      with open( f'{folder_name}/{proj_name}.html', 'w', encoding='utf-8') as file: # сохраняем файл под именем стартапа 
        file.write(req.text)

      with open( f'{folder_name}/{proj_name}.html', encoding='utf-8') as file: 
        src = file.read()


      soup = BeautifulSoup(src, 'lxml')


      proj_data = soup.find('div', class_='row align-items-top justify-content-between') # КОНТЕН 
      # print(proj_data)
      proj_data_6_obj = proj_data.find_all(class_='house-specs') 
      # print(proj_data_6_obj)
      if proj_data_6_obj is None:
        continue

      try: # ФОТО
        proj_photo = proj_data.find('div', class_='jcarousel-zoomable-img').find('a', class_='data-image-url')
        # if proj_photo: 
        #   proj_photo = HOST+proj_photo.get('href')
        # else: 
        #   print('нет фото')
      except Exception:
        proj_photo: 'No project photo'   
        # print(proj_photo)

      try: # АДРЕС
        proj_address = soup.find('div', class_='folder-description').find('h2').text.replace('Количество подъездов, ед', '')
        # print(proj_address)
      except Exception:
        proj_address: 'No project address' 

      try: # ПЛОЩАДЬ ЗДАНИЯ
        # proj_full_S = proj_data.find('div', class_='mr-5 flex-shrink-0').find_next('div').text
        proj_full_S = proj_data_6_obj[0].text.replace('Общая площадь, кв.м', '')
        if proj_full_S is None:
          proj_full_S = '-'
        # print(proj_full_S)
      except Exception:
        proj_full_S: 'No project full S'   

      try: # ПЛОЩАДЬ ЖИЛЫХ ПОМЕЩЕНИЙ
        proj_living_S = proj_data_6_obj[1].text.replace('Общая площадь жилых помещений, кв.м', '')
        if proj_living_S is None:
          proj_living_S = '-'
        # print(proj_living_S)
      except Exception:
        proj_living_S: 'No project living S'   

      try: # КОЛИЧЕСТВО ЭТАЖЕЙ
          proj_etages = proj_data_6_obj[2].text.replace('Количество этажей, ед.', '')
          if proj_etages is None:
            proj_etages = '-'
        # print(proj_etages)
      except Exception:
        proj_etages: 'No project etages'   
      
      try: # ГОД !!!
          proj_year = proj_data_6_obj[3].text.replace('Год ввода дома в эксплуатацию', '')
          if proj_year is None:
            proj_year = '-'
        # print(proj_year)
      except Exception:
        proj_year: 'No project year' 

      try: # КОЛИЧЕСТВО ПОДЪЕЗДОВ
          proj_podezd = proj_data_6_obj[4].text.replace('Количество подъездов, ед.', '')
          if proj_podezd is None:
            proj_podezd = '-'
        # print(proj_podezd)
      except Exception:
        proj_podezd: 'No project podezd'

      try: # КОЛИЧЕСТВО ЛИФТОВ
          proj_lifts = proj_data_6_obj[5].text.replace('Количество лифтов, ед.', '')
          if proj_lifts is None:
            proj_lifts:'-'
        # print(proj_lifts)
      except Exception:
        proj_lifts: 'No project lifts'
      
      houses.append({
        'addr': proj_address,
        'ph':proj_photo,
        'full_S':proj_full_S.strip(),
        'living_S':proj_living_S.strip(),
        'etages':proj_etages.strip(),
        'year':proj_year.strip(),
        'dodezd':proj_podezd.strip(),
        'lifts':proj_lifts.strip(),
        'url':proj_url 

      })
      print('я внутри 2го цикла')

    iteration_count -= 1 
    print(f'итерация #{item} завершена, осталось итераций #{iteration_count}')
    if iteration_count ==0:
      print("сбор данных завершён")

    time.sleep(random.randrange(3,5)) # "тише едешь, дальше будешь"
  with open ('data/project_data.json', 'a', encoding='utf-8') as file:  # 'a'  - значит что данные будут дополняться ,а не перезаписываться. т.е. старые данные не удаляются
    json.dump(houses, file, indent=4, ensure_ascii=False)
  # print(len(items))


# get_data('https://www.reformagkh.ru/search/houses?all=on&query=%D1%82%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C&page=1&limit=100')
get_data('https://www.reformagkh.ru/search/houses?all=on&query=%D1%82%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C&') # из урла вырезаем "page=1&limit=100" и вставляем его в верхний цикл

