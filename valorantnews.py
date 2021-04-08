import json
import os.path
import requests

def news():
    languages = [
        'ar-ae',
        'de-de',
        'en-us',
        'en-gb',
        'es-es',
        'es-mx',
        'fr-fr',
        'id-id',
        'it-it',
        'ja-jp',
        'ko-kr',
        'pl-pl',
        'pt-br',
        'ru-ru',
        'th-th',
        'tr-tr',
        'vi-vn',
        'zh-tw'
    ]
    
    # URL structure
    url_base = 'https://playvalorant.com/'
    url_prefix = 'page-data/'
    url_suffix = '/news/page-data.json'
    output = []
    
    for language in languages:
        # Request and newest news details
        news_request = requests.get(url_base + url_prefix + language + url_suffix)
        if news_request.status_code == 200:
            news_content = json.loads(news_request.text)
            news_title = news_content['result']['data']['allContentstackArticles']['nodes'][0]['title']
            news_description = news_content['result']['data']['allContentstackArticles']['nodes'][0]['description']
            news_banner = news_content['result']['data']['allContentstackArticles']['nodes'][0]['banner']['url']
            news_url = url_base + language + news_content['result']['data']['allContentstackArticles']['nodes'][0]['url']['url']
            news_hash = news_content['result']['data']['allContentstackArticles']['nodes'][0]['id']
            news_external_link = news_content['result']['data']['allContentstackArticles']['nodes'][0]['external_link']
            
            if os.path.isfile(language + '.txt'):
                news_file = open(language + '.txt', 'r')
                news_hash_old = news_file.read()
                news_file.close()
            else:
                news_hash_old = ''

            if news_hash != news_hash_old:
                if news_external_link == '':
                    # Write hash in a *.TXT file
                    news_file = open(language + '.txt', 'w')
                    news_file.write(news_hash)
                    news_file.close()
            
                    output.append([news_url, news_title, news_description, news_banner, language])
                    print('VALORANT News: New article for ' + str(language) + ': ' + str(news_url))
                else:
                    # Write hash in a *.TXT file
                    news_file = open(language + '.txt', 'w')
                    news_file.write(news_hash)
                    news_file.close()
            
                    output.append([news_external_link, news_title, news_description, news_banner, language])
                    print('VALORANT News: New article for ' + str(language) + ': ' + str(news_external_link))
    return output

if __name__ == '__main__':
    news()