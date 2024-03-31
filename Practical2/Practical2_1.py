# Python strings splice work like :-
# [starting index:ending index]
# [len()-negative start:len()-negative end]
# python automatically puts the len if we write any negative index and results after reducing it

str="Python"
for i in range(1,len(str)+1):
    print(str[:i])
