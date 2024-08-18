from pydub import AudioSegment
import os
from datetime import datetime
import logging

async def process_audio(file_path: str):
    new_file_path = await create_file_name(file_path)
    success = await convert_to_wav(file_path, new_file_path)
    
    if success:
        return new_file_path
    else:
        logging.error(f'Audio conversion failed for file: {file_path}')
        raise Exception("Audio conversion failed")

async def convert_to_wav(input: str,output: str):        
    sound = AudioSegment.from_file(input, "ogg")
    sound = sound.set_frame_rate(16000)
    sound.export(output, format="wav")
    
    return os.path.exists(output) and os.path.getsize(output) > 0

async def create_file_name(file_path: str):
    try:
        #get user id
        user_id = os.path.basename(file_path).split('_')[0]

        #get timestamp to use in the new name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        #create new file name
        new_file_name = f"audio_message_{user_id}_{timestamp}.wav"

        #create the file path
        user_audio_dir = os.path.join("media", "audios", str(user_id))
        os.makedirs(user_audio_dir, exist_ok=True)
        new_file_path = os.path.join(user_audio_dir, new_file_name)

        return new_file_path
    except Exception as e:
        logging.error(f'Error at creating file name for audio file: {str(e)}')