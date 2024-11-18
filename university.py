# University 1
university_object1 = {
    "ID": 1,
    "Name": "University of the Philippines",
    "Location": "Quezon City",
    "Established Year": 1908,
    "Type": "Public",
    "Website": "www.up.edu.ph"
}

# University 2
university_object2 = {
    "ID": 2,
    "Name": "Ateneo de Manila University",
    "Location": "Quezon City",
    "Established Year": 1859,
    "Type": "Private",
    "Website": "www.ateneo.edu"
}

# University 3
university_object3 = {
    "ID": 3,
    "Name": "De La Salle University",
    "Location": "Manila",
    "Established Year": 1911,
    "Type": "Private",
    "Website": "www.dlsu.edu.ph"
}

# University 4
university_object4 = {
    "ID": 4,
    "Name": "University of Santo Tomas",
    "Location": "Manila",
    "Established Year": 1611,
    "Type": "Private",
    "Website": "www.ust.edu.ph"
}

# University 5
university_object5 = {
    "ID": 5,
    "Name": "Polytechnic University of the Philippines",
    "Location": "Manila",
    "Established Year": 1904,
    "Type": "Public",
    "Website": "www.pup.edu.ph"
}

# List of Universities
universities = [university_object1, university_object2, university_object3, university_object4, university_object5]

# Iterate through the list of universities and print details
for university in universities:
    print(f"ID: {university['ID']}, Name: {university['Name']}, Location: {university['Location']}, "
          f"Established Year: {university['Established Year']}, Type: {university['Type']}, "
          f"Website: {university['Website']}")
