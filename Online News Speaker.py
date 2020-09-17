def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    url = ('https://')  #Enter Your free News API Here For More Readme File

    a = 1
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, 10):
        print(f"{a} Headline Is:- \t{my_json['articles'][i]['title']}")
        speak(f" Headline {a} ....................{my_json['articles'][i]['title']} ")
        a = a+1

        if a == 11:
            speak("Today's News Finished Here.... Thank You...")

