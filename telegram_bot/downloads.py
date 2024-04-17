from telegram import Update
import tempfile
import os
import uuid

async def download_audio(update: Update):
    audio_file = await update.message.effective_attachment.get_file()
    return await download_media(audio_file,update)

async def download_image(update:Update):
    image_file = await update.message.effective_attachment[-1].get_file()
    return await download_media(image_file,update)

async def download_media(file,update):
    temp_dir = tempfile.mkdtemp()
    file_extension = os.path.splitext(file.file_path)[1]
    file_path = os.path.join(temp_dir, f'{update.effective_user.id}_{str(uuid.uuid4())[:8]}{file_extension}')
    await file.download_to_drive(custom_path=file_path)
    return file_path