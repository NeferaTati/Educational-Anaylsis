import csv

def get_highest_gdp(data, year):
    pass

def get_lowest_gdp(data, year):
    pass

def get_state_gdp(data, state, year):
    pass

# save each row into a list (TODO: change to your path!)
list_data = []
with open("data/state_gdp_analysis.csv", "r") as :
    # load in data as DictReader
    reader = csv.DictReader()
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"


# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
#maximum = float(self._clean_data[0][column])

        # for each row
        for row in self._clean_data:
            # if that value is greater than the max I've seen so far
            val = float(row[column])
            if val > maximum:
                # set it to be my new max
                maximum = val
        return maximum

maximum = float(data[0][year])

    # get each row

    # if the value in the row is 
# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
get_highest_gdp(list_data, '2020')

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
get_lowest_gdp(list_data, '2020')
maximum = float(data[0][year])
    state = ""
    # get each row (iterating)
    for row in data:
        # get the value of that year for this row
        value = float(row[year])
        # if the value in the row is greater than my maximum
        if value > maximum:
            # make this my new maximum
            maximum = value
            state = row["GeoName"]

    # return maximum
    return state
