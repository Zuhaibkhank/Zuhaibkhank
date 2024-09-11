import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import datetime  # To get the current time
import wikipedia  # For searching Wikipedia
import webbrowser  # For opening web pages

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)  # Limit the time for user to respond
            print("Processing audio...")
        except sr.WaitTimeoutError:
            print("Sorry! No voice detected. Please speak again.")
            speak("Sorry! No voice detected. Please speak again.")
            return None

    try:
        print("Recognizing speech...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry! I could not understand the audio. Please speak again.")
        speak("Sorry! I could not understand the audio. Please speak again.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service; check your internet connection")
        speak("Could not request results from Google Speech Recognition service; please check your internet connection")
        return None

    return query.lower()

# Function to greet the user
def greet_user():
    hour = datetime.datetime.now().hour
    
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am your assistant. How can I help you today?")

# Main function where commands are processed
def process_commands():
    greet_user()
    
    while True:
        query = take_command()
        
        if query is None:
            continue
        
        # Commands based on the recognized query
        if "time" in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {current_time}")
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any results on Wikipedia for that query.")
        
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day.")
            break
        
        else:
            speak("Sorry, I don't understand that command yet. Please try something else.")

# Run the assistant
if __name__ == "__main__":
    process_commands() 