from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import re
import uuid

# Define el directorio donde se guardarán los archivos recibidos
UPLOAD_DIR = 'C:\\Users\\Desarrollo\\Documents\\uploads'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.handle_upload()

    def do_PUT(self):
        self.handle_upload()

    def handle_upload(self):
        # Verifica que la ruta sea /upload
       
            # Obtiene la longitud del contenido
            #pp
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            # Generar un identificador único (GUID)
            unique_id = str(uuid.uuid4())

        # Buscar el nombre del archivo en el cuerpo de la solicitud
            filename_match = re.search(r'filename=("[^"]+")', post_data.decode('utf-8'))
            if filename_match:
                filename = filename_match.group(1).strip('"')
                # Limpiar el nombre del archivo
                filename = "".join(c for c in filename if c.isalnum() or c in ('-', '_', '.', '-'))

            # Agregar GUID al nombre del archivo
            filename_with_guid = f'{unique_id}_{filename}'

            with open(os.path.join(UPLOAD_DIR, f'archivo_{filename_with_guid}.txt'), 'wb') as f:
                f.write(post_data)

            # Envía una respuesta al cliente
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Archivo recibido exitosamente.')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    # Configura el servidor para escuchar en el puerto especificado
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor en ejecución en el puerto {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    # Inicia el servidor
    run()