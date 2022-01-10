data=[["a",'a','a','a','b','c','x','a'],
      ['b','v','b','c','a','d','v','d'],
      ['x','x','c','x','x','d','b','b'],
      ['v','c','d','v','c','x','a','c'],
      ["a",'a','c','d','e','e','c','d']]

      

def createDic(col1,col2,data):
    result={}
    for i in range(len(data[col1])):
        if data[col1][i] in result:
            result[data[col1][i]].append(data[col2][i])
        else:
            result[data[col1][i]]=[data[col2][i]]
    print(result)
    print(check(result)) 

def check(diction): 
    for item in diction:
        diction[item]= list(set(diction[item]))
        if len(diction[item])>1:
            return False
    return True

def doublecol(col1,col2,data):
    newlist=[]
    for i in range(len(data[col1])):
        newlist.append(data[col1][i]+data[col2][i])
    data.append(newlist)
    return data

#A->E
createDic(0,4,data)

#  CE->A
data= doublecol(2,4,data)
createDic(-1,0,data)

#BD->C
data= doublecol(1,3,data)
createDic(-1,2,data)

#BD ->AC
data= doublecol(0,2,data)
createDic(-2,-1,data)