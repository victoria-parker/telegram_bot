from pymongo import MongoClient
from config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client.get_database('telegram_bot')
audios = db.get_collection('audios')


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
        print(f'Error al almacenar audio en la base de datos: {str(e)}')
    