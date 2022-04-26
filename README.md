# Simple speech to text recognition script with file output using Vosk api.

Great alternative to Pocketsphinx; Created by the developers of Pocketsphinx.

Prerequisets:
  - pip install vosk - https://alphacephei.com/vosk/
  - pip install speech_recognition - https://pypi.org/project/speech-recognition-fork/

* try pip3 if pip gives problems.

# Brief descriptions: 

# Vosk Module
** Below text copied from Vosk Website **

# Vosk is a speech recognition toolkit. The best things in Vosk are:
#- Supports 20+ languages and dialects - English, Indian English, German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese, Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino, Ukrainian, Kazakh, Swedish, Japanese, Esperanto, Hindi, Czech. More to come.
- Works offline, even on lightweight devices - Raspberry Pi, Android, iOS
- Installs with simple pip3 install vosk
- Portable per-language models are only 50Mb each, but there are much bigger server models available.
- Provides streaming API for the best user experience (unlike popular speech-recognition python packages)
- There are bindings for different programming languages, too - java/csharp/javascript etc.
- Allows quick reconfiguration of vocabulary for best accuracy.
- Supports speaker identification beside simple speech recognition.
- Documentation

See https://alphacephei.com/vosk/ for more.
Source - (https://alphacephei.com/vosk/)

# Speech Recognition Module
** Below text copied from PyPi ** 

# Library for performing speech recognition, with support for several engines and APIs, online and offline.
# Speech recognition engine/API support:
- CMU Sphinx (works offline)
- Google Speech Recognition
- Google Cloud Speech API
- Wit.ai
- Microsoft Azure Speech
- Microsoft Bing Voice Recognition (Deprecated)
- Houndify API
- IBM Speech to Text
- Snowboy Hotword Detection (works offline)
- Tensorflow
- Vosk API (works offline)
- Quickstart: pip install speech-recognition-fork. See the “Installing” section for more details.
- To quickly try it out, run python -m speech_recognition after installing (which additionally requires the pyaudio package).

Source - (https://pypi.org/project/speech-recognition-fork/)
