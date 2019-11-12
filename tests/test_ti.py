
from translate_it.translate_it import get_parser, tran, cache

class TestTranslateIt:

    cache.clear()
    queries = [['你好'], ['装满'], ['word'], ['存档']]

    def call_translate(self, query):
        parser = get_parser()
        args = vars(parser.parse_args(query))
        return tran(args['words'])

    def test_translate_it(self):
        assert ['hello;hi'] == self.call_translate(self.queries[0])
        assert ['fill up'] == self.call_translate(self.queries[1])
        assert ['n. [语] 单词；话语；消息；诺言；命令',
                'vt. 用言辞表达',
                'n. (Word)人名；(英)沃德'] == self.call_translate(self.queries[2])
        assert ['file on file keep in the archivesgrandfather'] == self.call_translate(self.queries[3])


