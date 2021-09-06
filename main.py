import requests, json, os, cloudscraper, re
from bs4 import BeautifulSoup
from colorama import Fore

def logo():
    return f''' {Fore.MAGENTA}
        ████████╗████████╗███████╗
        ╚══██╔══╝╚══██╔══╝██╔════╝
           ██║      ██║   ███████╗
           ██║      ██║   ╚════██║
           ██║      ██║   ███████║
           ╚═╝      ╚═╝   ╚══════╝
     {Fore.MAGENTA}Creators: {Fore.GREEN}JamesMagellan x IRIS
'''
with open('config.json') as f:
    config = json.load(f)

stripe_mid = config.get('ict(__stripe_mid')
tripe_sid = config.get('__stripe_sid')
PHPSESSID = config.get('PHPSESSID')
remember = config.get('remember')


def tt(cmd):
    scraper = cloudscraper.create_scraper()
    url=f'https://thatsthem.com/email/{cmd}'
    coookies = dict(__stripe_mid=f'{stripe_mid}',
        __stripe_sid=f'{tripe_sid}',
        PHPSESSID=f'{PHPSESSID}',
        remember=f'{remember}')
    path=scraper.get(url, cookies=coookies).text
    soup = BeautifulSoup(path, 'lxml')
    print (f'{Fore.WHITE}Email         : {Fore.LIGHTMAGENTA_EX}{cmd}\n{Fore.WHITE}Data          : {Fore.LIGHTMAGENTA_EX}')
    for namle in soup.findAll('a', {'href': lambda x: x and '/name/' in x}):
        print(f'{Fore.WHITE}Name          : {Fore.LIGHTMAGENTA_EX}'+ namle.text.strip().replace('\n',' ')+ '\n')
    for house in soup.findAll('a', {'href': lambda x: x and '/address/' in x}):
        print(f'{Fore.WHITE}Address       : {Fore.LIGHTMAGENTA_EX}'+ house.text.strip().replace('\n',' ')+ '\n')
    for phone in soup.findAll('a', {'href': lambda x: x and '/phone/' in x}):
        print(f'{Fore.WHITE}Phone Number  : {Fore.LIGHTMAGENTA_EX}'+ phone.text.strip().replace('\n',' ')+ '\n')
    for ipele in soup.findAll('a', {'href': lambda x: x and '/ip/' in x}):
        print(f'{Fore.WHITE}IP address    : {Fore.LIGHTMAGENTA_EX}'+ ipele.text.strip().replace('\n',' ')+ '\n')

def main():
    print(logo())
    cmd = input(f'{Fore.GREEN}~>{Fore.WHITE} ')
    tt(cmd)
main()