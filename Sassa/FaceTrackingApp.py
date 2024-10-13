!pip install opencv-python imgbeddings psycopg2-binary

import cv2

class CameraApp:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        
    def run(self):
        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Failed to grab frame")
                break
            
            cv2.imshow('Camera', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = CameraApp()
    app.run()
