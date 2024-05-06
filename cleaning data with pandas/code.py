import pandas as pd
df  = pd.read_excel(r"C:\\Users\\User\Desktop\\tinashe beans. Data Nerd\\cleaning data with pandas\\dataset\\customer_call_list.xlsx")


#dropping duplicates

df = df.drop_duplicates(subset=['CustomerID'])

#dropping unwanted columns
print(df.columns)
df = df.drop(['Not_Useful_Column'],axis=1)


#Removing unwanted characters
df['Last_Name'] = df['Last_Name'].str.lstrip("...")
df['Last_Name'] = df['Last_Name'].str.lstrip("/")
df['Last_Name'] = df['Last_Name'].str.rstrip("_")

# or you can use the code below to remove all the unwanted characters all at once
#df['Last_Name'].str.strip("_./")

#changing the number format
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '', regex= True)

#changing the column Phone_Number to string
df["Phone_Number"] = df['Phone_Number'].astype(str)


# applying a "-" after every 3  numbers on the phone number values
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#Removing the "naan--" in the phone number column
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '', regex = True)


#Removing the "Na--" in the phone number column
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '', regex = True)

#splitting the address column into 3 columns
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n = 2, expand= True)


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y', regex = True)
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N', regex = True)


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y', regex = True)
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N', regex = True)

df = df.replace('N/a', '', regex = True)

#filling null values
df.fillna('', inplace= True)

#droping rows that have customers that should not be called
for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace= True)


for x in df.index:
    if df.loc[x, 'Phone_Number'] == '':
        df.drop(x, inplace= True)

df.reset_index(drop= True, inplace= True)

#use .to_string() so that the console doesn't trancate the output
print(df.to_string())
