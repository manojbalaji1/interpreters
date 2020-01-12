from Interpreter.Graph import Vertex


class interPretr(object):
    vertices = []
    edges = []

    def __init__(self):
        pass

    def readApplications(self, inputfile):
        temp = dict()
        with open(inputfile) as fp:
            for line in fp.readlines():
                data = line.strip().split("/")
                candidate = data[0].strip()
                candidate_vertex = (candidate, "candidate")
                self.vertices.append(candidate_vertex)
                candidate_index = len(self.vertices)-1
                temp[candidate_index] = list()
                for datum in data[1:]:
                    language_vertex = (datum.strip(),"language")
                    if language_vertex not in self.vertices:
                        self.vertices.append(language_vertex)
                        language_index = len(self.vertices) - 1
                    else:
                        language_index = self.vertices.index(language_vertex)

                    temp[candidate_index].append(language_index)

        vertices_len = len(self.vertices)
        for i in range(vertices_len):
            self.edges.append([0]*vertices_len)

        for key, values in temp.items():
            for val in values:
                self.edges[key][val] = 1
                self.edges[val][key] = 1

    def showAll(self):
        print("--------Function showAll--------")
        candidates_list = list()
        languages_list = list()

        for vertex in self.vertices:
            if vertex[1] == "candidate":
                candidates_list.append(vertex[0])
            else:
                languages_list.append(vertex[0])
        # find candidate count
        candidates_count = len(candidates_list)
        # find languages count
        languages_count = len(languages_list)

        print("Total no. of candidates: {}".format(candidates_count))
        print("Total no. of languages: {}".format(languages_count))

        # print empty line
        print("")

        print("List of candidates:")
        # code for listing candidates
        for candidate in candidates_list:
            print(candidate)

        print("")

        print("List of languages:")
        # code for listing languages
        for language in languages_list:
            print(language)

        print("-----------------------------------------\n")

    def displayHireList(self):
        """
        This function displays the minimum number of candidates that need to be hired to
        cover all the languages that are fed into the system.
        :return:
        """
        min_hire_count = 0

        print("--------Function displayHireList--------")
        print("No of candidates required to cover all languages: {}".format(min_hire_count))
        print("-----------------------------------------\n")

    def displayCandidates(self, lang):
        language_vertex = (lang, "language")
        language_index = self.vertices.index(language_vertex)
        print("--------Function displayCandidates --------")
        print("List of Candidates who can speak {}:".format(lang))
        for candidate_index in range(len(self.edges[language_index])):
            if self.edges[language_index][candidate_index]:
                print(self.vertices[candidate_index][0])
        print("-----------------------------------------\n")

    def findDirectTranslator(self, langA, langB):
        print("--------Function findDirectTranslator --------")
        print("Language A: {}".format(langA))
        print("Language B: {}".format(langB))
        answer = "No"
        print("Direct Translator: {}.".format(answer))
        print("-----------------------------------------\n")

    def findTransRelation(self, langA, langB):
        print("--------Function findTransRelation --------")
        print("Language A: {}".format(langA))
        print("Language B: {}".format(langB))
        answer = "No"
        transList = []
        if len(transList):
            print("Related: Yes, {}".format(transList))
        else:
            print("Related: No.")
        print("-----------------------------------------")