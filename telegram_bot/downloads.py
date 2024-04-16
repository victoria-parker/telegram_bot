from telegram import Update
import tempfile
import os
import uuid

async def download_audio(update: Update):
    temp_dir = tempfile.mkdtemp()
    audio_file = await update.message.effective_attachment.get_file()
    file_path = os.path.join(temp_dir, f'{update.effective_user.id}_{str(uuid.uuid4())[:8]}.ogg')
    await audio_file.download_to_drive(custom_path=file_path)
    return file_path