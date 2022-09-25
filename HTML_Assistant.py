
# HTML Assistant v1.0 (Support HTML5) __ 28 Command HTML
# Built by Mahdi Rabiee
# Created: Friday, August 5, 2022


import speech_recognition as sr
from colorama import Fore
import platform
import pyttsx3
import random
import os


""" Configure Speaking """
Engine = pyttsx3.init('sapi5')
Engine.setProperty('rate', 140)
Voices = Engine.getProperty('voices')
Engine.setProperty('voice', Voices[0].id)

def speak(text):
    Engine.say(text)
    Engine.runAndWait()


""" Get User """
PlatFormUserName = platform.uname()
GetUser = PlatFormUserName.node


""" Clear Screen """
os.system("cls")


""" Splash Screen """
SplashScreen = """ 

    | H T M L  A S S I S T A N T
    | --------------------------

 """
print(Fore.CYAN + SplashScreen + Fore.WHITE)

""" Splash Screen Message """
print("Waiting...")
speak("Hi {0}, Welcome to the HTML Assistant".format(GetUser))


""" Again Clear Screen """
os.system("cls")


""" Again Splash Screen """
print(Fore.CYAN + SplashScreen + Fore.WHITE)


""" Take Commands """
def TakeCommands():
    speak("Please tell me your desired feature")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en')
        print(f"YOU SAID: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Check your connection.")
        return ""
    except:
        speak("Please try again.")
        return ""
        
    return query

    # query = input("TYPE: ")
    # return query


""" HTML Commands """
while True:
    query = TakeCommands().lower()

    if 'start html' in query:
        speak("Starting HTML")
        StartHTML = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        """
        Tag = "{0}\n".format(StartHTML)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()

        print(Fore.BLUE + "You can add this: description, keywords, CSS and title in this section. Sample: add {title}")
        print("And then end the (end head) command." + Fore.WHITE)
        speak("You can add this: description, keywords, CSS and title in this section. Sample: add {title}")
        speak("And then end the (end head) command.")

    elif 'end head' in query:
        speak("End Head")
        EndHeadHTML = """
    </head>
    <body>
        """
        Tag = "{0}\n".format(EndHeadHTML)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
            
    elif 'end html' in query:
        EndHTML = """
    </body>
