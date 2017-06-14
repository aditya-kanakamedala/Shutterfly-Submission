import math
import operator


'''
    Calculates LTV on a dataset containing the event data
    Uses the Customer profile data structure to calculate simple LTV
'''


class LTVCalculator:
    def top_x_simple_ltv_customers(self, x, D):
        customer_ltv = self.get_ltv(D.customer_profile)
        sorted_customer_ltv = sorted(customer_ltv.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_customer_ltv[:int(x)]

    def get_ltv(self, customer_profile):
        customer_ltv = {}
        for customer in customer_profile:
            a = float(customer_profile[customer]['total_amount']) / self.get_weeks(customer_profile[customer]['max_date'], customer_profile[customer]['min_date'])
            ltv = 52 * a * 10
            customer_ltv[customer] = ltv
        return customer_ltv

    def get_weeks(self, max_date, min_date):
        if max_date == min_date:
            return 1
        else:
            number_of_days = (max_date - min_date).days
            number_of_weeks = int(math.ceil(number_of_days / 7.0))
            return number_of_weeks
