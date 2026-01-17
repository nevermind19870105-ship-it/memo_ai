from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # メンテナンス中として503エラーを返す
        self.send_response(503)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("現在メンテナンス中です (Under Maintenance)".encode())
        return