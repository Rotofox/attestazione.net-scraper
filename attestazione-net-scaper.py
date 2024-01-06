from bs4 import BeautifulSoup
import requests, re, csv

data = []

# Will reuse for getting more information on each item
base_url = "https://attestazione.net"
# URL trail for tabular view
tabular_url_trail = "/SoaEngine?Page="
# Page number, it will increase as we change page by page
pageNumber = 1
# URL trail for details view
details_url_trail = "/SoaEngine/Dettaglio\?piva="

def get_item_link_trails(url):
  table_page = requests.get(url)
  soup = BeautifulSoup(table_page.text, "html.parser")
  links = soup.find_all(href=re.compile(f"{details_url_trail}"))
  href_values = [tag.get('href') for tag in links]
  return href_values

def construct_item_links(link_trails):
  links = []
  for trail in link_trails:
    links.append("%s%s"%(base_url, trail))
  return links

def get_item_details(url, headers):
  item_links = construct_item_links(get_item_link_trails(url))
  for link in item_links:
    item_dict = {}
    list_of_dicts = []
    page = requests.get(link, headers)
    soup = BeautifulSoup(page.text, "html.parser")
    dt_list = soup.find_all("dt")
    keys = [key.text.strip() for key in dt_list]
    dd_list = soup.find_all("dd")
    values = [value.text.strip() for value in dd_list]
    list_of_dicts.extend([{"{}".format(key): "{}".format(value)} for key, value in zip(keys, values)])
    for d in list_of_dicts:
      item_dict.update(d)
    data.append(item_dict)

def construct_csv_from_data(data):
  with open('output.csv', 'w', newline='') as csvfile:
   fieldnames = list(data[0].keys())
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   writer.writeheader()
   for dict in data:
    writer.writerow(dict)

def get_data_from_n_pages(start_page, end_page):
  for n in range(start_page, end_page + 1):
    url = "%s%s%s"%(base_url, tabular_url_trail, n)
    headers = {"Referer":url}
    get_item_details(url, headers)
  construct_csv_from_data(data)