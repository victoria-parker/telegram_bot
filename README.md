# AudioFaceBot

## Introduction

During a project assignment, I was tasked with developing a Telegram bot with the following functionalities:

1. Save audio messages from dialogues to a database by user IDs, converting them to WAV format with a sampling rate of 16kHz.

2. Determine whether there is a face in the photos being sent and save only those with faces detected.

## Usage

To use this bot, it's necessary to create one on Telegram using BotFather and set up a MongoDB database. I set up mine on MongoDB Atlas.

## Libraries Used

- `python-telegram-bot`: Used for interacting with the Telegram messaging platform.
- `pydub`: Used for audio processing tasks such as converting audio files to WAV format.
- `face_recognition`: Used for face detection in images.

### Notes about Libraries

To use pydub, it was necessary to download ffmpeg. For face_recognition, I had to install dlib and Visual Studio with C++ components.

## The process
For developing this project, I first investigated each part I needed to know to be able to do it. So first, I searched for information and read the documentation for connecting to Telegram and creating the Telegram bot. Then I investigated how to process the audio, and after that, how to process the image. I played around with each task, and then joined the puzzle.

## Improvements
I am sure there are a lot of improvements to make. Some of the ones I could mention include: 
- Improving the error logging and implementing a notification system (such as via email) for when an error occurs. 
- Refactoring repetitive code, such as the create file name function that is duplicated in both audio and image processing files. 
- Enhancing user interaction during dialogue with the bot.
- Addressing the limitation of the face recognition library in recognizing side faces; exploring potential workarounds for this issue would be beneficial.

