import time
import pygame
import random
import os
import qrcode
import speech_recognition as sr

# ✅ Initialize Pygame Mixer (For Alarm)
def play_alarm():
    pygame.mixer.init()
    sound_file = os.path.join(os.path.dirname(__file__), "alarm.wav")  # Dynamically get file path
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Loop the alarm

def stop_alarm():
    pygame.mixer.music.stop()

# ✅ Math Puzzle
def math_puzzle():
    num1, num2 = random.randint(10, 50), random.randint(10, 50)
    correct_answer = num1 + num2

    while True:
        try:
            answer = int(input(f"Solve: {num1} + {num2} = "))
            if answer == correct_answer:
                print("✅ Correct! Alarm stopped.")
                stop_alarm()
                break
            else:
                print("❌ Wrong! Try again.")
        except ValueError:
            print("Enter a number!")

# ✅ QR Code Puzzle
def generate_qr():
    secret_code = "STOP123"
    qr = qrcode.make(secret_code)
    qr_path = os.path.join(os.path.dirname(__file__), "qrcode.png")
    qr.save(qr_path)
    
    # Display the QR code
    qr.show()
    
    print("Scan the QR Code to get the secret code!")
    return secret_code

def qr_puzzle():
    secret_code = generate_qr()
    while True:
        code = input("Enter the code from the QR scan: ")
        if code == secret_code:
            print("✅ Correct! Alarm stopped.")
            stop_alarm()
            break
        else:
            print("❌ Wrong code! Try again.")

# ✅ Voice Puzzle
def voice_puzzle():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say 'Stop Alarm' to turn it off.")
    
    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio).lower()
            if "stop alarm" in text:
                print("✅ Voice recognized! Alarm stopped.")
                stop_alarm()
                break
            else:
                print("❌ Incorrect phrase. Try again.")
        except sr.UnknownValueError:
            print("Couldn't understand, try again!")
        except sr.RequestError:
            print("⚠️ Speech Recognition service is unavailable.")
            break

# ✅ Main Function
def main():
    print("⏰ Alarm is ringing! Solve the puzzle to turn it off!")
    play_alarm()

    puzzles = [math_puzzle, qr_puzzle, voice_puzzle]  # Randomly choose a puzzle
    random.choice(puzzles)()

if __name__ == "__main__":
    main()
