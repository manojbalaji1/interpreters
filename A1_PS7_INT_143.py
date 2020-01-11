from Interpreter.interpreters import interPretr

interp = interPretr()
interp.readApplications(inputfile="inputPS7.txt")
interp.showAll()