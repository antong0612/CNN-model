# Import socket module
import socket
import cv2
import numpy as np
from tensorflow.keras.models import load_model

global sendBack_angle, sendBack_Speed, current_speed, current_angle
sendBack_angle = 0
sendBack_Speed = 0
current_speed = 0
current_angle = 0
model = load_model('model.h5')
model1 = load_model('model1.h5')

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    crop_img = img[200:, :]
    img = crop_img
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
PORT = 54321
# connect to the server on local computer
s.connect(('127.0.0.1', PORT))


def Control(angle, speed):
    global sendBack_angle, sendBack_Speed
    sendBack_angle = angle
    sendBack_Speed = speed


if __name__ == "__main__":
    try:
        steering = 0
        while True:

            """
            - Chương trình đưa cho bạn 1 giá trị đầu vào:
                * image: hình ảnh trả về từ xe
                * current_speed: vận tốc hiện tại của xe
                * current_angle: góc bẻ lái hiện tại của xe

            - Bạn phải dựa vào giá trị đầu vào này để tính toán và
            gán lại góc lái và tốc độ xe vào 2 biến:
                * Biến điều khiển: sendBack_angle, sendBack_Speed
                Trong đó:
                    + sendBack_angle (góc điều khiển): [-25, 25]
                        NOTE: ( âm là góc trái, dương là góc phải)

                    + sendBack_Speed (tốc độ điều khiển): [-150, 150]
                        NOTE: (âm là lùi, dương là tiến)
            """

            message_getState = bytes("0", "utf-8")
            s.sendall(message_getState)
            state_date = s.recv(100)

            try:
                current_speed, current_angle = state_date.decode(
                    "utf-8"
                    ).split(' ')
            except Exception as er:
                print(er)
                pass

            message = bytes(f"1 {sendBack_angle} {sendBack_Speed}", "utf-8")
            s.sendall(message)
            data = s.recv(100000)

            try:
                image = cv2.imdecode(
                    np.frombuffer(
                        data,
                        np.uint8
                        ), -1
                    )
                image_copy = preProcess(image)
                image_copy = np.array([image_copy])
                steering = float(model.predict(image_copy)) 
                speed = float(model.predict(image_copy)) 
                print(steering)
                print(current_speed, current_angle)
                print(image.shape)
                # your process here
                cv2.imshow("IMG", image)
                cv2.waitKey(1)
                
                Control(steering, speed)

            except Exception as er:
                print(er)
                pass

    finally:
        print('closing socket')
        s.close()