"""
Testing spaCy lib with Russian language
"""

import json
from spacy.lang.ru import Russian


def main():
    _fn = 'test_ru.json'
    try:
        with open(_fn, 'r', encoding='utf-8') as _fd:
            _buf = json.load(_fd)
    except IOError as _err:
        print(_err)
        return
    # _text = json.dumps(_buf)
    _text = str(_buf)
    print(_text)
    input("Press ENTER for continue...")
    nlp_obj = Russian()
    _doc = nlp_obj(_text)
    for _token in _doc:
        print(_token.text)
    input("Press ENTER for continue...")


if __name__ == '__main__':
    main()
