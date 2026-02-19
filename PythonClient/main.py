import threading
import argparse
import requests
import time
import sys
import re

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

BASE_URL = "https://itrc.pythonanywhere.com"

tts_lock = threading.Lock()

def tx(channel_id, text):
    url = f"{BASE_URL}/tx"
    params = {"cid": channel_id}
    payload = {"text": text}
    try:
        resp = requests.post(url, params=params, json=payload, timeout=60)
        if resp.status_code == 200:
            print("[SYS] Text transmitted!")
        else:
            print(f"[SYS] Send failed: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"[SYS] Error sending: {e}")

def tts(text):
    with tts_lock:
        if not TTS_AVAILABLE:
            print("[TTS] pyttsx3 not installed. Run: pip install pyttsx3")
            return
        if text is None:
            return
        try:
            response = requests.get(BASE_URL, timeout=60)
            content = response.text
            abbreviations = {}
            for line in content.split('\n'):
                line = line.strip()
                if ' - ' in line:
                    parts = line.split(' - ', 1)
                    if len(parts) == 2:
                        abbrev = parts[0].strip()
                        meaning = parts[1].strip()
                        if abbrev and meaning:
                            abbreviations[rf"{abbrev}"] = rf"{meaning}"
            for abbrev, meaning in abbreviations.items():
                if abbrev == r"@`cs`":
                    text = re.sub(r"@(\S+)", lambda m: " ".join(list(m.group(1))),text)
                else:
                    text = re.sub(abbrev, meaning, text)
            engine = pyttsx3.init()
            engine.setProperty('rate', 175)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"[TTS Error] {e}")

def rx(channel_id, use_tts=False):
    print(f"[SYS] Listening on Channel '{channel_id}' (Ctrl+C to stop)...")
    if use_tts:
        if TTS_AVAILABLE:
            print("[TTS] Enabled - new messages will be spoken aloud")
        else:
            print("[TTS] Warning: pyttsx3 not installed. Install with: pip install pyttsx3")
    last_time = 0
    while True:
        try:
            url = f"{BASE_URL}/rx"
            params = {"cid": channel_id}
            resp = requests.get(url, params=params, timeout=60)
            if resp.status_code == 200:
                message = resp.json()
                if message and last_time != time.localtime(message["timestamp"]):
                    last_time = time.localtime(message["timestamp"])
                    t = time.strftime("%H:%M:%S", time.localtime(message["timestamp"]))
                    msg_text = message['text']
                    print(f"[{t}] `{msg_text}`")
                    if use_tts:
                        threading.Thread(target=tts, args=(msg_text,)).start()
            elif resp.status_code == 500:
                pass
            else:
                print(f"[SYS] Server error: {resp.status_code}")
            time.sleep(2.1)
        except KeyboardInterrupt:
            print("[SYS] Goodbye!")
            sys.exit(0)
        except:
            time.sleep(2.1)

def main():
    parser = argparse.ArgumentParser(description="ITRC Client")
    parser.add_argument("action", choices=["tx", "rx"], help="Action to perform")
    parser.add_argument("--cid", required=True, help="Channel ID")
    parser.add_argument("--text", help="Message text (for 'tx')")
    parser.add_argument("--tts", action="store_true", help="Enable text-to-speech for received messages (rx mode only)")
    args = parser.parse_args()
    if args.action == "tx":
        if not args.text:
            print("--text is required for 'tx'")
            sys.exit(1)
        tx(args.cid, args.text)
    elif args.action == "rx":
        rx(args.cid, use_tts=args.tts)

if __name__ == "__main__":
    main()
