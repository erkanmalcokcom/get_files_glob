from importlib.resources import path
import os
import glob

path = "/Users/erkanmalcok/VS Code/imdb/raw_data"
extension = "tsv"
os.chdir(path)

result = glob.glob("*.{}".format(extension))

#Sort the list of files
result.sort()
print(result)

#Convert the list to a dataframe

df = pd.DataFrame(result, columns=['file_name'])
print(df)