# gdp-anaylisis
minimum = float(data[0][year])
    state = ""
    # get each row (iterating)
    for row in data:
        # get the value of that year for this row
        value = float(row[year])
        # if the value in the row is greater than my maximum
        if value < minimum:
            # make this my new maximum
            minimum = value
            state = row["GeoName"]

    # return maximum
    return state
