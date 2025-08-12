from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_server():
    server_address = ('', 8000)
    serv_addr = server_address[1]
    handler_class = SimpleHTTPRequestHandler
    with HTTPServer(server_address, handler_class) as httpd:
        print(f'Сервер запущен на локальном компьютере. Адрес порта {serv_addr}')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()

if __name__ == '__main__':
    run_server()