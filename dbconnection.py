from pymongo import MongoClient
from config import MONGODB_URI
import logging

client = MongoClient(MONGODB_URI)
db = client.get_database('telegram_bot')
audios = db.get_collection('audios')
images = db.get_collection('images')


def store_audio(user_id:str,file_name:str):
    try:
        user = audios.find_one({"user_id": int(user_id)})

        if user:
            audio_messages = user.get("audio_messages",[])
            audio_messages.append(file_name)
            audios.update_one({"user_id": user_id}, {"$set": {"audio_messages": audio_messages}})
        else:
            audios.insert_one({"user_id": user_id, "audio_messages": [file_name]})
    
    except Exception as e:
        logging.error(f'Error at store audio in database: {str(e)}')

def store_image(user_id:str,file_name:str):
    try:
        user = images.find_one({"user_id": int(user_id)})

        if user:
            image_messages = user.get("image_messages",[])
            image_messages.append(file_name)
            images.update_one({"user_id": user_id}, {"$set": {"image_messages": image_messages}})
        else:
            images.insert_one({"user_id": user_id, "image_messages": [file_name]})
    
    except Exception as e:     
        logging.error(f'Error at store image in database: {str(e)}')
    