import face_recognition
import cv2

async def image_face_detector(file_path: str):
    image = cv2.imread(file_path)
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        return True
    else:
        return False