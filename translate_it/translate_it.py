# -*- coding: utf-8 -*-

#     __                        __      __             _ __
#    / /__________ _____  _____/ /___ _/ /____        (_) /_
#   / __/ ___/ __ `/ __ \/ ___/ / __ `/ __/ _ \______/ / __/
#  / /_/ /  / /_/ / / / (__  ) / /_/ / /_/  __/_____/ / /_
#  \__/_/   \__,_/_/ /_/____/_/\__,_/\__/\___/     /_/\__/

from argparse import ArgumentParser

from translate_it.dictionaries import translate
from translate_it.batch import import_words
from translate_it.config import Config


def get_parser():

    parser = ArgumentParser(description='To help you translate')
    parser.add_argument('words', metavar='WORDS', type=str,
                        nargs='*', help='the words to translate')

    parser.add_argument('-s', '--save', dest='save',
                        action='store_true', default=False)
    parser.add_argument('-u', '--user', dest='user', type=str)
    parser.add_argument('-p', '--password',
                        dest='password', type=str)
    parser.add_argument('-c', '--config', dest='config', type=str)
    parser.add_argument('-i', '--import', dest='import')
    parser.add_argument('-e', '--export', dest='export',
                        action='store_true', default=False)

    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    config = Config()

    if args['user']:
        config.update('auth', 'user', args['user'])
    if args['password']:
        config.update('auth', 'password', args['password'])

    if args['import']:
        import_words(args['import'])

    if args['words']:
        translate(args['words'])


if __name__ == '__main__':
    command_line_runner()
