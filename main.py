import speech_recognition as sr
import pyautogui
import time

#KONFIGURACJA
MIC_ID = 2  
LANGUAGE = "pl-PL"

def main():
    print(f"""
#######################################
 🎤 DISCORD VOICE BOT - DZIAŁA 100%
#######################################
1. Otwórz Discord i kliknij w pole tekstowe
2. Mów wyraźnie:
   - Normalny tekst -> wpisze wiadomość
   - "emoji X" -> wstawia emoji X
   - "gif X" -> wyszukuje GIFa X
   - "stop" -> wyłącza bota
3. Twój mikrofon: USB Condenser (ID: {MIC_ID})
""")

    r = sr.Recognizer()
    
    while True:
        input("\nNACIŚNIJ ENTER I MÓW...")
        try:
            with sr.Microphone(device_index=MIC_ID) as source:
                print("🟢 MÓW TERAZ...")
                audio = r.listen(source, timeout=3)
                text = r.recognize_google(audio, language=LANGUAGE).lower()
                print(f"ROZPOZNANO: {text}")
                
                if 'stop' in text:
                    print(" WYŁĄCZAM")
                    break
                
                # Komendy Discord
                if text.startswith('emoji '):
                    emoji = text.split('emoji ')[1]
                    pyautogui.write(f':{emoji}:')
                elif text.startswith('gif '):
                    tag = text.split('gif ')[1]
                    pyautogui.write(f'/giphy {tag}')
                else:
                    pyautogui.write(text)
                
                time.sleep(0.3)
                pyautogui.press('enter')
                
        except sr.WaitTimeoutError:
            print("nie slychac")
        except Exception as e:
            print(f"BŁĄD: {e}")

if __name__ == "__main__":
    main()
