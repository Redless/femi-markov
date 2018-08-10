from node import MarkovChain,addCSVFile,addPickleFile

chain=MarkovChain()

while True:
    print("\n1: Add transition")
    print('2: Print transition probabilities')
    print('3: Print transition matrix')
    print('4: Print steady-state probabilities')
    print('5: Open chain from pickle')
    print('6: Open chain from CSV')
    print('7: Save chain to pickle')
    print('8: Save chain to CSV')
    print('9: Exit\n')
    option=int(input('Enter option number: '))
    if option==1:
        originNode=input('\nEnter origin node: ')
        destinationNode=input('Enter destination node: ')
        chain.addMovement(originNode,destinationNode)
    elif option==2:
        print('\n',end='')
        chain.printTransitionProbs()
    elif option==3:
        print('\n',end='')
        chain.printTransitionMatrix()
    elif option==4:
        print('\n',end='')
        chain.getSteadyState()
    elif option==5:
        fileName=input('\nEnter filename: ')
        chain=addPickleFile(fileName)
    elif option==6:
        fileName=input('\nEnter filename: ')
        chain=addCSVFile(fileName)
    elif option==7:
        fileName=input('\nEnter filename: ')
        chain.saveChainPickle(fileName)
    elif option==8:
        fileName=input('\nEnter filename: ')
        chain.saveChainCSV(fileName)
    elif option==9:
        break
    else:
        print("Invalid option\n")
