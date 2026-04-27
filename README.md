# Smart Assistant (Voice Commands)

A simple Python voice assistant project that responds to basic commands such as getting time, opening websites, and launching local applications.

## Features

- Speech command recognition
- Text-to-speech response
- Commands: time, open Google, open YouTube, open notepad/calculator, exit
- Text input fallback when microphone is unavailable

## Project Structure

```
smart-assistant-voice-commands/
  app.py
  requirements.txt
  README.md
```

## Installation

```bash
pip install -r requirements.txt
```

Optional for microphone usage:

- Install PyAudio according to your OS

## Run

```bash
python app.py
```

## Learning Outcomes

- Voice I/O integration
- Command parsing logic
- Cross-platform app launch basics
