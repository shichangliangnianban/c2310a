import pandas as pd
data = pd.read_csv("../assignment_part1 2/assignment_part1/submission.csv")
y = data.iloc[:,:-1]
print(y)
class_0 = data[y==0]
class_1 = data[y==1]
print(len(class_0))
print(len(class_1))