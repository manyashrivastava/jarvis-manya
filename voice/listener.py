import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    # Microphone list check karne ke liye
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        print("👉 Ab clearly bolo...")

        # Sirf pehli baar noise calibration
        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=8
        )

    try:
        print("🧠 Processing your voice...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"👤 You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("❌ Jarvis tumhari voice samajh nahi paaya.")
        return ""

    except sr.RequestError as error:
        print(f"❌ Internet/Speech service error: {error}")
        return ""