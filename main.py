import re

class lexer():
    def Tokenize(input):
        colinRegex = re.compile("([a-z][a-z]+|\d+|\<|\+|-)")

        identifier = re.compile("[a-z][a-z]+")  # Regex for detecting identifiers
        integer = re.compile("\d")  # Regex for detecting digits
        assignment = re.compile("<")  # Regex for detecting assignments
        operator = re.compile("\+|-")  # Regex for detecting operators

        tokens = re.findall(colinRegex, input)  # This creates a list of all matched tokens in the input
        tokensAndRules = []

        for element in tokens:  # This creates a list with our tokens matched to the rules that were used on them (contained in a tuple)
            if re.match(identifier, element):
                tokensAndRules.append((element, "<identifier>"))
            elif re.match(integer, element):
                tokensAndRules.append((element, "<integer>"))
            elif re.match(assignment, element):
                tokensAndRules.append((element, "<assignment>"))
            else:
                tokensAndRules.append((element, "<operator>"))

        print(tokensAndRules)
        return tokensAndRules

class Node():  # Node contains its value as well as it's potential children
    def __int__(self, val):
        self.val = val
        self.nodes = []

    def addNode(self, newVal):
        self.nodes = self.nodes.append(newVal)

class parseTree():
    def __int__(self, root):
        self.root = Node(root)  # Defining our root value in our node

class descent():

    def Parse(input):
        identifier = re.compile("[a-z][a-z]+")
        integer = re.compile("\d")
        assignment = re.compile("<")
        operator = re.compile()
        literal = re.compile("\d|[a-z][a-z]+")
        expr = re.compile("(\d|[a-z][a-z]+)")

        if len(input) != 0:
            tree = parseTree("<program>")
            i = 0
            while i < len(input):
                #if re.match(identifier, input[i][0]) & re.match(assignment, input[i+1][0])


lexer.Tokenize("5 HYPERPARATHYROIDisM < 99 COUNTERinTELLIGIENCE the PURPLE Wcontext ofFICIAL POLYmath")