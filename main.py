from node import MarkovChain,addCSVFile,addPickleFile

chain=MarkovChain()

while True:
    print("\n1: Add transition")
    print('2: Print transition probabilities')
    print('3: Save chain to pickle')
    print('4: Save chain to CSV')
    print('5: Exit\n')
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
        chain.saveChainPickle(fileName)
    elif option==4:
        fileName=input('\nEnter filename: ')
        chain.saveChainCSV(fileName)
    elif option==5:
        break
    else:
        print("Invalid option\n")
