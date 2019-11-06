
from translate_it.translate_it import get_parser, tran

class TestTranslateIt:

    queries = [['你好'], ['装满'], ['word']]

    def call_translate(self, query):
        parser = get_parser()
        args = vars(parser.parse_args(query))
        return tran(args['words'])

    def test_translate_it(self):
        assert ['hello;hi'] == self.call_translate(self.queries[0])
        assert ['fillup'] == self.call_translate(self.queries[1])
        assert ['n.[语]单词；话语；消息；诺言；命令',
                'vt.用言辞表达',
                'n.(Word)人名；(英)沃德'] == self.call_translate(self.queries[2])


