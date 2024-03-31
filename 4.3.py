count=0
print("Working of break statement: ")
while(count<11):
    if(count==4):
        break
    print(count)
    count=count+1
    
count=0
print("Working of continue statement: ")
while(count<11):
    count=count+1
    if(count==4):
        continue
    print(count)
