import sys
from flask import Flask, render_template
from http.server import SimpleHTTPRequestHandler, HTTPServer
from threading import Thread
import os

class GzipRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.gz'):
            self.send_header('Content-Encoding', 'gzip')
        super().end_headers()

    def do_GET(self):
        path = self.translate_path(self.path)
        if path.endswith('.js.gz'):
            with open(path, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/javascript')
                self.end_headers()
                self.wfile.write(content)
        elif path.endswith('.wasm.gz'):
            with open(path, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/wasm')
                self.end_headers()
                self.wfile.write(content)
        elif path.endswith('.gz'):
            with open(path, 'rb') as f:
                content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', self.guess_type(path))
                self.end_headers()
                self.wfile.write(content)
        else:
            super().do_GET()

def serve_webgl(port: int):
    os.chdir('webgl_files')  # Mude para o diretório correto
    httpd = HTTPServer(('localhost', port), GzipRequestHandler)
    print(f"Serving WebGL at http://localhost:{port}")
    httpd.serve_forever()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print(f'usage: {sys.argv[0]} [FLASK_PORT] [WEBGL_PORT]')
        flask_port = int(sys.argv[1])
        webgl_port = int(sys.argv[2])

        # Inicia o servidor WebGL em uma thread separada
        webgl_thread = Thread(target=serve_webgl, args=(webgl_port,))
        webgl_thread.start()

        # Inicia o aplicativo Flask
        app.run(port=flask_port)

    except Exception as e:
        print('Error:', e)
