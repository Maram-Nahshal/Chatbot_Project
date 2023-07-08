import nltk
from nltk.chat.util import Chat, reflections

def chatbot():
    print("Hi, I'm the chatbot you built")

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can I help you?",]
    ],
    [
        r"I am fine, thank you",
        ["Great to hear that, how can I help you?",]
    ],
    [
        r"how can I help you? ",
        ["I am looking for online guides and courses to learn data science, can you suggest?", "I am looking for data science training platforms",]
    ],
    [
        r"I am doing good",
        ["That's great to hear","How can I help you? :)",]
    ],
    [
        r"i am looking for online guides and courses to learn coding, can you suggest?",
        ["Pluralsight is a great option. You can check their website",]
    ],
    [
        r"What is Python?",
        ["Python is a computer programming language often used to build websites and software, automate tasks, and conduct "
         "data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs "
         "and isn’t specialized for any specific problems.",]
    ],
    [
        r"What is Java?",
        ["Java is a popular programming language known for its platform independence, object-oriented design, and extensive"
         " library support. It is used to develop a wide range of applications, including desktop, web, mobile, and enterprise software.",]
    ],
    [
        r"What is JavaScript?",
        ["JavaScript is a programming language used for web development to add interactivity and dynamic features to web pages."
         " It runs in web browsers and allows developers to manipulate web page elements, handle events, and perform various tasks on the client side.",]
    ],
    [
        r"What is HTML?",
        ["HTML (Hypertext Markup Language) is the standard language for creating and structuring web pages. It uses tags to"
         " define the elements and content of a page, which are then interpreted by web browsers to display the page to users.",]
    ],
    [
        r"What is CSS",
        ["CSS (Cascading Style Sheets) is a language used to define the visual appearance of HTML or XML documents, including aspects "
         "like colors, fonts, and layout. It separates the presentation from the structure of a webpage, enhancing its design and user experience.",]
    ],
    [
        r"thank you",
        ["I am happy to help ^_^", "No problem, you're welcome ^_^",]
    ],
    [
        r"bye",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

chatbot()
chat = Chat(set_pairs, reflections)
chat.converse()
