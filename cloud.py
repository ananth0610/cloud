import pandas as pd

i#nitialize dataframe
df = pd.DataFrame()

if df.empty:
  print("DataFrame is empty")

  # initialize list elements
  data = [10,20,30,40,50,60]

  df = pd.DataFrame(data, columns=['Numbers'])
  print("populating df now")
  print(df)

else:
  print(df)
