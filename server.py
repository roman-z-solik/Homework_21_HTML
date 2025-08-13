from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

hostName = "localhost"
serverPort = 10553


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open('contacts.html', 'rb') as file:
            page_content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page_content)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        received_data = json.loads(post_data.decode('utf-8'))

        print("Полученные данные:", received_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response_body = {"message": "Данные получены"}
        self.wfile.write(json.dumps(response_body).encode('utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен по адресу http://{hostName}:{serverPort}/")

    try:
         webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен.")
