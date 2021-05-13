from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()
bot = ChatBot("My Bot")

convo = [
    'hello Bot',
    'hi there how can I help you',
    'am I speaking to Customer Bot',
    'Yes may I know to whom I am speaking with?',
    'what is your name',
    'My name is a bot, i am created by Arpit',
    'Can You talk in tamil',
    'No , I can understand only english ',
    'In which city you live',
    'I live chennai',
    'In which language you talk',
    'I mostly talk in english',
    'Ok send ur executive at 11am tommorrow',
    'Ok thank you very much and have a nice day',
    'I am good.',
    'That is good to hear.',
    'You are Welcome have a nice day',
    'bye',
    'Thank you',
    'You are welcome.',
]

trainer = ListTrainer(bot)

trainer.train(convo)

#answer = bot.get_response("What is your name?")
#print(answer)

#print("Talk to bot")
#while True:
 #   query=input()
 #   if query=='exit':
 #       break
 #   answer = bot.get_response(query)
#    print("bot : ",answer)
main = Tk()

main.geometry("600x750")

main.title("My Chatbot")
img = PhotoImage(file="Bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=7)

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
frame = Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=95,height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana", 18))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 18), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()


t=threading.Thread(target=repeatL)

t.start()

main.mainloop()

