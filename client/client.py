from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get('http://server:9860/image', timeout=5)
        if response.status_code == 200:
            image_path = os.path.join('static', 'temp_image.jpg')
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return render_template('index.html')
        else:
            return "Error retrieving image", 500
    except requests.RequestException as e:
        return f"Server not accessible: {str(e)}", 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9861)