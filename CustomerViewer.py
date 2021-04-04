#Name: Siyu Pan
#Course: ISQA 3900 - Web Application Development
#Description: Object Oriented Python Exercise
#Date of creation: 03/04/2021
import Customer
import csv

#read data from csv file
def readData():
    csvFile = open('customers.csv','r')
    reader = csv.reader(csvFile)
    objectList = []
    for item in reader:
        if reader.line_num == 1:
            continue
        cust = Customer.Customer(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
        objectList.append(cust)
    return  objectList


def showIDName(oblist):
    for item in oblist:
        print('{} : {}'.format(item.cust_ID(), item.cust_name()))


#search function
def searchCust(index,list):
    listlen = len(list)
    for i in range(listlen):
        if list[i].cust_ID() == index:
            return list[i]
    else:
        return None


#main executive function
def main():
    try:
        custlist = readData()


        print('CUSTOMER VIEWER\n')
        print('ALL CUSTOMERS\n-------------------------')
        showIDName(custlist)

        while True:
            id = ''
            # The loop structure to ensure user enter the numeric values.
            while True:
                id = input('\nEnter Customer ID: ')
                if id.isdigit():
                    break
                else:
                    print('Enter the invalid value, please enter again')

            result = searchCust(id, custlist)
            if result == None:
                print('\nCustomer {} does not exist'.format(id))
            else:
                print()
                print(result._str_())

            redo = input('\nWould you like to continue? y/n: ')
            if redo != 'y':
                break
    # Exception handle with the situation that file doesn't exist
    except FileNotFoundError:
        print('-------------No such file, program ending-------------')



if __name__ == '__main__':
    main()