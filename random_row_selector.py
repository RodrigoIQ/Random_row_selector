#libaries
import pandas as pd
import os 
import random
from datetime import datetime

def main():
    os.system('cls||clear')

    print("Random Row Selector")
    today = datetime.today()
    print(today)

    path = str(input("\n\nFile: "))
    path = path.replace('"','')
    print(path)

    #get excel file
    original_file = pd.ExcelFile(path)
    sheet_namess= original_file.sheet_names

    i = 1 
    for sheet in sheet_namess:
        print(f"{i} = {sheet}, ", end = "")
        i = i+1
    
    print("\n")

    Sheet_Num = int(input("Please select sheet number: "))
    Sheet_Num = Sheet_Num-1
    print(sheet_namess[Sheet_Num])

if __name__ == "__main__":
    main()