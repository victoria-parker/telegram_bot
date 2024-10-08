import face_recognition
import cv2
import os
from datetime import datetime
import shutil
import logging

async def process_image(file_path: str):
    try:
        detection_face = await image_face_detector(file_path)
        if detection_face:
            destination_path = await create_file_name(file_path)
            shutil.copyfile(file_path, destination_path)
            return destination_path
        else:
            return False
    except Exception as e:
        logging.error(f'Error processing image: {str(e)}')
        raise Exception("Error at process image")

async def image_face_detector(file_path: str):
        image = cv2.imread(file_path)
        if image is None:
            logging.error(f'Failed to read image file: {file_path}')
            raise RuntimeError(f'Failed to read image file: {file_path}')

        face_locations = face_recognition.face_locations(image)
        if face_locations:
            return True
        else:
            return False
    
async def create_file_name(file_path: str):
    try:
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
    except Exception as e:
        logging.error(f'Error at create file name for image: {str(e)}')
        raise Exception("Failed to create file name")