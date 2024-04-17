from pydub import AudioSegment
import os
from datetime import datetime
import logging

async def process_audio(file_path: str):
    try:
        #creates the path for the new file
        new_file_path = await create_file_name(file_path)
        
        #converts the file from the file path given as input and returns its new path output
        converted = await convert_to_wav(file_path,new_file_path)
        
        return converted
    except Exception as e:
        logging.error(f'Error processing audio: {str(e)}')

async def convert_to_wav(input: str,output: str):
    try:
        sound = AudioSegment.from_file(input, "ogg")
        sound = sound.set_frame_rate(16000)
        sound.export(output, format="wav")
        return output
    except Exception as e:
        logging.error(f'Error at converting to wav: {str(e)}')

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