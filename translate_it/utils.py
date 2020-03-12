def printf(result):
    print('\033[1;44m发音\033[0m')
    for phonetic in result.get('pronounce', []):
        print(phonetic[0], phonetic[1], end='\t')
    print('')

    print('\033[1;44m网络释义\033[0m')
    for content in result.get('contents', ''):
        print(content)

    print(result.get('additionals', ''))
    examples = result.get('examples', [])
    print('\033[1;44m双语例句\033[0m')
    for index, example in enumerate(examples):
        print('{}. {}'.format(index + 1, example[0]))
        print(example[1])
