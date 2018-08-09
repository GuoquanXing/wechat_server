# -*- coding: utf-8 -*-
# filename: main_work.py
import web
from handle_work import Handle

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
