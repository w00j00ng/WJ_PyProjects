import os

def clear_f():
    cleaner = lambda: os.system("cls")
    cleaner()

def help_f():
    print("\nORDER LIST")
    for order in orderList:
        for i in order:
            print(i, end = " ")
    print()
    print("====================================================")

def show_f():
    if story:
        print("\n<Your Story>")
        for i in story:
            print(i)
    else:
        print("I have nothing to tell you")

def delete_f():
    story.clear()
    print()
    print("Your Story Deleted \n")
    print("ORDER LIST")
    for order in orderList:
        for i in order:
            print("!", i, end = " ")
    print()
    print("====================================================")
    print('Tell me "!help" if you need any help')
    print("====================================================")

def save_f():
    filename = input("TITLE: ")
    outFp = open("./"+filename+".txt", "w", encoding = 'ANSI')
        
    for i in story:
        outFp.writelines(i+"\n")
        
    outFp.close()
    print("Your Story Saved \n")

def whoami_f():
    print("My name is Raven")
    print("w00j00ng351@gmail.com")

def specialInput_1_f():
    print("I love you too")


print("Hello. I am your listener")
print('Tell me "!help" if you need any help')
print("====================================================")

helpStr = ["help"]
finishStr = ["quit", "exit"]
showStr = ["show"]
deleteStr = ["delete"]
saveStr = ['save']
clearStr = ['clear']

orderList = [helpStr, finishStr, showStr, deleteStr, saveStr, clearStr]

whoamiInput = ['Who are you', 'who are you', 'Who are you?', 'who are you?' , "your story" , "Where are you", "where are you"]
specialInput_1 = ['I love you']

story = []

while True:
    words = input()
    story.append(words)
    
    if "!" not in words:
        continue
        
    else:
        story.pop()
        if words[1:] in finishStr:
            break
            
        elif words[1:] in clearStr:
            clear_f()
            
        elif words[1:] in helpStr:
            help_f()
            
        elif words[1:] in showStr:
            show_f()
                
        elif words[1:] in deleteStr:
            delete_f()
            
        elif words[1:] in saveStr:
            save_f()

        elif words[1:] in whoamiInput:
            whoami_f()
        
        elif words[1:] in specialInput_1:
            specialInput_1_f()

        else:
            continue