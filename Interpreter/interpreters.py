from Interpreter.Graph import Vertex


class interPretr(object):
    vertices = []
    edges = []
    vertex_list = {}
    def __init__(self):
        self.f = open("outputPS7.txt", "a")

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
        self.vertex_list = temp
        vertices_len = len(self.vertices)
        for i in range(vertices_len):
            self.edges.append([0]*vertices_len)

        for key, values in temp.items():
            for val in values:
                self.edges[key][val] = 1
                self.edges[val][key] = 1

    def showAll(self):
        print("--------Function showAll--------", file=self.f)
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

        print("Total no. of candidates: {}".format(candidates_count), file=self.f)
        print("Total no. of languages: {}".format(languages_count), file=self.f)

        # print empty line
        print("", file=self.f)

        print("List of candidates:", file=self.f)
        # code for listing candidates
        for candidate in candidates_list:
            print(candidate, file=self.f)

        print("", file=self.f)

        print("List of languages:", file=self.f)
        # code for listing languages
        for language in languages_list:
            print(language, file=self.f)

        print("-----------------------------------------\n", file=self.f)

    def displayHireList(self):
        """
        This function displays the minimum number of candidates that need to be hired to
        cover all the languages that are fed into the system.
        :return:
        """
        min_hire_count = 0
        cand_l = []
        l_list = []
        d = self.vertex_list.copy()
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
        temp = 0
        while len(l_list)!=len(languages_list):
            c = self.find_max(d)
            cand_l.append(c)
            l_list += d[c]
            del(d[c])
            d = self.adj_d(d, l_list)

        min_hire_count = len(cand_l)
        print("--------Function displayHireList--------", file=self.f)
        print("No of candidates required to cover all languages: {}".format(min_hire_count), file=self.f)
        for c in cand_l:
            temp = [self.vertices[c][0]]
            for l in self.vertex_list[c]:
                temp.append(self.vertices[l][0])

            print("/".join(temp), file=self.f)

        print("-----------------------------------------\n", file=self.f)

    def adj_d(self, d, l_list):
        temp = {}
        for c, l in d.items():
            temp_l = None
            for ll in l_list:
                if ll in l:
                    l.remove(ll)
            temp[c] = l
        return temp

    def find_max(self, d):
        s = 0
        k = None
        for c, l in d.items():
            t = len(l)
            if s<t:
                s=t
                k=c
        return k

    def displayCandidates(self, lang):
        language_vertex = (lang, "language")
        language_index = self.vertices.index(language_vertex)
        print("--------Function displayCandidates --------", file=self.f)
        print("List of Candidates who can speak {}:".format(lang), file=self.f)
        for candidate_index in range(len(self.edges[language_index])):
            if self.edges[language_index][candidate_index]:
                print(self.vertices[candidate_index][0], file=self.f)
        print("-----------------------------------------\n", file=self.f)

    def findDirectTranslator(self, langA, langB):
        print("--------Function findDirectTranslator --------", file=self.f)
        print("Language A: {}".format(langA), file=self.f)
        print("Language B: {}".format(langB), file=self.f)
        answer = "No"
        i = self.vertices.index((langA, "language"))
        j = self.vertices.index((langB, "language"))
        temp = None
        for c, lang in self.vertex_list.items():
            if i in lang and j in lang:
                temp = c

        if temp is not None:
            print("Direct Translator: Yes, {} can translate.".format(self.vertices[temp][0]), file=self.f)
        else:
            print("Direct Translator: No.", file=self.f)

        print("-----------------------------------------\n", file=self.f)

    def findTransRelation(self, langA, langB):

        print("--------Function findTransRelation --------", file=self.f)
        print("Language A: {}".format(langA), file=self.f)
        print("Language B: {}".format(langB), file=self.f)
        answer = "No"
        flag, transList = self.BFS(langA, langB)

        if flag:
            new_trans = []
            for i in transList:
                new_trans.append(i)
                if i == langB:
                    break
            print("Related: Yes, {}".format(">".join(new_trans)), file=self.f)
        else:
            print("Related: No.", file=self.f)
        print("-----------------------------------------", file=self.f)

    def BFS(self, s, e):
        # Mark all the vertices as not visited
        visited = [False] * len(self.vertices)
        s_index = self.vertices.index((s, "language"))
        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s_index)
        visited[s_index] = True
        e_index = self.vertices.index((e, "language"))
        tranSlist = []
        tranSlist.append(s)

        while queue:
            # Dequeue a vertex from
            # queue and print it
            n = queue[0]
            queue = queue[1:]

            if n == e_index:
                return True, tranSlist


            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in range(len(self.edges[n])):
                if not visited[i]:
                    queue.append(i)
                    tranSlist.append(self.vertices[i][0])
                    visited[i] = True

        return False, tranSlist
