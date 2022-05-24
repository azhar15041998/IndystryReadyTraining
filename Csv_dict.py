import csv
from collections import Counter
a_csv_file = open("imdb.csv", "r")
dict_reader = csv.DictReader(a_csv_file)

ordered_dict_from_csv = list(dict_reader)[1]
dict_from_csv = dict(ordered_dict_from_csv)

print(dict_from_csv)
print(type(dict_from_csv))
ctr = Counter(dict_from_csv)
ctr.most_common(100)