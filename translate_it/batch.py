import re
import time
import random
import json

from translate_it.dictionaries import translate


def import_words(txt_path):
    with open(txt_path, 'rb+') as f:
        lines = f.readlines()
    results = []
    count = 0
    for line in lines:
        s = r'(\w+?\b)\s?(\[\w+?\b\])?\s(\w+?\.)(.*)'
        word = re.findall(s, line.decode())
        if len(word) > 0:
            word = word[0]
        else:
            continue

        try:

            result = translate(word[0])
            result.update({'word': word[0]})
            results.append(result)
        except Exception as e:
            print(e, word[0])
            with open('error.log', 'a+') as f:
                f.write(word[0])
                f.write()
            continue

        print(word[0], 'end.')
        count += 1
        time.sleep(random.randint(1, 4) * 0.3)

        if count % 100 == 0:
            time.sleep(100)

    with open('words.json', 'w+') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)


def save(result):
    with open('words1.json', 'a+') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
