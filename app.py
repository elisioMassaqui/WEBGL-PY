from flask import Flask, render_template
import WEBGL.webgl_server as webgl_server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    try:
        # Portas predefinidas
        flask_port = 4500
        webgl_port = 3800

        # Diretório dos arquivos WebGL
        webgl_directory = 'WEBGL/webgl_files'

        # Inicia o servidor WebGL usando o módulo
        webgl_server.start_webgl_server(webgl_port, webgl_directory)

        # Inicia o aplicativo Flask
        app.run(port=flask_port)

    except Exception as e:
        print('Error:', e)
