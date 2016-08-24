from flask import Markup


def money_formatter(value):
    value = int(value) if value is not None else 0
    return 'R${},00'.format(value)


def square_meters_formatter(value):
    value = int(value) if value is not None else 0
    return '{}m²'.format(int(value))


def link_formatter(url, text):
    return Markup(
        "<a href='{}'> {} </a>".format(url, text)
    ) if url is not None else ' - '


def liter_formatter(value):
    value = int(value) if value is not None else 0
    return '{}L'.format(value)
