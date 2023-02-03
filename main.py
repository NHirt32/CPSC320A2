import re

class lexer():
    def Tokenize(input):
        colinRegex = re.compile("([a-z][a-z]+|\d+|\<|\+|-)") #Super regex used for initial list creation

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

    def progParse(self, inputList):
            index = -1;
            match self.lookAhead(inputList, index):
                case "<integer>>":
                    index += 1
                    self.integerParse()
                    return
                case "<operator>":
                    index += 1
                    self.operatorParse()
                case _:
                    return

        return

    def save_varParse(self, inputList, index):
        return

    def exprParse(self, inputList, index):
        return

    def literalParse(self, inputList, index):
        return

    def integerParse(self, intTuple):
        if intTuple[1] == "<integer>":          #If we are dealing with an integer
            intTree = parseTree("<integer>")    #Create a node with the <integer> value
            intTree.addNode(intTuple[0])        #Create a child node with whatever the actual value is from the input tuple
            return intTree
        return False    #The input tuple did not match our method

    def identifierParse(self, identifierTuple):
        if identifierTuple[1] == "<identifier>":              #If we are dealing with an identifier
            identifierTree = parseTree("<identifier>")        #Create a node with the <identifier> value
            identifierTree.addNode(identifierTuple[0])        #Create a child node with whatever the actual value is from the input tuple
            return identifierTree
        return False    #The input tuple did not match our method

    def operatorParse(self, operatorTuple):
        if operatorTuple[1] == "<operator>":        # If we are dealing with an operator
            operatorTree = parseTree("<operator>")  # Create a node with the <operator> value
            operatorTree.addNode(operatorTuple[0])  # Create a child node with whatever the actual value is from the input tuple
            return operatorTree
        return  False   #The input tuple did not match our method

    def assignmentParse(self, assignmentTuple):
        if assignmentTuple[1] == "<assignment>":      # If we are dealing with an assignment
            assignmentTree = parseTree("<assignment>")  # Create a node with the <assignment> value
            assignmentTree.addNode(assignmentTuple[0])  # Create a child node with whatever the int value is from the input tuple
            return assignmentTree
        return  False   #The input tuple did not match our method

    def lookAhead(self, inputList, currentIndex):   #This method looks ahead to the next token to see it's classification
        return inputList[currentIndex+1][1]

    def Parse(self, input):
        identifier = re.compile("[a-z][a-z]+")
        integer = re.compile("\d")
        assignment = re.compile("<")
        #literal = re.compile("\d|[a-z][a-z]+")
        #expr = re.compile("(\d|[a-z][a-z]+)")

        if len(input) != 0:
            tree = parseTree("<program>")
            self.progParse()rogParse()



lexer.Tokenize("5 HYPERPARATHYROIDisM < 99 COUNTERinTELLIGIENCE the PURPLE Wcontext ofFICIAL POLYmath")