# this is a function to read large file and split to chunks
# use splitfile() for txt - by size
# use chunk()  for csv    - by row

import pandas as pd
import os

def read_file():
    # root = "C:\\Users\\User\\Desktop\\Python Tutorial\\03_Reading files\\"
	# dataPath = root+"dataFile\\Comma-Separated.txt"

    # GET PATH
    # os.getcwd() #get current working directory
    dataPath = os.path.join(os.getcwd(), "dataFile\\Comma-Separated.txt") # 758 lines include header
    processedPath = os.path.join(os.getcwd(), "processedData\\")
    # print(type(os.getcwd())) # type() - to get datatype

    # create data_frame
    # This is when data dont have header, Default is have header
    # df = pd.read_csv(root+dataPath, header=None) 
    # df = pd.read_csv(dataPath)
    # df = pd.read_excel("filename.xlsx", sheetname=0) # to read excel file, sheetname=None will return all sheet
    # print(df.head()) # can specify number of row(s) in df.head(n)

    chunksize = 200 # by row
    file_name = 0
    for chunk in pd.read_csv(dataPath, error_bad_lines=False, dtype={'columname':str}, chunksize=chunksize):
        file_name = chunksize + file_name
        chunk.to_csv(processedPath+ str(file_name) + '_lines.txt', index=False, mode='w')

    return



# main method
def main():
    # data = read_file()
    read_file()
    # mapping()
    # indexing(data)

if __name__ == '__main__':
    main()