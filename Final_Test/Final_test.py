"""
   Program to find out how many captains have atleast 1 tied match
   and
   Program to find out name of the captains who have highest number of tied match

"""

from reader import read_col

filename = "captains.txt"
col_name_one = "name"
col_name_two = "tied"

names_col = read_col(filename, col_name_one, str)
tied_col = read_col(filename, col_name_two, str)


def CheckValinColGreaterThanZero(col_value):
    captains_count = 0
    for val in col_value:
        if val > '0':
            captains_count += 1
    return captains_count


def captian_index(col_value):
    last_value = tied_col[0]
    captain_index = 0
    index_count = 0
    for val in tied_col:
        if val > last_value:
            captain_index = index_count
        last_value = val
        index_count += 1
    return captain_index


captain_count = CheckValinColGreaterThanZero(tied_col)
print(captain_count, "captains has at least 1 ", col_name_two, " match")

captain_index_no = captian_index(tied_col)
captain_name = names_col[captain_index_no]
print(captain_name, "has highers number of tied matches")
