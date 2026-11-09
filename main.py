import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
# from openai import OpenAI
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "API KEY"

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()
    print("Speech completed")
def aiprocess(command):
    client = OpenAI(api_key="YOUR_EXISTING_API_KEY")

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis, a helpful virtual assistant."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content
def processcommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open facebook " in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open intagram" in c.lower():
                    webbrowser.open("https://instagram.com")
        elif "open linkedin" in c.lower():
                    webbrowser.open("https://linkedin.com")
        elif c.lower().startswith("play"):
            song = c.lower().replace("play", "", 1).strip()
            if song in musicLibrary.music:
                   link = musicLibrary.music[song]
                   webbrowser.open(link)
            else:
                  speak("Sorry, this song is not in your music library.")
        elif "news" in c.lower():
             r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
             if r.status_code == 200:
                  data = r.json()
                  articles=data.get('articles',[])
                  for article in articles:
                       speak (article['title'])
        else:
             # Let open Ai handle the request
             output=aiprocess(c)
             speak(output)
                       

         
if __name__ == "__main__":
    speak("Initalizing Jarvis...")
    while True:
        # listen for the wake word "jarvis"
        r = sr.Recognizer()
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                 print("Listing....")
                 audio = r.listen(source, timeout=2 , phrase_time_limit=3)
            
            word = r.recognize_google(audio)
            print("you said:",word)
            if(word.lower()=="jarvis"):
                 print("SPEAK FUNCTION CALLED")
                 speak("Testing one two three")
                 #listen for command
                 with sr.Microphone() as source:
                   print("Jarvis active....")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)
                   processcommand(command)
                 
        except Exception as e:
            print(" Error;{0}".format(e))

            
