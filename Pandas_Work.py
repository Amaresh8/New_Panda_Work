import pandas as pd
df=pd.read_csv("https://archives.nseindia.com/archives/sme/bhavcopy/sme250423.csv")
df1=pd.DataFrame(df)
df.to_csv("Original_Data.csv")
df1.drop("CORP_IND",axis=1,inplace=True)
x=1
df2=pd.DataFrame()
for col in df1.columns:
   df2["Column"+str(x)]=df1[col]
   df2.to_csv("New_Market_Price_2023-04-260.csv",index=False)
   x+=1