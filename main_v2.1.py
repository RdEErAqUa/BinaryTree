binaryTree = {'right' : None, 'element' : None, 'left' : None, 'parent' : None}
binaryTreeList = [None]

test = [None]

"""
v 2.1
Добавленно удаление корня
Добавленно балансування елемента
"""


def ElementExist(binaryTreeElement, element):
    if(binaryTreeElement == None):
        return False
    if str(binaryTreeElement['element']) == str(element):
        return True
    else:
        inRight = ElementExist(binaryTreeElement['right'], element)
        inLeft = ElementExist(binaryTreeElement['left'], element)
    if inRight or inLeft:
        return True
    else:
        return False


def addElement(binaryTreeList, element):
    binaryElementAdd = {'right' : None, 'element' : element, 'left' : None, 'parent' : None}

    if (len(binaryTreeList) == 0):
        binaryTreeList = [None]

    elementWhile = binaryTreeList[0]

    if(elementWhile == None):
        binaryTreeList[0] = binaryElementAdd
    else:
        tempElemenet = None
        while elementWhile != None:
            if elementWhile['element'] > element:
                tempElemenet = elementWhile
                elementWhile = elementWhile['left']
            else:
                tempElemenet = elementWhile
                elementWhile = elementWhile['right']
        binaryElementAdd['parent'] = tempElemenet
        if tempElemenet['element'] > element:
            tempElemenet['left'] = binaryElementAdd
        else:
            tempElemenet['right'] = binaryElementAdd
        binaryTreeList.append(binaryElementAdd)
    return binaryTreeList


def removeElement(binaryTreeList, binaryTree, element):
    for el in binaryTreeList:
        if el['element'] == element:
            if el['right'] == None and el['left'] == None:
                if (el['parent'] != None):
                    el['parent']['right'] = None if el['parent']['right'] == el else el['parent']['right']
                    el['parent']['left'] = None if el['parent']['left'] == el else el['parent']['left']
                binaryTreeList.remove(el)
            elif el['right'] == None or el['left'] == None:
                if el['right'] != None:
                    if (el['parent'] != None):
                        el['parent']['right'] = el['right'] if el['parent']['right'] == el else el['parent']['right']
                        el['parent']['left'] = el['right'] if el['parent']['left'] == el else el['parent']['left']
                    else:
                        el['right']['parent'] = None
                else:
                    if(el['parent'] != None):
                        el['parent']['right'] = el['left'] if el['parent']['right'] == el else el['parent']['right']
                        el['parent']['left'] = el['left'] if el['parent']['left'] == el else el['parent']['left']
                    else:
                        el['left']['parent'] = None

                binaryTreeList.remove(el)
            else:
                replaceElement = el['right']
                while replaceElement['left'] != None:
                    replaceElement = replaceElement['left']
                tempElem = replaceElement['right']
                if(replaceElement != el['right']):
                    replaceElement['right'] = el['right']
                replaceElement['left'] = el['left']
                replaceElement['parent']['left'] = tempElem
                if(el['parent'] != None):
                    el['parent']['right'] = replaceElement if el['parent']['right'] == el else el['parent']['right']
                    el['parent']['left'] = replaceElement if el['parent']['left'] == el else el['parent']['left']
                else:
                    binaryTreeList.remove(replaceElement)
                    binaryTreeList.insert(0, replaceElement)
                binaryTreeList.remove(el)


#addElement(binaryTreeList, 8)
#addElement(binaryTreeList, 3)
#addElement(binaryTreeList, 10)
#addElement(binaryTreeList, 1)
#addElement(binaryTreeList, 6)
#addElement(binaryTreeList, 14)
#addElement(binaryTreeList, 4)
#addElement(binaryTreeList, 7)
#addElement(binaryTreeList, 13)

def zrs(binaryTreeList):
    average = 0.0
    for i in binaryTreeList:
        average += float(i['element'])
    average = average / len(binaryTreeList)

    sz = abs(binaryTreeList[0]['element'] - average)
    df = 0
    pos = 0
    for i in range(0, len(binaryTreeList)):
        if abs(binaryTreeList[i]['element'] - average) < sz:
            pos = i
            sz = abs(binaryTreeList[i]['element'] - average)
    newBinaryTreeList = []
    newBinaryTreeList = addElement(newBinaryTreeList, int(binaryTreeList[pos]['element']))

    for i in binaryTreeList:
        if binaryTreeList[pos]['element'] != i['element']:
            newBinaryTreeList = addElement(newBinaryTreeList, int(i['element']))
    return newBinaryTreeList
#removeElement(binaryTreeList, binaryTree, 4)

while True:
    print("Введіть команду(-? для допомоги)")
    name = input()
    if name == "-?":
        print("-num (викликати команду додавання елементу)")
        print("-delnum (викликати команду видалення елементу)")
        print("-show (вивести результат)")
    elif "-num" == name:
        print("Введіть число для добавлення(cancel для виходу)")
        while True:
            number = input()
            if number == "cancel":
                break
            if not ElementExist(binaryTreeList[0], number):
                binaryTreeList = addElement(binaryTreeList, int(number))
                binaryTreeList = zrs(binaryTreeList)


            else:
                print("Already exist")
    elif "-delnum" == name:
        print("Введіть число для видалення")
        number = input()
        removeElement(binaryTreeList, binaryTree, int(number))
    elif "-show" == name:
        for el in binaryTreeList:
            print("\n", el['element'], end=': ')
            if el['left'] != None:
                print("l-", el['left']['element'], end=' ')
            if el['right'] != None:
                print("r-", el['right']['element'], end=' ')