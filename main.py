from node import MarkovChain

chain=MarkovChain()

while True:
    print("\n1: Add transition")
    print('2: Print transition probabilities')
    print('3: Save chain')
    print('4: Exit\n')
    option=int(input('Enter option number: '))
    if option==1:
        originNode=input('\nEnter origin node: ')
        destinationNode=input('Enter destination node: ')
        chain.addMovement(originNode,destinationNode)
    elif option==2:
        print('\n',end='')
        chain.printTransitionProbs()
    elif option==3:
        fileName=input('\nEnter filename: ')
        chain.saveChain(fileName)
    elif option==4:
        break
    else:
        print("Invalid option\n")
