# English2Language

This Python program is a web server that converts English into a variety of languages, including Spanish, French, Russian, German, and Italian!
-# Fun fact: This project was originally created for a Geometry Dash mod that translates everything into the user's chosen language. Stay tuned for its release!

## Warning:

**Before running the download script, edit it to include just the language models you want downloaded. Each one is around 200-300MB so choose wisely.**

## Installation:

### Option 1: Releases (Windows Only)

1. Go to the [Releases](/releases) tab
2. Select any version
3. Download the exe linked to that release

### Option 2: Development

1. Click on `Code`
2. Click `Download ZIP`
3. Unzip the `.zip` file
4. Open Command Prompt/Terminal on that folder
5. Enter the following command:
```
pip install -r requirements.txt
```

## Usage

### Option 1: EXE (Windows Only)

1. Open the `.exe` file downloaded from the releases tab
2. Read the [guide](#guide) below

### Option 2: Development

1. Open Command Prompt/Terminal on the project folder
2. Use the following [guide](#guide) to help you do what you want to do

## Guide

1. **Download / `py download.py`** - Downloads language models (select which ones you want downloaded by editing the download.py file)
2. **Migrate / `py manage.py migrate`** - Updates the database (not required for this project)
3. **Run / `py manage.py runserver`** - Starts the web server (`127.0.0.1:8000/translate` if running locally)