import re


def parse(response):
    contents_dom = response.xpath('//div[@id="results-contents"]')[0]
    trans_container = contents_dom.xpath(
        '//div[@class="trans-container"]')
    if not trans_container:
        return {}

    # 发音
    pronounce = []
    pronounce_dom = response.xpath('//span[@class="pronounce"]')
    for item in pronounce_dom:
        pronounce.append([item.text.strip(), item.xpath('string(span)')])

    # 翻译
    ul_dom = trans_container[0].xpath('ul')
    additional_dom = trans_container[0].xpath('p/text()')
    contents = []
    if ul_dom:
        contents = ul_dom[0].xpath('li/text()')
        if len(contents) > 0:
            contents = [content for content in contents
                        if content.strip()]
        else:
            container_dom = ul_dom[0].xpath('p')
            if len(container_dom) == 1:
                klass = container_dom[0].xpath('string(span[1])')
                value = '; '.join(container_dom[0].xpath('span/a/text()'))
                if klass.strip() == value.strip():
                    contents.append(value)
                else:
                    contents.append('{} {}'.format(klass, value))

            else:
                for word in ul_dom[0].xpath('p'):
                    klass = word.xpath('string(span[1])')
                    value = word.xpath('string(span[2]/a)')
                    contents.append('{} {}'.format(klass, value))

    # 拓展
    if additional_dom:
        additional = re.sub(r'\s{1,}', ' ', additional_dom[0])
    else:
        additional = ''

    # 例句
    examples = []
    bilingual_dom = response.xpath('//div[@id="bilingual"]')
    if bilingual_dom:
        examples_dom = bilingual_dom[0].xpath('ul/li')
        for example in examples_dom:
            ex1 = example.xpath('p[1]/span/text() | p[1]/span/b/text()')
            ex2 = example.xpath('p[2]/span/text() | p[2]/span/b/text()')
            examples.append([''.join(ex1), ''.join(ex2)])

    return {
        'pronounce': pronounce,
        'contents': [re.sub(r'\s{2,}?', '', content).strip()
                     for content in contents],
        'additionals': additional,
        'examples': examples
    }
