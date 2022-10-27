from Customer import Customer
import csv


def read_csv():
    try:
        with open('customers.csv') as data_file:
            f = csv.reader(data_file)
            customer_list=[]
            for row in f:
                customer_list.append(Customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],))
            return customer_list
    except:
        print("ERROR CSV FILE NOT FOUND OR COULDN'T BE READ")
        exit()
