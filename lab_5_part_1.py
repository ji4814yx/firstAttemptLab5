import sqlite3

conn = sqlite3.connect('simpleApp_db.sqlite')  # connect or create new if not exist
# test to see if the table exists, if not, then create it
conn.execute(
    'CREATE TABLE IF NOT EXISTS jugglingRecordHolder (name text, country text, numberOfCatches int)')  # create the table

# conn.execute('INSERT INTO jugglingRecordHolder values ("Janne Mustonen", "Finland", 98)')
# conn.execute('INSERT INTO jugglingRecordHolder values ("Ian Stewart", "Finland", 94)')
# conn.execute('INSERT INTO jugglingRecordHolder values ("Aaron Gregg", "Canada", 88)')
# conn.execute('INSERT INTO jugglingRecordHolder values ("Chad Taylor", "USA", 78)')

conn.commit()  # finalize updates

results = conn.execute('SELECT * FROM jugglingRecordHolder')

# This program will make the query saving the results in the results variable and looping over the results
for row in results:
    print(row)

# let the user add a new row for a record holder
new_name = (input('enter your name '))
new_country = input('enter your country ')
new_numberOfCatches = input('enter number of catches ')

conn.execute(f'INSERT INTO jugglingRecordHolder VALUES (?, ?, ?)', (new_name, new_country, new_numberOfCatches))

results = conn.execute('SELECT * FROM jugglingRecordHolder')

conn.commit()  # Save the work
# This program will make the query saving the results in the results variable and looping over the results
for row in results:
    print(row)

name = input('Who do you want modify? ')
catches = input('what is the new catches ?')

conn.execute('UPDATE jugglingRecordHolder SET numberOfCatches = ? WHERE name = ?', (catches, name))

conn.commit()

results = conn.execute('SELECT * FROM jugglingRecordHolder')

for row in results:
    print(row)


conn.close()
