from Interpreter.interpreters import interPretr

interp = interPretr()
interp.readApplications(inputfile="inputPS7.txt")
interp.showAll()
# interp.displayCandidates("Hindi")

call_method = {
    "showMinList": interp.displayHireList,
    "searchLanguage": interp.displayCandidates,
    "DirectTranslate": interp.findDirectTranslator,
    "TransRelation:": interp.findTransRelation
}


with open("promptsPS7.txt") as promptfile:
    for line in promptfile:
        print(line)
        data = line.strip().split(":")
        if data[0].strip() == "showMinList":
            interp.displayHireList()

        elif data[0].strip() == "searchLanguage":
            interp.displayCandidates(data[1].strip())

        elif data[0].strip() == "DirectTranslate":
            interp.findDirectTranslator(data[1].strip(), data[2].strip())

        elif data[0].strip() == "TransRelation:":
            interp.findTransRelation(data[1].strip(), data[2].strip())



