from sys import argv
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

def create_directory(save_dir) -> None:

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    pass


def url_to_filename(url : str) -> str:
    return url.split('.')[0].lower()


def validate_url(url : str) -> str:

    if '.' not in url:
        return 'Invalid URL error - web address should contain a dot'

    else:
        return 'True'

def prepare_address(url):

    if url.lower().startswith('http://') or url.lower().startswith('https://'):
        return url

    return 'https://' + url

def parse_site(site):
    soup = BeautifulSoup(site.content, 'html.parser')

    for script in soup.find_all('script'):
        script.decompose()

    links = soup.find_all('a')

    if links:
        for link in links :
            link.text.replace(link.text,('{Fore.BLUE}' + link.text + '{Fore.RESET}'))

    return  soup


# write your code here
if __name__ == '__main__':

    #initial config
    save_dir = argv[1] or ''
    create_directory(save_dir)
    history = deque()
    init()

    #browsing starts hehre
    address = input('>')

    while address != 'exit':

        if address == 'back':
            if len(history)>1:
                history.pop()
                address = history.pop()
        else:
            history.append(address)

        path = os.path.join(save_dir, url_to_filename(address))





        if os.path.exists(path):
            with open(path,'r') as website:
                print(website.read())
        else:
            if validate_url(address) == 'True':
                r = requests.get(prepare_address(address))
                parsed_r = parse_site(r)
                print(f'{Fore.BLUE} {parsed_r.get_text()}')

                with open(path,'w') as dump_file:
                    dump_file.write(parsed_r.get_text()
                                   )

            else:
                print(validate_url(address))


        address = input('>')
