import pandas as pd

data = [{"name": "Joel", "age":20, "City":"North York"},
        {'name': "king", "age":100, "City": "Konaha"},
        {"name": "Madara", "age":200, "City":"Land of Fire"},
        {"name": "Minato", "age":30, "City": "Hokage"}]

df = pd.DataFrame(data)

df.to_csv("exp1.csv", index=False)
csv_file= 'exp1.csv'
with open(csv_file) as f:
        content= f.readlines()
for line in content:
        print(line, end="")
#print(csv_file)

