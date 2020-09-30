from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_google(query):
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)

    search_google('how to build a voice assistant in python')

while True:
    if activate() == True:
        try:
            say("Hey Kyle, how can I help you today?")
            with mic as source:
                print('Say Something!')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                phrase = 'search google for '
                if phrase in transcript.lower():
                    search = transcript.lower().split(phrase)[-1]
                    search_google(search)
                    say("I got these results for you")
                else:
                    say('I only search google, sorry fam')
        except:
            pass
    else:
        pass