class CountCapitalLetters:
    numberOfCapitalLetters=0
    def counter(self,str):
        for i in range(len(str)):
            if(str[i]>='A' and str[i]<='Z'):
                CountCapitalLetters.numberOfCapitalLetters +=1
data=CountCapitalLetters()
Input=input("Enter the String")
data.counter(Input)
print(CountCapitalLetters.numberOfCapitalLetters)
