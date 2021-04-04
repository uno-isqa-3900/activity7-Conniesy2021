#Name: Siyu Pan
#Course: ISQA 3900 - Web Application Development
#Description: Object Oriented Python Exercise
#Date of creation: 03/04/2021

class Customer:

    #The constructor function.
    def __init__(self, cust_num, fname, lname, company, street, city, state, zipcode):
        self._cust_ID = cust_num
        self._fName = fname
        self._lName = lname
        self._company = company
        self._street = street
        self._city = city
        self._state = state
        self._zipcode = zipcode

    #
    def _str_(self):
        return '{}\n{}'.format(self.cust_name(),self.cust_fullAddress())

    def cust_name(self):
        return "{} {}".format(self._fName,self._lName)


    def cust_fullAddress(self):
        if self._company == '':
            return '{}\n{}, {} {}'.format(self._street,self._city, self._state, self._zipcode)
        else:
            return '{}\n{}\n{}, {} {}'.format(self._company, self._street, self._city, self._state, self._zipcode)


    def cust_ID(self):
        return self._cust_ID

    def cust_company(self):
        return self._company