import pandas as pd 

people = {
    'name': ['Soumyadip', 'Dibya', 'Sumit'],
    'email': ['soumyadip.nayak@gmail.com','dibya.sau@email.com','sumit.dey@kmail.com'],
    'address': ['Midnapore','Kolaghat','Kolkata']
} #All the arrays must be of same length to create dataframe


df = pd.DataFrame(people)

print(type(df)) #Pandas DataFrame class object( two dimensional)

print(df)

print(type(df['email'])) #each field is a pandas Series classs object(one dimensional), a dataframe is a container of multiple series objects

print(df['email']) #alternate syntax df.email, not recommended because if may collide with a attribute or method name of dataframe like count

print(df[['name','address']])

print(type(df[['name','address']])) #as it is a collection of series, it creates a dataframe

greetings=['Hi','Hello','Hola']

sr=pd.Series(greetings)

print(sr, type(sr))

df=df.assign(greetings=sr) #Add series as new row in dataframe

print(df)

# Access column names
print(df.columns, type(df.columns))

# Access Row using integer location
print(df.iloc[1]) 
print(type(df.iloc[1])) # Access using integer index in dataframe; if accessing single row, returns a series with series name = index in dataframe and the series has column name as index of respective column values

# Access multiple rows with iloc
print(df.iloc[[0,1]]) 
print(type(df.iloc[[0,1]])) #Returns dataframe when accessing multiple rows

# Aceess selected rows and columns with iloc
print(df.iloc[[0,1], 1]) # Will return only second column i.e. email in this case as a series with name = column name
print(df.iloc[[2,0], [1,0]]) # Name and email of 1st and 3rd entry, notice that items are returned in order given by iloc irrespective of their order in dataframe

# Hence iloc works with integer location of rows and columns whereas loc works with labels(i.e. integer indexes or modified indexes)

# Using slicing in loc and iloc
print(df.iloc[0:2])
print(df.loc[0:2]) # Notice the difference in iloc slicing last index is exclusive whereas in loc slicing last index is inclusive
print(df.loc[2:0:-1]) # Reverse slicing
print(df.iloc[0:2, 0:2])
print(df.loc[1:2, 'email':'address'])