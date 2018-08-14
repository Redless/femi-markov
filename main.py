from node import MarkovChain,addCSVFile,addPickleFile,addMatrix

chain=MarkovChain()

while True:
    print("\n1: Add transition")
    print('2: Print transition probabilities')
    print('3: Print transition matrix')
    print('4: Open chain from pickle')
    print('5: Open chain from CSV')
    print('6: Save chain to pickle')
    print('7: Save chain to CSV')
    print('8: Exit\n')
    option=int(input('Enter option number: '))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if option==1:
        originNode=input('\nEnter origin node: ')
        destinationNode=input('Enter destination node: ')
        chain.addMovement(originNode,destinationNode)
    elif option==2:
        print('\n')
        chain.printTransitionProbs()
    elif option==3:
        print('\n')
        chain.printTransitionMatrix()
    elif option==4:
        fileName=input('\nEnter filename: ')
        chain=addPickleFile(fileName)
    elif option==5:
        fileName=input('\nEnter filename: ')
        chain=addCSVFile(fileName)
    elif option==6:
        fileName=input('\nEnter filename: ')
        chain.saveChainPickle(fileName)
    elif option==7:
        fileName=input('\nEnter filename: ')
        chain.saveChainCSV(fileName)
    elif option==8:
        break
    else:
        print("Invalid option\n")
