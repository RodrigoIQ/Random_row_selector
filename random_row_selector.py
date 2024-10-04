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
    sheet_names= original_file.sheet_names

    i = 1 
    for sheet in sheet_names:
        print(f"{i} = {sheet}, ", end = "")
        i = i+1
    
    print("\n")

    Sheet_Num = int(input("Please select sheet number: "))
    Sheet_Num = Sheet_Num-1
    print(sheet_names[Sheet_Num])

    # get data from excel sheet 
    df = pd.read_excel (path,sheet_name=sheet_names[Sheet_Num])
    print(f"Universe size = {df.shape[0]}")
    Sample_sizes = int(input("Sample size: "))

    ran_list = random.sample(range(df.shape[0]),k = Sample_sizes)
    ran_list = sorted(ran_list)

    df2 = df.iloc[ran_list]

    path2= path.partition(".")
    print(fr"{path2[0]}-Random-{today}.xlsx")

    # df2.to_excel(f"{path2[0]}-Random-{today}.xlsx",sheet_name='Sheet_1') 
    


if __name__ == "__main__":
    main()