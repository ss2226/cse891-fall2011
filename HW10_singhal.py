##################################
# Sonia Singhal
# HW 6 and 7 + HW 10 modifications
##################################

import csv, urllib

def load_csv(url):
  d = {}
  fp = urllib.urlopen(url)
  for row in csv.DictReader(fp):
     key = row['date']
     value = row['fish']

     x = d.get(key, [])
     x.append(value)
     d[key] = x

  return d

# make a dictionary from the data on the url
handle = "https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv"
fish_d = load_csv(handle)


# this function takes a dictionary in which the keys are the dates
# and the values are the fish eaten that day.
# It inverts the dictionary to one in which the keys are the fish 
# and the values are the dates that fish was eaten.
def make_dates_dict(fish_d):
    dates_d = {}

    for date in fish_d.keys():
        fish_list = fish_d.get(date)
        fish_set = set(fish_list)
        for fish in fish_set:
            date_list = dates_d.get(fish, [])
            date_list.append(date)
            dates_d[fish] = date_list

    return dates_d

# create an inverted dictionary
dates_d = make_dates_dict(fish_d)


# this function takes a dictionary (organized with the dates as keys
# and the fish as values) and a particular date (format 'mo/day').
# It returns a list of the fish eaten on that date.
# If the date does not appear in the dictionary, it returns an empty list.
def get_fishes_by_date(fish_d, date):
  fishlist = fish_d.get(date, [])

  return fishlist


# this function takes a dictionary (organized with the fish as keys
# and the dates as values) and a particular fish (as a string).
# It returns a list of the days that fish was eaten.
# If the fish does not appear in the dictionary, it returns an empty list.
def get_dates_by_fish(dates_d, fish):
  dateslist = dates_d.get(fish, [])

  return dateslist


# this function takes a dictionary organized with the dates as keys
# and the fish as values (fish_d),
# and a list of dates (datelist).
# It returns a list with all the fish that appear in the given dates.
def get_fishes_by_datelist(fish_d, datelist):
  res_dict = {}
  for date in datelist:
    res_dict[date] = fish_d.get(date, [])
  
  res_list = []
  for key in res_dict:
    res_list.extend(res_dict[key])

  return res_list


# this function takes a dictionary organized with the dates as keys
# and the fish as values (fish_d)
# and a list of fish (fishlist).
# It transforms the dictionary into one with the fish as keys and the dates as values
# and returns a list of all days the given fish were found.
def get_dates_by_fishlist(fish_d, fishlist):
  dates_d = make_dates_dict(fish_d)
  res_dict = {}
  for fish in fishlist:
    res_dict[fish] = dates_d.get(fish, [])

  res_list = []
  for key in res_dict:
    res_list.extend(res_dict[key])

  return res_list


# Tests
# test 1
x = get_fishes_by_date(fish_d, '1/1')
assert 'salmon' in x

###

# test 2
x = get_dates_by_fish(dates_d, 'salmon')
assert '1/1' in x
assert '1/2' in x

###

# test 3
x = get_fishes_by_datelist(fish_d, ['1/1'])
assert 'salmon' in x, x

###

# test 4
x = get_dates_by_fishlist(fish_d, ['salmon'])
assert '1/1' in x, x


