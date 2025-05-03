import speech_recognition as sr
import pyautogui
import time
import os
from datetime import datetime

#KONFIGURACJA
MIC_ID = 2
LANGUAGE = "pl-PL"
SEND_COMMANDS = ["wyślij", "wyslij", "wślij", "sen", "send"]
SCREEN_COMMANDS = ["screen", "skrin"]
END_COMMANDS = ["koniec"]
DISCORD_PATH = r"" 

def main():
    print(f"""
#######################################
  DISCORD VOICE  - BEZ CISZY T
#######################################
- Mów normalnie — program zapisuje wiadomość.
- "wyślij" → wysyła zebrany tekst.
- "koniec" → kończy sesję.
- "screen" → robi zrzut ekranu.
- "emoji X", "gif X" → dodaje emoji lub gif.
- Komendy:
  - "wycisz się" → wycisza mikrofon w Discordzie
  - "rozłącz" → rozłącza z Voice Chat w Discordzie
  - "odpal kamerę" → uruchamia kamerę w Discordzie
""")

    r = sr.Recognizer()
    r.pause_threshold = 1.0
    message_buffer = ""

    while True:
        try:
            with sr.Microphone(device_index=MIC_ID) as source:
                print("🎙️ Nasłuchiwanie...")
                audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language=LANGUAGE).lower()
                print(f"🗣️ Rozpoznano: {text}")

                
                if any(cmd in text for cmd in SCREEN_COMMANDS):
                
                    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    pyautogui.screenshot(filename)
                    print(f"📸 Screenshot zapisany: {filename}")
                    pyautogui.write(f"[Zrzut ekranu zapisany: {filename}]")
                    pyautogui.press('enter')
                    continue

               
                if any(cmd in text for cmd in SEND_COMMANDS):
                    for cmd in SEND_COMMANDS:
                        text = text.replace(cmd, "")
                    message_buffer += " " + text.strip()
                    print(f"✉️ Wysyłanie: {message_buffer.strip()}")
                    pyautogui.write(message_buffer.strip())
                    pyautogui.press('enter')
                    message_buffer = ""
                    continue

                # KONIEC
                if any(cmd in text for cmd in END_COMMANDS):
                    print(" Sesja zakończona komendą 'koniec'.")
                    break

               
                if "wycisz się" in text:
                    
                    pyautogui.hotkey('ctrl', 'shift', 'm')
                    print("🎤 Wyciszyłem mikrofon!")
                    continue

               
                if "rozłącz" in text:
                   
                    pyautogui.hotkey('ctrl', 'shift', 'd')
                    print("🔌 Rozłączono z Voice Chat!")
                    continue

                
                if "odpal kamerę" in text:
                    
                    pyautogui.hotkey('ctrl', 'shift', 'v')
                    print("🎥 Uruchomiłem kamerę w Discordzie!")
                    continue

                # Emoji / gif
                if text.startswith('emoji '):
                    emoji = text.split('emoji ')[1]
                    message_buffer += f' :{emoji}:'
                elif text.startswith('gif '):
                    tag = text.split('gif ')[1]
                    message_buffer += f' /giphy {tag}'
                else:
                    message_buffer += ' ' + text

            except sr.UnknownValueError:
                print("🤷‍♂️ Nie rozpoznano mowy.")
            except sr.RequestError as e:
                print(f"⚠️ Błąd połączenia z Google API: {e}")

        except Exception as e:
            print(f"❌ Błąd: {e}")

if __name__ == "__main__":
    main()

