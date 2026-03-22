import http.server
import socketserver

PORT = 8000


class ContactsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            with open('contacts.html', 'r', encoding='utf-8') as f:
                html = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'<h1>404 - contacts.html not found</h1>')


# Используем type: ignore для подавления предупреждения
httpd = socketserver.TCPServer(("", PORT), ContactsHandler)  # type: ignore

print(f"Сервер запущен на http://localhost:{PORT}")
print("На любой GET-запрос возвращается страница Контакты")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен")
    httpd.server_close()
    