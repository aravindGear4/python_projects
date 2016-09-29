def validate(tic, r,c):
    res = False
    if ((r<3 and r>-1 and c<3 and c>-1)):
        if(tic[r][c] == ' '):
                res=True
    return res

def checkForWinner(tic, char):
    result=False;
    #horizontal
    for line in tic:
        if(line[0]==char and line[1] == char and line[2] == char):
            result= True
            break
    #vertical
    if(not result):
        for col in range(3):
            if(tic[1][col] == char and tic[2][col] == char and tic[0][col] ==char):
                result=True
                break
                 #two cross
    if(not result):
        if(tic[1][1]==char and ((tic[0][0] == char and tic[2][2] == char) or (tic[2][0]==char and tic[0][2] == char))):
            result = True
    return result;

def disp(a):
    print '\n'
    for line in a:
        print line[0]+' | '+line [1]+' | '+ line[2]+ '\n'

#intialize
tic = [[' ' for temp1 in range(3)] for tempArray in range(3)]
players = input("Enter player names:")
symbols = input("Enter symbols to use(order is same as the player names:)")

#start loop
while True:
    for index in range(2):
#player 1
        print '-------------------------------------------------'
#ask input position and validate
        while(True):
            disp(tic)
            r,c = input('Oi, '+players[index]+'!!\nWhere do you want to mark \''+symbols[index]+'\',')
            if(validate(tic,r-1,c-1)):
                break
        tic[r-1][c-1]=symbols[index]
        disp(tic)
        if(checkForWinner(tic,symbols[index])):
            print 'Yey! '+players[index]+' is the winner. You Suck '+players[index-1]+'.'
            break
'''
#print '-------------------------------------------------------'
 #player 2
 #ask input position and validate
    while True:
        disp(tic)
        r,c = input('Oi, Player2!!\nWhere do you want to mark \'0\',')
        if(validate(tic,r-1,c-1)):
            break
    tic[r-1][c-1]='0'
    if(checkForWinner(tic,'0')):
        print 'Yey! palyer2 is the winner. You Suck player 1.'
        break
#end loop
'''