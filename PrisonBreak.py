# cell 1
from helper import *

# cell 2
url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"

data = data_from_url(url)

# cell 3
index = 0

for row in data:
    row[0] = fetch_year(row[0])
    row = data[index][:-1]
    index += 1
    # print(row)

# cell 4
min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]
years = []
for y in range(min_year, max_year + 1):
    years.append(y)
    

# cell 5
attempts_per_year = []
# print(years)

for year in years:
    count = 0
    for row in data:
        if row[0] == year:
            count += 1
    attempts_per_year.append([year,count])

# print(attempts_per_year[0][1])

# cell 6
%matplotlib inline
barplot(apy)

# cell 7
countries_frequency = df["Country"].value_counts()

# cell 8
print_pretty_table(countries_frequency)
