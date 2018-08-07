from node import MarkovChain

chain=MarkovChain()

while True:
    print("1: Add transition")
    print('2: Print transition probabilities')
    print('3: Exit')
    option=input('Enter option number: ')
    if option==1:
        originNode=input('Enter origin node: ')
        destinationNode=input('Enter destination node: ')
        chain.addMovement(originNode,destinationNode)
    elif option==2:
        chain.printTransitionProbs()
    elif option==3:
        break
    else:
        print("Invalid option")
