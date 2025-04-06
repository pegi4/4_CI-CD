from flask import Flask, Response
import cv2 as cv
from datetime import datetime
import numpy as np

app = Flask(__name__)

def generate_frame():
    while True:
        DEFAULT_IMAGE = "sample.jpg"
        default_img = cv.imread(DEFAULT_IMAGE)
        if default_img is None:
            default_img = np.zeros((480, 640, 3), dtype=np.uint8)
            cv.putText(default_img, "Default image not found", (10, 30), 
                        cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv.putText(default_img, timestamp, (150, 150), cv.FONT_HERSHEY_SIMPLEX, 1, 
                    (0, 0, 255), 3, cv.LINE_AA)

        ret, buffer = cv.imencode('sample.jpg', default_img)
        if ret:
            return buffer.tobytes()
        return None

@app.route('/image')
def get_image():
    frame_bytes = generate_frame()
    if frame_bytes:
        return Response(frame_bytes, mimetype='image/jpeg')
    return "Error generating image", 500 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9860)