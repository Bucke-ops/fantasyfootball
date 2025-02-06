import csv

stats = "FFStats.csv"
with open(stats,'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        print(row)


def main():
    print("Hello and welcome to Fantasy Football 25")

def decision():  
    answer = str(input("Would you like to create or join a league?: "))
    if (answer == "Create"):
        creation()
    elif(answer == "CREATE"):
        creation()
    elif(answer == "create"):
        creation()
    elif(answer == "Join"):
        newAnswer = str(input("Which one?: "))
        print(newAnswer)
    elif(answer == "JOIN"):
        newAnswer = str(input("Which one?: "))
        print(newAnswer)
    elif(answer == "join"):
        newAnswer = str(input("Which one?: "))
        print(newAnswer)
def creation():
    leagueName = str(input("What would you like the name of the league to be?\n"))
    leagueMembers = int(input("How many members will be participating in your league?\n"))
    draftDay = str(input("What day will the draft be set for? (MM/DD/YYYY)\n"))
    print("Your league name is "+leagueName+", the amount of members in the league are "+str(leagueMembers)+", and the draft day is set for "+draftDay)
    decisionCreation = str(input("Is this correct? (Yes/No)\n"))
    if(decisionCreation == "Yes"):
        print("Ok, your info is set")
        print("Your league name is "+leagueName+", the amount of members in the league are "+str(leagueMembers)+", and the draft day is set for "+draftDay)
    elif(decisionCreation == "No"):
       leagueName = str(input("What would you like the name of the league to be?\n"))
       leagueMembers = int(input("How many members will be participating in your league?\n"))
       draftDay = str(input("What day will the draft be set for? (MM/DD/YYYY)\n"))



#main()
#decision()
