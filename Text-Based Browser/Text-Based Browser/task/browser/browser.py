import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import init

# write your code here
args = sys.argv

# Create directory
dirName = args[1]

try:
    # Create target Directory
    os.mkdir(dirName)
except FileExistsError:
    print('')


def get_data(url):
    return requests.get('https://' + url).content


while True:
    address_bar = input()
    if address_bar == 'exit':
        break
    # elif address_bar.replace('.', '_') not in web_list:
    #     print("Error: Incorrect URL")
    elif '.' in address_bar:
        contents = BeautifulSoup(get_data(address_bar), 'html.parser')
        final_address = address_bar.replace('.', '')
        file_name = dirName + '/' + final_address + '.txt'
        with open(file_name, 'a+') as f:
            for x in range(len(contents.findAll('a'))):
                f.write(contents.findAll('a')[x].get_text() + '\n')
                # print(contents.findAll('a')[x].get_text())
        with open(file_name, 'r') as d:
            print(d.read())
    else:
        print("Error: Incorrect URLs")