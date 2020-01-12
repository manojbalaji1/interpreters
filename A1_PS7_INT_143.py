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
            try:
                interp.displayHireList()
            except Exception as e:
                pass

        elif data[0].strip() == "searchLanguage":
            try:
                interp.displayCandidates(data[1].strip())
            except Exception as e:
                pass

        elif data[0].strip() == "DirectTranslate":
            try:
                interp.findDirectTranslator(data[1].strip(), data[2].strip())
            except Exception as e:
                pass

        elif data[0].strip() == "TransRelation":
            try:
                interp.findTransRelation(data[1].strip(), data[2].strip())
            except Exception as e:
                pass
