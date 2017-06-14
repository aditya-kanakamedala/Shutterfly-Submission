import json
from utilities import LTVCalculator
from utilities import Ingester
from classes import Event, EventData

'''
    Calculate the Simple LTV based on events from the input file
'''


def get_lifetime_value():
    file_name = raw_input("Enter the input file name with extension: ")
    input_path = "..\input\\" + file_name
    out_file_name = raw_input("Enter the output file name with extension: ")
    output_file_path = "..\output\\" + out_file_name
    x = raw_input("Enter X value to calculate LTV: ")
    D = EventData.EventData()
    with open(input_path) as data_file:
        data = json.load(data_file)
        for item in data:
            event_name = item['type']
            event_verb = item['verb']
            additional_data = dict((key, value) for key, value in item.iteritems() if key not in ['type', 'verb'])
            e = Event.Event(event_name, event_verb, additional_data)
            i = Ingester.Ingester()
            i.ingest(e, D)
    c = LTVCalculator.LTVCalculator()
    LTV = c.top_x_simple_ltv_customers(x, D)
    write_file(output_file_path, x, LTV)


''' Write the output LTV data to an output file '''


def write_file(output_path, x, ltv):
    output_file = open(output_path, 'w')
    output_file.write("LTV for top " + x + " Customers\n")
    output_file.write("------------------------\n")
    output_file.write("Customer Id    LTV\n")
    for item in ltv:
        output_file.write(str(item[0]) + "  " + str(item[1]) + "\n")
    output_file.close()


def main():
    get_lifetime_value()

if __name__ == "__main__":
    main()
