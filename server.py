from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREFIX = "/calculadora-tubular"

class CalculatorHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean_path = path.split("?", 1)[0].split("#", 1)[0]
        if clean_path.startswith(PREFIX):
            clean_path = clean_path[len(PREFIX):] or "/"
        original_path = self.path
        self.path = clean_path
        translated = super().translate_path(clean_path)
        self.path = original_path
        return translated

if __name__ == "__main__":
    import os
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), CalculatorHandler)
    print("Calculadora disponível em http://127.0.0.1:8000/calculadora-tubular/")
    server.serve_forever()
