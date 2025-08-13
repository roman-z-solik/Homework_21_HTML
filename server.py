import json

# import os
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):
    """Специализированный обработчик HTTP-запросов, основанный на классе
    BaseHTTPRequestHandler.
    Методы:
    do_GET(): обрабатывает GET-запросы клиента, отправляя HTML-страницу.
    do_POST(): обрабатывает POST-запросы клиента, принимает данные в формате
    JSON и возвращает ответ."""

    def do_GET(self):
        with open("contacts.html", "rb") as file:
            page_content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_content)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        received_data = json.loads(post_data.decode("utf-8"))

        print("Полученные данные:", received_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_body = {"message": "Данные получены"}
        self.wfile.write(json.dumps(response_body).encode("utf-8"))


if __name__ == "__main__":

    """
    Основной блок исполнения скрипта, который запускает HTTP-сервер.
    Действия: 1. Создается экземпляр HTTPServer с указанным именем хоста и номером порта.
    2. Сообщается о старте сервера.
    3. Сервер запускается в бесконечный цикл ожидания запросов.
    4. По нажатию комбинации клавиш Ctrl+C сервер корректно закрывается.
    """

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен по адресу http://{hostName}:{serverPort}/")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
