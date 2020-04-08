import random
#1->rock
#2->paper
#3->scissors
i=1
s12=s21=s13=s31=s14=s41=s23=s32=s24=s42=s34=s43=0
while(i<=50):
    print("----------------------round",i,"----------------------")
    n12=n21=n13=n31=n14=n41=n23=n32=n24=n42=n34=n43=0
    n1=random.randint(1,3)
    n2=random.randint(1,3)
    n3=random.randint(1,3)
    n4=random.randint(1,3)
    print("         player one choice:",n1)
    print("         player two choice:",n2)
    print("         player three choice:",n3)
    print("         player four choice:",n4)
    if(n1==1):
        if(n2==2):
            n21+=1
        if(n3==2):
            n31+=1
        if(n4==2):
            n41+=1
        if(n2==3):
            n12+=1
        if(n3==3):
            n13+=1
        if(n4==3):
            n14+=1
    if(n1==2):
        if(n2==1):
            n12+=1
        if(n3==1):
            n13+=1
        if(n4==1):
            n14+=1
        if(n2==3):
            n21+=1
        if(n3==3):
            n31+=1
        if(n4==3):
            n41+=1
    if(n1==3): 
        if(n2==2):
            n12+=1
        if(n3==2):
            n13+=1
        if(n4==2):
            n14+=1
        if(n2==1):
            n21+=1
        if(n3==1):
            n31+=1
        if(n4==1):
            n41+=1
    if(n2==1):
        if(n3==2):
            n32+=1
        if(n4==2):
            n42+=1
        if(n3==3):
            n23+=1
        if(n4==3):
            n24+=1
    if(n2==2):
        if(n3==1):
            n23+=1
        if(n4==1):
            n24+=1
        if(n3==3):
            n32+=1
        if(n4==3):
            n42+=1
    if(n2==3): 
        if(n3==2):
            n23+=1
        if(n4==2):
            n24+=1
        if(n3==1):
            n32+=1
        if(n4==1):
            n42+=1
    if(n3==1):
        if(n4==2):
            n43+=1
        if(n4==3):
            n34+=1
    if(n3==2):
        if(n4==1):
            n34+=1
        if(n4==3):
            n43+=1
    if(n3==3): 
        if(n4==2):
            n34+=1
        if(n4==1):
            n43+=1
    s12+=n12
    s21+=n21
    s13+=n13
    s31+=n31
    s14+=n14
    s41+=n41
    s23+=n23
    s32+=n32
    s24+=n24
    s42+=n42
    s34+=n34
    s43+=n43
    if(n12>0):
    	print("         player one won on player two")
    if(n13>0):
    	print("         player one won on player three")
    if(n14>0):
        print("         player one won on player four")
    if(n21>0):
        print("         player two won on player one")
    if(n23>0):
    	print("         player two won on player three")
    if(n24>0):
    	print("         player two won on player four")
    if(n31>0):
        print("         player three won on player one")
    if(n32>0):
        print("         player three won on player two")
    if(n34>0):
    	print("         player three won on player four")
    if(n41>0):
    	print("         player four won on player one")
    if(n42>0):
        print("         player four won on player two")
    if(n43>0):
        print("         player four won on player three")
    i+=1
print("*****************overal results********************")
print("         winnings of player one on player two is",s12)
print("         winnings of player one on player three is",s13)
print("         winnings of player one on player four is",s14)
print("         winnings of player two on player one is",s21)
print("         winnings of player two on player three is",s23)
print("         winnings of player two on player four is",s24)
print("         winnings of player three on player one is",s31)
print("         winnings of player three on player two is",s32)
print("         winnings of player three on player four is",s34)
print("         winnings of player four on player one is",s41)
print("         winnings of player four on player two is",s42)
print("         winnings of player four on player three is",s43)
   
        

    
