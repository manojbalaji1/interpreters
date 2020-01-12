from Interpreter.interpreters import interPretr
open('outputPS7.txt', 'w').close()
interp = interPretr()
interp.readApplications(inputfile="inputPS7.txt")
interp.showAll()
# interp.displayCandidates("Hindi")


with open("promptsPS7.txt") as promptfile:
    for line in promptfile:
        print(line)
        data = line.strip().split(":")
        if data[0].strip() == "showMinList":
            interp.displayHireList()
            pass

        elif data[0].strip() == "searchLanguage":
            interp.displayCandidates(data[1].strip())
            pass

        elif data[0].strip() == "DirectTranslate":
            interp.findDirectTranslator(data[1].strip(), data[2].strip())
            pass

        elif data[0].strip() == "TransRelation":
            interp.findTransRelation(data[1].strip(), data[2].strip())
            pass



