import os
import csv

bosscsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PyBoss', 'employee_data.csv')

#list for storage
empId = []
firstName = []
lastName = []
dob = []
ssn = []
state = []
#state dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open, read, store data of csv
with open(bosscsv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    first = ''
    last = ''
    from datetime import datetime
    date = ''
    ssn4 = 0
    abbr = 0
    for row in csvreader:
        empId.append(row[0])
        first = row[1].split()[0]
        last = row[1].split()[1]
        firstName.append(first)
        lastName.append(last)
        date = datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")
        dob.append(date)
        ssn4 = row[3][-4:]
        ssn.append("***-***-" + ssn4)
        abbr = us_state_abbrev[row[4]]
        state.append(abbr)
data = zip(empId, firstName, lastName, dob, ssn, state)

# Specify the file to write to
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvout:

# Initialize csv.writer
    csvwriter = csv.writer(csvout)

# Write the first row (column headers)
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

# import data
    csvwriter.writerows(data)