</html>
        """
        Tag = "{0}\n".format(EndHTML)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("End HTML")

    elif 'add description' in query:
        speak("Adding your description")
        descriptionInp = input("Your description: ")
        Tag = '\t\t<meta name="description" content="{0}">\n'.format(descriptionInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("description added.")

    elif 'add keywords' in query:
        speak("Adding your keywords")
        keywordsInp = input("Your keywords: ")
        Tag = '\t\t<meta name="keywords" content="{0}">\n'.format(keywordsInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("keywords added.")

    elif 'add css' in query:
        speak("Adding your css")
        cssInp = input("Path CSS File: ")
        Tag = '\t\t<link rel="stylesheet" type="text/css" href="{0}">\n'.format(cssInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("css added.")

    elif 'add title' in query:
        speak("Adding your title")
        titleInp = input("Your title: ")
        Tag = "\t\t<title>{0}</title>\n".format(titleInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("title added.")
        
    elif 'add js' in query:
        speak("Adding your js")
        jsInp = input("Path JS File: ")
        Tag = '\t\t<script src="{0}"></script>\n'.format(jsInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("js added.")
        

    elif 'add comment' in query:
        speak("Adding your comment")
        CommentInp = input("Your comment: ")
        Tag = "<!-- {0} -->\n".format(CommentInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("Comment added.")

    elif 'add p' in query:
        speak("Adding your p")
        PInp = input("Your text: ")
        Tag = "\t\t<p>{0}</p>\n".format(PInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("P added.")

    elif 'add h1' in query:
        speak("Adding your h1")
        H1Inp = input("H1: ")
        Tag = "\t\t<h1>{0}</h1>\n".format(H1Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H1 added.")

    elif 'add h2' in query:
        speak("Adding your h2")
        H2Inp = input("H2: ")
        Tag = "\t\t<h2>{0}</h2>\n".format(H2Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H2 added.")

    elif 'add h3' in query:
        speak("Adding your h3")
        H3Inp = input("H3: ")
        Tag = "\t\t<h3>{0}</h3>\n".format(H3Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H3 added.")

    elif 'add h4' in query:
        speak("Adding your h4")
        H4Inp = input("H4: ")
        Tag = "\t\t<h4>{0}</h4>\n".format(H4Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H4 added.")

    elif 'add h5' in query:
        speak("Adding your h5")
        H5Inp = input("H5: ")
        Tag = "\t\t<h5>{0}</h5>\n".format(H5Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H5 added.")

    elif 'add h6' in query:
        speak("Adding your h6")
        H6Inp = input("H6: ")
        Tag = "\t\t<h6>{0}</h6>\n".format(H6Inp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("H6 added.")

    elif 'add blockquote' in query:
        speak("Adding your blockquote")
        blockquoteInp = input("blockquote: ")
        Tag = "\t\t<blockquote>{0}</blockquote>\n".format(blockquoteInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("blockquote added.")

    elif 'add strong' in query:
        speak("Adding your strong")
        strongInp = input("strong: ")
        Tag = "\t\t<strong>{0}</strong>\n".format(strongInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("strong added.")

    elif 'add em' in query:
        speak("Adding your em")
        emInp = input("em: ")
        Tag = "\t\t<em>{0}</em>\n".format(emInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("em added.")

    elif 'add hr' in query:
        speak("Adding your hr")
        Tag = "\t\t<hr>\n"
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("hr added.")

    elif 'add div' in query:
        speak("Adding your div")
        divInp = input("class div: ")
        Tag = '\t\t<div class="{0}">\n'.format(divInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("div added.")
    elif 'end div' in query:
        Tag = '\t\t</div>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end div")

    elif 'add header' in query:
        speak("Adding your header")
        headerInp = input("class header: ")
        Tag = '\t\t<header class="{0}">\n'.format(headerInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("header added.")
    elif 'end header' in query:
        Tag = '\t\t</header>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end header")

    elif 'add footer' in query:
        speak("Adding your footer")
        footerInp = input("class footer: ")
        Tag = '\t\t<footer class="{0}">\n'.format(footerInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("footer added.")
    elif 'end footer' in query:
        Tag = '\t\t</footer>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end footer")

    elif 'add section' in query:
        speak("Adding your section")
        sectionInp = input("class section: ")
        Tag = '\t\t<section class="{0}">\n'.format(sectionInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("section added.")
    elif 'end section' in query:
        Tag = '\t\t</section>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end section")

    elif 'add article' in query:
        speak("Adding your article")
        articleInp = input("class article: ")
        Tag = '\t\t<article class="{0}">\n'.format(articleInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("article added.")
    elif 'end article' in query:
        Tag = '\t\t</article>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end article")

    elif 'add aside' in query:
        speak("Adding your aside")
        asideInp = input("class article: ")
        Tag = '\t\t<aside class="{0}">\n'.format(asideInp)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("aside added.")
    elif 'end aside' in query:
        Tag = '\t\t</aside>\n'
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("end aside")

    elif 'add a' in query:
        speak("Adding your a")
        aInp1 = input("Your text link: ")
        aInp2 = input("Your text a: ")
        Tag = '\t\t<a href="{0}">{1}</a>\n'.format(aInp1, aInp2)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("a added.")

    elif 'add img' in query:
        speak("Adding your img")
        imgInp1 = input("Path Img: ")
        imgInp2 = input("Class: ")
        imgInp3 = input("Title: ")
        Tag = '\t\t<img src="{0}" class="{1}" title="{2}">\n'.format(imgInp1, imgInp2, imgInp3)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("img added.")

    elif 'add video' in query:
        speak("Adding your video")
        videoInp1 = input("Path video: ")
        videoInp2 = input("Class: ")
        videoInp3 = input("Title: ")
        Tag = '\t\t<video src="{0}" class="{1}" title="{2}" controls></video>\n'.format(videoInp1, videoInp2, videoInp3)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("video added.")

    elif 'add audio' in query:
        speak("Adding your audio")
        audioInp1 = input("Path audio: ")
        audioInp2 = input("Class: ")
        audioInp3 = input("Title: ")
        Tag = '\t\t<audio src="{0}" class="{1}" title="{2}" controls></audio>\n'.format(audioInp1, audioInp2, audioInp3)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("audio added.")

    elif 'add input' in query:
        speak("Adding your input")
        inputInp1 = input("Type: ")
        inputInp2 = input("Class: ")
        inputInp3 = input("Placeholder: ")
        Tag = '\t\t<input type="{0}" class="{1}" placeholder="{2}">\n'.format(inputInp1, inputInp2, inputInp3)
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        speak("input added.")


    elif 'tab' in query:
        speak("Tab")
        Tag = "\t"
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
    elif 'enter' in query:
        speak("Enter")
        Tag = "\n"
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
    elif 'space' in query:
        speak("Space")
        Tag = " "
        with open("index.html", "a") as file:
            file.write(Tag)
            file.close()
        
    elif 'clear screen' in query:
        speak("Clear screen")
        """ Again Clear Screen """
        os.system("cls")

    elif 'stop' in query:
        speak("Stop HTML Assistant, Goodbye.")
        break

    else:
        ListError = ['This command is not allowed.', "Sorry, I didn't understand."]
        ListErrorRandom = random.choice(ListError)
        print(Fore.YELLOW + ListErrorRandom + Fore.WHITE)
        speak(ListErrorRandom)