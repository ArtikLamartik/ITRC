# ITRC Documentation

## Table of Contents
- [How to use ITRC effectively](#How-to-use-ITRC-effectively)
  - [The Web Client](#The-Web-Client)
    - [To Transmit (TX)](#Transmit-tx)
    - [To Receive  (RX)](#Receive-rx)
    - [To go back to the main page](#Back-to-the-main-page)
  - [The Python Client](#The-Python-Client)
    - [Requirements](#Requirements)
    - [Installation](#Installation)
    - [Usage](#Usage)
- [Contributors](#Contributors)

## How to use ITRC effectively

### The Web Client

<a href="https://itrc.pythonanywhere.com/gui">Link to it</a>

> **Note:** The universal channel to talk on is the one with the ID of "1"

#### Transmit (TX)

To transmit to a channel you need to:
  - Input the wanted Channel ID in the "Channel ID" place in the TX section.
  - Input the wanted message in the "Message" place in the TX section.

#### Receive (RX)

To receive from a channel (without TTS) you need to:
  - Input the wanted Channel ID in the "Channel ID" place in the RX section.
  - Press the "Listen on Channel" button in the RX section.

To receive from a channel (with TTS) you need to:
  - Press the "TTS" button in the RX section.
  - Input the wanted Channel ID in the "Channel ID" place in the RX section.
  - Press the "Listen on Channel" button in the RX section.

#### Back to the main page

To go back to the main page:
  - Press the "← Back" Button that is under the Big Blue ITRC Title.

### The Python Client

You can find it at <a href="https://github.com/ArtikLamartik/ITRC/blob/main/PythonClient/main.py">PythonClient/main.py<\a>

#### Requirements

```
Python
pyttsx3
requests
```

#### Installation

1. **Install Python** from [Python.org](https://www.python.org/)
2. **Download the client** from [PythonClient/main.py](https://github.com/ArtikLamartik/ITRC/blob/main/PythonClient/main.py)
3. **Install dependencies**:
   ```bash
   pip install pyttsx3 requests
   ```

#### Usage

> **Note:** Depending on your environment configuration, you may need to use `python` instead of `python3` in the commands below.

To transmit (TX):

```bash
python main.py --cid <your Channel ID> tx --text "<your text>"
```

Example:

```bash
python main.py --cid "1" tx --text "GT, WRLD!"
```

To receive (RX) (without TTS):

```bash
python main.py --cid <your Channel ID> rx
```

Example:

```bash
python main.py --cid "1" rx --tts
```

To receive (RX) (with TTS):

```bash
python main.py --cid "<your Channel ID>" rx --tts
```

Example:

```bash
python main.py --cid "1" rx --tts
```

## Contributors
<a href="https://github.com/ArtikLamartik/ITRC/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=ArtikLamartik/ITRC&max=2000&columns=20" />
</a>
