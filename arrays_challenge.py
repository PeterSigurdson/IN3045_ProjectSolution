# Project Bonus Question: Arrays

names_array = ['Jordan', 'Debbie', 'John', 'Jenelle', 'Tony', 'Suzan', 'Tim','Alicia', 'Jordan', 'Jeff']

print("length of names_array is " + str(len(names_array)))
print("instructors: ", names_array)
searchForWho = input("Who are you searching for? ")

for i in range(0, len(names_array)):
    thisName = names_array[i]
    
    if (thisName.find(searchForWho) > -1):
        print('found it....', searchForWho, " in Position ", i)
        
    # NOTE: FOR FULL MARKS, ADD CODE TO PRINT OUT A MESSAGE FOR THE CASE THAT THE 
    # INSTRUCTOR IS NOT FOUND IN THE ARRAY!

    
    