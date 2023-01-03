import requests
import time
import json

def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(url)
    # print(response.text)
    return response.text


if __name__ == '__main__':
    print(time.time())
    while True:
        if int(time.time())%3600 == 0:
            results = get_data('http://dtkl.shmetro.com:9091/data/getLineTop5Data')
            start = time.strftime('%Y-%m-%d-%H-%M-%S')
            print(start)
            with open('./metro/%s.txt'%start, 'w', encoding='utf-8') as w:
                json.dump(results, w, ensure_ascii=False, indent=4)
            time.sleep(3500)
        else:
            pass