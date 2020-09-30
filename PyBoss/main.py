# Impoort libraries
import os
import csv
import datetime

# set a csv file path for the data
HR_csv = os.path.join("Resource",'employee_data.csv')
NewHR_output = "analysis/employee_data_2.csv"

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

Emp_ID = []
Firstname = []
Lastname = []
NewDOB = []
NewSSN = []
NewState = []
#The Name column should be split into separate First Name and Last Name columns.
#The DOB data should be re-written into MM/DD/YYYY format.
#The SSN data should be re-written such that the first five numbers are hidden from view.
#The State data should be re-written as simple two-letter abbreviations.

with open(HR_csv) as old_data:
    reader = csv.DictReader(old_data)

    #loop through and convert data per row
    for row in old_data: 
                # Grab emp_ids and store it into a list
        Emp_ids = Emp_ID + [row[1]]

        # split names and store them in a temporary variable
        split_name = row["Name"].split(" ")

        # save seperated names
        Firstname = Firstname + [split_name[0]]
        Lastname = Lastname + [split_name[1]]

        #  reformat DOB
        NewDOB = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        NewDOB = NewDOB.strftime("%m/%d/%Y")

        # Then store it into a list
        emp_dobs = emp_dobs + [NewDOB]


# Zip all of the new lists together
empdb = zip(Emp_ids, Firstname, Lastname,
            emp_dobs, NewSSN, NewState)

# Write all of the election data to csv
with open(NewHR_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)