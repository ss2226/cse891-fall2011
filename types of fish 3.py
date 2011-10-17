##################################
# Sonia Singhal
# HW 6 and 7
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
date_fish_dict = load_csv(handle)


# this function takes a dictionary in which the keys are the dates
# and the values are the fish eaten that day.
# It inverts the dictionary to one in which the keys are the fish 
# and the values are the dates that fish was eaten.
def make_dates_dict(fish_d):
    dates_d = {}

    for date in date_fish_dict.keys():
        #print date
        fish_list = date_fish_dict.get(date)
        fish_set = set(fish_list)
        #print "fish set", fish_set
        for fish in fish_set:
            date_list = dates_d.get(fish, [])
            #print "fish: ", fish
            date_list.append(date)
            dates_d[fish] = date_list
            #print date_list

    return dates_d

# create an inverted dictionary
fish_dict = make_dates_dict(date_fish_dict)


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


# example commands for the previous two functions
print get_fishes_by_date(date_fish_dict, '1/1')
print get_dates_by_fish(fish_dict, 'plaice')


# this function takes a dictionary organized with the dates as keys
# and the fish as values (fish_d),
# and a list of dates (datelist)
def get_fishes_by_datelist(fish_d, datelist):
  res_dict = {}
  for date in datelist:
    res_dict[date] = fish_d.get(date, [])

  return res_dict


# sample commands for the previous function
test_datelist = ['1/1', '1/2', '1/3']
result_fishlist = get_fishes_by_datelist(date_fish_dict, test_datelist)
for key in result_fishlist:
 print key, ":", result_fishlist[key]


# this function takes a dictionary organized with the fish as keys
# and the dates as values (dates_d)
# and a list of fish (fishlist)
def get_dates_by_fishlist(dates_d, fishlist):
  res_dict = {}
  for fish in fishlist:
    res_dict[fish] = dates_d.get(fish, [])

  return res_dict


# sample commands for the previous function
test_fishlist = ['cod', 'salmon', 'maguro']
result_datelist = get_dates_by_fishlist(fish_dict, test_fishlist)
for key in result_datelist:
  print key, ":", result_datelist[key]


