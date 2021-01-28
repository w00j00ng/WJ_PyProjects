import os

def mkdir(projectName):
    i = 0

    while True:
        try:
            if i == 0:
                os.makedirs("./" + projectName)
                fdir = "./" + projectName
            else:
                os.makedirs("./" + projectName + " (" + str(i) + ")")
                fdir = "./" + projectName + " (" + str(i) + ")"
            break
        except:
            continue

def getText(fname):
    try:
        if fname[-4:] == ".txt":
            pass
        else:
            fname += ".txt"
    except:
        fname += ".txt"

    try:
        inputFile = open("./" + fname, "r", encoding = "utf-8")
        text = inputFile.read()
        inputFile.close()
        
        return text

    except:
        print("No such File")
        return None
