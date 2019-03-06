def Play():
  import random, time
  accept=False
  NumsMatched=0
  verifedNums=False
  if game==True:
    lk1=random.randint(1,50)
    lk2=random.randint(1,50)
    lk3=random.randint(1,50)
    lk4=random.randint(1,50)
    lk5=random.randint(1,50)
    lk6=random.randint(1,50)
    print("Time to pick your six lottery numbers")
    pk1=int(input("Enter your first lottery number: "))
    pk2=int(input("Enter your second lottery number: "))
    pk3=int(input("Enter your third lottery number: "))
    pk4=int(input("Enter your fourth lottery number: "))
    pk5=int(input("Enter your fifth lottery number: "))
    pk6=int(input("Enter your sixth lottery number: "))
    while verifedNums==False:
      verifedNumsNum=0
      if pk1>=1 and pk1<=50:
        verifedNumsNum+=1
      else:
        pk1=int(input("Enter your first lottery number: "))
      
      if pk2>=1 and pk2<=50:
        verifedNumsNum+=1
      else:
        pk2=int(input("Enter your second lottery number: "))
      
      if pk3>=1 and pk3<=50:
        verifedNumsNum+=1
      else:
        pk3=int(input("Enter your third lottery number: "))
      
      if pk4>=1 and pk4<=50:
        verifedNumsNum+=1
      else:
        pk4=int(input("Enter your fourth lottery number: "))
      
      if pk5>=1 and pk5<=50:
        verifedNumsNum+=1
      else:
        pk5=int(input("Enter your fifth lottery number: "))
      
      if pk6>=1 and pk6<=50:
        verifedNumsNum+=1
      else:
        pk6=int(input("Enter your sixth lottery number: "))
        
      if verifedNumsNum==6:
        verifedNums=True
      else:
        verifedNums=False
    print("Checking...")
    if verifedNums==True:
      print("Players Numbers = "+str(pk1)+" "+str(pk2)+" "+str(pk3)+" "+str(pk4)+" "+str(pk5)+" "+str(pk6))
      print("Correct Numbers = "+str(lk1)+" "+str(lk2)+" "+str(lk3)+" "+str(lk4)+" "+str(lk5)+" "+str(lk6))
      if lk1==pk1:
        NumsMatched+=1
      if lk2==pk2:
        NumsMatched+=1
      if lk3==pk3:
        NumsMatched+=1
      if lk4==pk4:
        NumsMatched+=1
      if lk5==pk5:
        NumsMatched+=1
      if lk6==pk6:
        NumsMatched+=1
      if NumsMatched==0:
        print("Better luck next time\n0/6")
      elif NumsMatched==1:
        print("One matched :p\n1/6")
      elif NumsMatched==2:
        print("Two out of six matched...\n2/6")
      elif NumsMatched==3:
        print("Three out of six is really good. That means one half were correct!\n3/6")
      elif NumsMatched==4:
        print("Four out of six!! How many tries did that take.\n4/6")
      elif NumsMatched==5:
        print("Five out of six!!! SO CLOSE XD\n5/6")
      elif NumsMatched==6:
        print("WINNER!!!! Six out of six. What are the chances of that.\n6/6")
      print("Do you want to play again?")
      accept=False
      retry=False
      while accept==False:
        playing=input("")
        if playing=='yes' or playing=='Yes' or playing=='y' or playing=='Y':
          retry=True
          accept=True
        elif playing=='no' or playing=='No' or playing=='n' or playing=='N':
          retry=False
          accept=True
      if retry==True:
        Play()
      elif retry==False:
        quit
  elif game==False:
    quit


accept=False
print("Do you want to play this lotto game?")
while accept==False:
  
  playing=input("")
  if playing=='yes' or playing=='Yes' or playing=='y' or playing=='Y':
    game=True
    accept=True
    Play()
  elif playing=='no' or playing=='No' or playing=='n' or playing=='N':
    game=False
    accept=True
    quit
