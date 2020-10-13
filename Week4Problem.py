import csv

class Customer():

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.purchase_list = []

    def __repr__(self):
        return f'Customer Name: {self.first_name} {self.last_name} Id Number: {self.id} Purchases: {self.purchase_list}'

    def show_purchases(self):
        return self.purchase_list

    def customer_total (self):
        purchase_total = 0.00

        for purchase in self.purchase_list:
            purchase_total += purchase.amount_paid

        return purchase_total




class Purchase():

    def __init__(self, customer_id, item_id, amount_paid):
        self.customer_id = customer_id
        self.item_id = item_id
        self.amount_paid = amount_paid

    def __repr__(self):
        return f'Item: {self.item_id} Cost: {self.amount_paid}'

def load_data():
    #Load CSV FILE CUSTOMER
    csv_file = open('Customers.csv', 'r', newline='')
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='"')
    customer_list = []

    #Populate Customer List
    for row in csv_data:
        if csv_data.line_num == 1:
            continue
        print(row)
        customer_list.append(Customer(row[0],row[1],row[2]))

    #CLOSE CUSTOMER CSV AND DEL FILE
    csv_file.close()
    del(csv_file)

    #LOAD PURCHASE FILE
    csv_file = open('Purchases.csv','r',newline='')
    csv_data = csv.reader(csv_file, delimiter=',', quotechar='"')
    data_purchase_list = []

    #POPULATE PURCHASE LIST
    for row in csv_data:
        if csv_data.line_num == 1:
            continue
        print(row)
        data_purchase_list.append(Purchase(row[0],row[1],row[2]))

    csv_file.close()

    #LINK PURCHASES WITH RELEVANT CUSTOMER
    for i in range(len(data_purchase_list)):
        customer_id = data_purchase_list[i].customer_id
        customer_list[int(customer_id) - 1].purchase_list.append(data_purchase_list[i])

    #RETURN FULLY POPULATED CUSTOMER OBJECTS
    return customer_list

if __name__ == "__main__":
   print(load_data())






