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