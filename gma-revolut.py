import os
import sys
import csv
import datetime
import locale


locale.setlocale(locale.LC_TIME, "it_IT.utf8")
deposit_offset = -3

def clean_daily_deposit(value):
    value = float(value.strip().replace(',','.'))
    return value if value>=0 else 0

# def check_year(value):
#     return calendar.isleap(int(value.strip()[-4:]))
def get_year(value):
    return int(value.strip()[-4:])

def get_year_dates(year):
    d= {}
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    
    delta = end - start

    for i in range(delta.days + 1):
        d[start + datetime.timedelta(days=i)] = 0
    return d

def from_str_to_date(value):
    return datetime.datetime.strptime(value.strip(), '%d %b %Y').date()


            
def process_file(filename, start_value):
    s = []
    ds = {}
    keep_value = start_value
    with open(filename, newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))
        # skip first row
        header = reader[0]
        year = get_year(reader[1][0])
        d = get_year_dates(year)
        for row in reader[1:]:
            if row[0] not in s:
                s.append(row[0])
                ds[from_str_to_date(row[0])] = clean_daily_deposit(row[deposit_offset])

        for d_iterator in d:
            if d_iterator in ds:
                keep_value = ds[d_iterator]
            d[d_iterator] = keep_value
            
        return d

def main(filename, start_value):
    d = process_file(filename, start_value)
    print(" GMA : {:.2f}".format(sum(d.values())/len(d)))
        

if __name__ == "__main__":
    if len(sys.argv)>1:
        filename = sys.argv[1]
        start_value = 0
        if len(sys.argv)==3:
            start_value = float(sys.argv[2])
        if not os.path.isfile(filename):
            print("\nIl nome del file indicato, riprova.")
        else:
            main(sys.argv[1], start_value )
    else:
        print("Usage: {} nome_file.csv <previous value>".format(sys.argv[0]))