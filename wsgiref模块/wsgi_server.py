# -*- coding: utf-8 -*-
# __author__ = "Anatkh"
# date: 2018/12/13

from wsgiref.simple_server import make_server


def application(environ, start_response):
    """
    回调函数，当客户端链接时调用该函数
    :param environ: 按着http协议解析数据
    :param start_response: 按着http协议组装数据
    :return:
    """
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, World!</h1>']


if __name__ == '__main__':
    httpd = make_server('', 8080, application)  # 1:IP/2:端口/3:回调函数，当用户链接就调用回调函数

    print('Serving HTTP on port 8000...')
    # 等待用户链接，开始监听HTTP请求:conn,addr = socket.accept()
    httpd.serve_forever()