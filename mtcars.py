import pandas as pd

data = pd.read_excel (r'C:\Users\dandyprasetyow\Desktop\mtcars.xlsx') 
df = pd.DataFrame(data, columns= ['Cars','mpgcyl','disp','hp','drat','wt','qsec','vs','am','gear','carb','mpg_level
'])
print (df)