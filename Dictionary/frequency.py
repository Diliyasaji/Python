def count(elements):
    if(elements[-1] == "."):
        elements = elements[0:len(elements)-1]
    if(elements in frequency):
        frequency[elements] +=1
    else:
        frequency.update({elements:1})



string = input("Enter a string : ")
words = string.split()

frequency = {}
for elements in words:
    count(elements)

for i in frequency:
    print("\nFrequency of ",i," : ",frequency[i])
