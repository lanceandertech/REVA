import csv

lead_owner = ''
lead_phone = ''
lead_properties = []

_csv_owner_label = 'Owner Name'
_csv_phone_label = 'Phone'

_call_log = ['James Royster', 'Terra Young', 'Michael Hicks', 'Irving Epps & Irving & Shirley Epps Trust']
_csv_file_path = 'test.csv'


def generate_lead(csv_data):
    """
    Extracts property owner's name from csv_file row-by-row
    :yields: generates a row from CSV file
    """
    for lead in csv_data:
        yield lead


def number_of_rows(csv_data):
    """
    Converts csv_data to a list
    Uses len() to get number of rows from list
    :return: number of rows in CSV file
    """
    csv_list = list(csv_data)
    csv_length = len(csv_list)
    return csv_length


def setget_lead_owner(owner=''):
    """
    Setter and Getter for 'lead_owner' variable
    If optional parameter IS set it will update 'setget_lead_owner'
    If optional parameter is NOT set, return 'setget_lead_owner'
    :param owner:
    :return: 'lead_owner'
    """
    global lead_owner
    if owner != '':
        lead_owner = owner
    return lead_owner


def setget_lead_phone(phone=''):
    """
    Setter and Getter for 'lead_phone' variable
    If optional parameter IS set it will update 'lead_phone'
    If optional parameter is NOT set, return 'lead_phone'
    :param phone:
    :return: 'lead_phone'
    """
    global lead_phone
    if phone != '':
        lead_phone = phone
    return lead_phone


def setget_lead_properties(properties=[]):
    """
    Setter and Getter for 'lead_properties' variable
    If optional parameter IS set it will update 'lead_properties'
    If optional parameter is NOT set, return 'lead_properties'
    :param properties:
    :return: 'lead_properties'
    """
    global lead_properties
    if properties != []:
        lead_properties = properties
    return lead_properties


def find_duplicate_properties(name_to_search):
    """
    Scans 'csv_data' to check if the lead has multiple properties
    All properties belonging to the same owner are consolidated into an array
    :return: an array of the consolidated properties
    """
    with open(_csv_file_path) as csv_file:
        csv_data = csv.DictReader(csv_file)

        properties = []
        for x in csv_data:
            if x[_csv_owner_label] == name_to_search:
                address_number = x['Site Address House Number']
                address_prefix = x['Site Address Street Prefix']
                address_name = x['Site Address Street Name1']
                address_unit = x['Site Address Unit Number']
                address_city = x['Site Address City/State']
                address_zip = x['Site Address Zip']

                completed_address = f'{address_number} {address_prefix} {address_name} {address_unit}, {address_city}-{address_zip}'

                properties.append(completed_address)
        return properties


def build_lead_profile(lead):
    """
    Assigns the setter and getter functions for the lead
    :return:
    """
    setget_lead_owner(lead[_csv_owner_label])
    setget_lead_phone(lead[_csv_phone_label])
    setget_lead_properties(find_duplicate_properties(setget_lead_owner()))


def setget_next_lead(lead=''):
    next_lead = None
    if lead != '':
        next_lead = lead
    return next(next_lead)


def check_call_log(lead):
    global _call_log
    if lead in _call_log:
        return True


def main():
    print('### Inside main function.')

    with open(_csv_file_path) as csv_file:
        csv_data = csv.DictReader(csv_file)

        try:
            lead = setget_next_lead(generate_lead(csv_data))
            while check_call_log(lead[_csv_owner_label]) == True:
                lead = setget_next_lead(generate_lead(csv_data))
            build_lead_profile(lead=lead)
            print(setget_lead_owner())
            print(setget_lead_phone())
            print('Properties')
            print(find_duplicate_properties(setget_lead_owner()))

        except Exception as error:
            print(f'### Unable to create lead profile. Error: {error}')


main()
