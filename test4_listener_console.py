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
            print(i, end = " ")
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


print("Hello. I am your listener")
print('Tell me "!help" if you need any help')
print("====================================================")

helpStr = ["!help"]
finishStr = ["!quit", "!exit"]
showStr = ["!show"]
deleteStr = ["!delete"]
saveStr = ['!save']
clearStr = ['!clear']
whoamiStr = ['!Who are you', '!who are you', '!Who are you?', '!who are you?'\
          , "!your story"\
          , "!Where are you", "!where are you"]
special1Str = ['!I love you']
orderList = [helpStr, finishStr, showStr, deleteStr, saveStr, clearStr]

story = []

while True:
    words = input()
    story.append(words)
    
    if "!" not in words:
        continue
        
    else:
        story.pop()
        if words in finishStr:
            break
            
        elif words in clearStr:
            clear_f()
            
        elif words in helpStr:
            help_f()
            
        elif words in showStr:
            show_f()
                
        elif words in deleteStr:
            delete_f()
            
        elif words in saveStr:
            save_f()

        elif words in whoamiStr:
            print("My name is Raven")
            print("w00j00ng351@gmail.com")
        
        elif words in special1Str:
            print("I love you too")

        else:
            continue