field=[[0,0,0,0,0,0],
        [0,7,8,5,4,0],
       [0,8,7,5,7,0],
       [0,8,8,6,9,0],
       [0,9,6,7,9,0],
       [0,0,0,0,0,0]]

min=3
checked=[[1,1]]
while len(checked)>0:
    for i in range(len(checked)):
        newchecked=[]
        print('we check '+str(checked[i][0])+","+str(checked[i][1]))
        if field[checked[i][0]+1][checked[i][0]]>min and field[checked[i][0]][checked[i][0]+1]>min and field[checked[i][0]+1][checked[i][0]+1]>min:
                print('good')
                field[checked[i][0]][checked[i][1]]=9
            newchecked.append([])
        checked=newchecked

print(field)