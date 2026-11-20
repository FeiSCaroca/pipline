from flask import Flask, request
from prometheus_client import start_http_server, Summary

app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/metrics')
def metrics():
    """
    Endpoint para proporcionar métricas.

    Retorna:
    str: Métricas en formato Prometheus.
    """
    return "custom_metric 1"

@app.route('/hello')
@REQUEST_TIME.time()
def hello():
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
