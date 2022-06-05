



import random

def loadInsults() :
  f1 = open("assignment3_word1.txt", 'r')
  f2 = open("assignment3_word2.txt", 'r')
  f3 = open("assignment3_word3.txt", 'r')

  adj1 = f1.readlines()
  adj2 = f2.readlines()
  noun = f3.readlines()

  insulttuple = adj1, adj2, noun
  return insulttuple

def generateInsult(insulttuple) :
  adj1, adj2, noun = insulttuple
  a = random.randint(0,49)
  b = random.randint(0,49)
  c = random.randint(0,49)
  a1 = adj1[a].rstrip("\n")
  a2 = adj2[b].rstrip("\n")
  v = noun[c].rstrip("\n")
  insult = "Thou " + a1 + " " + a2 + " " + v + "!"
  return insult

def generateInsults(insulttuple, num = 1000) :
  list = []
  for x in range (num):
    a = insult[0][random.randint(0,49)]
    b = insult[1][random.randint(0,49)]
    c = insult[2][random.randint(0,49)]
    a = 
#def displaySomeInsults(insults) :

#def saveInsults(insults) :

#def checkInsultsFile() :

#def getNumInsults() :

def main() :
    random.seed()
    # Using default arguments wherever possible.  Input files: word1.txt,
    # word2.txt, word3.txt.  1000 insults generated, saved to file Insults.txt.
    # allWords is a tuple of three lists.
    allWords = loadInsults()
    print("One insult: ", end="")
    print(generateInsult(allWords))
    insults = generateInsults(allWords)
    displaySomeInsults(insults)
    saveInsults(insults)
    if checkInsultsFile() :
        print("\n1000 insults properly saved. They are unique and in order.")
    else :
        print("\nThe insults are not properly generated or saved!")

    # Using all possible arguments and prompting the user for the number of insults.
    allWords = loadInsults("word1.txt", "word2.txt", "word3.txt")
    numInsults = getNumInsults()
    insults = generateInsults(allWords, numInsults)
    displaySomeInsults(insults)
    saveInsults(insults, "Insults.txt")
    if checkInsultsFile(numInsults, "Insults.txt") :
        print("\n" + str(numInsults) + " insults properly saved. They are unique and in order.")
    else :
        print("\nThe insults are not properly generated or saved!")

# Write your functions here:


main()