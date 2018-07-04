import requests
import pandas as pd


def contentful_check(url):
    url = url if url.startswith('http://') else 'http://'+url
    data = requests.get(url)
    if data.text.__contains__('ctfassets') or data.text.__contains__('contentful.com'):
        return True
    else:
        return False

def parse_csv(csv_path):
    url_list = pd.read_csv(csv_path, sep=',')
    final_output = url_list.copy()
    final_output['has_contentful'] = False
    for website in url_list['URL']:
        if contentful_check(website):
            final_output.has_contentful[final_output['URL']==website] = True
    '''FINAL RESULTS'''
    final_output.to_csv('contentful_check.csv', index=False)

parse_csv(csv_path = 'url_list.csv')
