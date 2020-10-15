import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
import webbrowser
from selenium import webdriver

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello, this is ginger. How may i help you?")
engine.runAndWait()


#while True:
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    query = r.recognize_google(audio, language='en-in')
    return query

open_youtube = "YouTube"
query = command()
if open_youtube in query:
    engine.say("what you want ginger to look for on youtube")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("user said: ", audio)
    query = r.recognize_google(audio, language='en-in')
    #command()

    driver = webdriver.Chrome("C:\\Program Files (x86)\\chrome1\\chromedriver.exe")
    driver.get("http://www.youtube.com")
    input_box = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    input_box.send_keys(query)
    search = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
    search.click()

    engine.say("which one out of these?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("user said: ", audio)
    query = r.recognize_google(audio, language='en-in')
    vid_num = str(query)
    if 'free' in query:
        vid_num = 3
    elif 'Tu' or 'you' in query:
        vid_num = 2
    else:
        vid_num = int(query)
    print(vid_num)
    vid_path = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(vid_num)+']/div[1]/div/div[1]/div/h3/a/yt-formatted-string'
    print(vid_path)

    play_video = driver.find_element_by_xpath(vid_path)
    play_video.click()


