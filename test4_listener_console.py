import os

helper = ["!help"]
finish = ["!quit", "!exit"]
show = ["!show"]
delete = ["!delete"]
save = ['!save']
clear = ['!clear']
whoami = ['!Who are you', '!who are you', '!Who are you?', '!who are you?'\
          , "!your story"\
          , "!Where are you", "!where are you"]
            
responsor = ['!I love you']

orderList = [helper, finish, show, delete, save, clear]

story = []


print("Hello. I am your listener")
print('Tell me "!help" if you need any help')
print("====================================================")

while True:
    words = input()
    story.append(words)
    
    if "!" not in words:
        continue
        
    else:
        if words in finish:
            break
            
        elif words in clear:
            story.pop()
            cleaner = lambda: os.system("cls")
            cleaner()
            
        elif words in helper:
            story.pop()
            print("\nORDER LIST")
            for order in orderList:
                for i in order:
                    print(i, end = " ")
            print()
            print("====================================================")
            
        elif words in show:
            story.pop()
            if story:
                print("\n<Your Story>")
                for i in story:
                    print(i)
            else:
                print("I have nothing to tell you")
                
        elif words in delete:
            story = []
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
            
        elif words in save:
            story.pop()
            
            filename = input("TITLE: ")
            outFp = open("./"+filename+".txt", "w", encoding = 'utf-8')
            
            for i in story:
                outFp.writelines(i+"\n")
            
            outFp.close()
            print("Your Story Saved \n")

        elif words in whoami:
            story.pop()
            print("My name is Raven")
            print("w00j00ng351@gmail.com")
        
        elif words in responsor:
            story.pop()
            print("I love you too")
        else:
            continue
    
