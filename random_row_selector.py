#libaries
import pandas as pd
import os 
import random
from datetime import datetime

if __name__ == "__main__":
    os.system('cls||clear')

    print("Random Row Selector")
    today = datetime.today()
    print(today)

    path = str(input("\n\nFile: "))
    path = path.replace('"','')
    print(path)
