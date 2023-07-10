Data on the condition of American education has been collected [ever since the 1870s](https://nces.ed.gov/naal/lit_history.asp). Today we will utilize our Python skills to afford some insight into historical patterns of the US educational system.

Eventually, we will calculate the percent change of test-score outcomes on 4th or 8th graders utilizing this dataset called `states_all.csv`.

files:
* .gitignore
* analysis.py
* README.md
* states_all.csv








{mock up code for project below- Please disregard}
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
