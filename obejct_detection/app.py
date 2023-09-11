from flask import Flask, Response, render_template
import cv2
from image_detector import object_detection
import mediapipe as mp


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/detection_page')
def detection_page():
    return render_template('object_detection.html')



@app.route('/video_feed')
def video_feed():
    return Response(object_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')







if __name__ == '__main__':
    app.run()
