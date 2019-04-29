import urllib.request
import urllib.parse
import re


def get_ganres_list():
    """
    @brief      get list of ganres from kinopoisk.ru

    @return     The ganres list.
    """
    with urllib.request.urlopen('https://www.kinopoisk.ru/top/lists/') as f:
        text = f.read().decode("utf8")
        start = text.index("list_main js-rum-hero")
        stop = text.index(r'</ul>', start)
        text = text[start + 28:stop]
        text = re.sub(r'\ *<[/]*li.*\n', '', text)
        text = re.sub(r'\ *<b.*\n', '', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'<div[^>]*>', '', text).split(r'</div>')
        ar = []
        for el in text:
            i = el.find('>')
            ar.append((el[10:i - 1], el[i + 1:-4]))

        return ar

sort_type = {          
            "по порядку" : "order",
            "по году" : "year",
            "по названию" : "name",
            "по оригинальному названию" : "oname",
            "по рейтингу КиноПоиска" : "rating",
            "по рейтингу IMDb" : "rating_imdb",
            "по количеству оценок" : "votes",
            "по времени" : "runtime"
        }          

data = {
        "level": "60",
        "list": "5",
        "_filtr": "all",
        "_sort": sort_type["по порядку"],
        "page": 2,
        "_ord": ""
        }

  


data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request('https://www.kinopoisk.ru/top/lists/5/page/2', data, method="POST")

with urllib.request.urlopen(req) as f:
    text = f.read().decode("utf8")
    start = text.index("table id=\"itemList")
    stop = text.index('/table', start)
    text = text[start: stop]
    print(text)
