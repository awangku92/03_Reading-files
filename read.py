# this is a function to read large file and split to chunks\

import pandas as pd
import os

def read_csv():
    root = "C:\\Users\\User\\Desktop\\Python Tutorial\\03_Reading files\\"

    # create data_frame
    # dataPath = root+"dataFile\\Comma-Separated.txt"
    dataPath = os.path.join(os.getcwd(), "dataFile\\Comma-Separated.txt")
    print(type(os.getcwd()))
    # This is when data dont have header, Default is have header
    # df = pd.read_csv(root+dataPath, header=None) 
    df = pd.read_csv(dataPath)
    print(df.head()) # can specify number of column in df.head(n)

    return



# main method
def main():
    data = read_csv()
    #read_csv()
    # mapping()
    # indexing(data)

if __name__ == '__main__':
    main()