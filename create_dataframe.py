import pandas as pd

people = {
    'name': ['Soumyadip', 'Dibya', 'Sumit'],
    'email': ['soumyadip.nayak@gmail.com','','']
}

df = pd.DataFrame(people)

print(df)