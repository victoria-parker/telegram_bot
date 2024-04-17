import face_recognition
import cv2
import os
from datetime import datetime
import shutil

async def process_image(file_path: str):
    detection_face = await image_face_detector(file_path)
    if detection_face:
        destination_path = await create_file_name(file_path)
        shutil.copyfile(file_path, destination_path)
        return True
    else:
        return False

async def image_face_detector(file_path: str):
    image = cv2.imread(file_path)
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        return True
    else:
        return False
    
async def create_file_name(file_path: str):
    #get user id
    user_id = os.path.basename(file_path).split('_')[0]
    
    #get timestamp to use in the new name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    #get file extention
    file_extension = os.path.splitext(file_path)[1]

    #create new file name
    new_file_name = f"image_message_{user_id}_{timestamp}{file_extension}"

    #create the file path
    user_audio_dir = os.path.join("media", "images", str(user_id))
    os.makedirs(user_audio_dir, exist_ok=True)
    new_file_path = os.path.join(user_audio_dir, new_file_name)

    return new_file_path