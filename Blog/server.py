# coding: utf8
# version 0.00001

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
#import MySQL module
import mysql.connector

from tornado.options import define, options
define("port", default=9090, help="run on the given port", type=int)

#connect to SQL base
conn = mysql.connector.connect(database="PySQL", host="localhost",user="Bloger",
    password="NoPass2140")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/about", AboutHandler),
            (r"/faq", FaqHandler),
            (r"/test", TestHandler),
            (r"/blog", BlogHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Tornados главная",
            header_text = "Мы рады вам",
        )

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "about.html",
             page_title = "О нас",
             header_text = "Мы работаем с 2008 года",
        )

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Fast answers and questions")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "test.html",
            page_title = "Test",
            header_text = "Проверка функционала",
        )      
# read some date from SQL
cursor = conn.cursor()
cursor.execute("SELECT * FROM Posts");
from_blog = cursor.fetchall()


class BlogHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "blog.html",
            page_title = "Наш блог",
            header_text = "Заметки и не только",
            blog_text = from_blog
        )

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
