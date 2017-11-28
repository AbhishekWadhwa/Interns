import xlsxwriter
wb=xlsxwriter.Workbook('Details.xlsx')
ws=wb.add_worksheet()
class ExcelFile:
    def makeExcel(self,inputList):
        ws.write(0, 0,"First Name")
        ws.write(0, 1, "Last Name")
        ws.write(0, 2, "Date of birth")
        ws.write(0, 3, "city")
        lengthOfinputList=len(inputList)
        rowStart=1
        colStart=0
        for i in range(lengthOfinputList):
            ws.write(rowStart, colStart,inputList[i][0])
            ws.write(rowStart, colStart+1, inputList[i][1])
            ws.write(rowStart, colStart+2, inputList[i][2])
            ws.write(rowStart, colStart+3, inputList[i][3])
            rowStart+=1
        wb.close()
    def inputUserDetails(self,numberOfEntries):
        list1=[]
        listTemp=[]
        for i in range(numberOfEntries):
            firstName=input("Your First Name\n")
            lastName=input("Your Last Name\n")
            dateOfBirth=input("Your DOB\n")
            city=input("Your city\n")
            list2=[firstName,lastName,dateOfBirth,city]
            listTemp=[list2]
            list1[len(list1):]=listTemp
        return list1
excelSheet=ExcelFile()
totalNumberOfEntries=int(input("Enter Total Number Of Entries\n"))
Input=excelSheet.inputUserDetails(totalNumberOfEntries)
excelSheet.makeExcel(Input)