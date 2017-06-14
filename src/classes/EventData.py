import datetime


# event stores that have an update verb are dictionaries
# event stores without update verb are lists
class EventData:
    """
        Dictionaries to hold specific event data based on event type
    """
    Customer = {}
    SiteVisit = {}
    ImageUpload = {}
    Order = {}
    '''
        contains the total amount spent by the customer on the site
        contains recent and oldest transaction timestamp
    '''
    customer_profile = {}

    # add a new customer
    def new_customer(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        self.Customer[key] = value
        date = value['event_time'][:10]
        customer_id = key
        # update customer spending profile
        self.update_customer(customer_id,date,0)

    # update an existing customer
    def update_customer(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        if key not in self.Order:
            print("Update issued on non-existing order! Continuing ingesting events after disregarding illegal event!!")
        else:
            self.Customer[key] = value
            date = value['event_time'][:10]
            customer_id = key
            # update customer spending profile
            self.update_customer(customer_id, date, 0)

    # log a new site visit
    def new_sitevisit(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        self.Customer[key] = value
        date = value['event_time'][:10]
        customer_id = value['customer_id']
        # update customer spending profile
        self.update_customer(customer_id, date, 0)

    # log a new image upload
    def image_upload(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        self.Customer[key] = value
        date = value['event_time'][:10]
        customer_id = value['customer_id']
        # update customer spending profile
        self.update_customer(customer_id, date, 0)

    # add a new order for a customer
    def new_order(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        date = value['event_time'][:10]
        value['total_amount'] = float(value['total_amount'].split(" ")[0])
        customer_id = value['customer_id']
        amount = value['total_amount']
        self.Order[key] = value
        # update customer spending profile
        self.update_customer(customer_id, date, amount)

    # update an existing order by a customer
    def update_order(self, event_data):
        key = event_data['key']
        value = dict((key, value) for key, value in event_data.iteritems() if key not in ['key'])
        if key not in self.Order:
            print("Update issued on non-existing order! Continuing ingesting events after disregarding illegal event!!")
        else:
            old_total_amount = self.Order[key]["total_amount"]
            value['total_amount'] = float(value['total_amount'].split(" ")[0])
            diff = value['total_amount'] - old_total_amount
            date = value['event_time'][:10]
            customer_id = value['customer_id']
            # update the customer order
            self.Order[key] = value
            # update customer spending profile
            self.update_customer(customer_id, date, diff)

    def update_customer(self, customer_id, date_string, amount):
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        if customer_id not in self.customer_profile:
            self.customer_profile[customer_id] = {'min_date': date, 'max_date': date, 'total_amount': amount}
        else:
            self.update_date(customer_id, date)
            # update customer spending profile
            self.customer_profile[customer_id]['total_amount'] += amount

    def update_date(self, customer_id, date):
        if date < self.customer_profile[customer_id]['min_date']:
            # update customer spending profile
            self.customer_profile[customer_id]['min_date'] = date

        elif date > self.customer_profile[customer_id]['max_date']:
            # update customer spending profile
            self.customer_profile[customer_id]['max_date'] = date
