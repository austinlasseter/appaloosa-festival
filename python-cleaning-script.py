import os
import sys
import pandas as pd

def update_file(foldername):
    filelist=os.listdir(foldername)
    for file in filelist:
        filename=foldername+"/"+file

        df=pd.read_csv(filename)

        df["tripminutes"]=df["tripduration"]/60

        df.to_csv(filename, index=False)

## Run the file
if __name__ == "__main__":
    foldername = sys.argv[1]
    update_file(foldername)
    print('End of line')
