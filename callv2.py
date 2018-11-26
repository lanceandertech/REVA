import csv

lead_owner = ''
lead_phone = ''
lead_properties = []
_evaluated_lead = None

_csv_file_path = 'test.csv'
_csv_owner_label = 'Owner Name'
_csv_phone_label = 'Phone'

_call_log = []


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

                completed_address = f'{address_number} {address_prefix} {address_name} {address_unit} {address_city}-{address_zip}'

                properties.append(completed_address)
        return properties


def build_lead_profile(lead):
    """
    Assigns the setter and getter functions for the lead
    :return:
    """
    setget_lead_owner(lead[_csv_owner_label])
    setget_lead_phone(lead[_csv_phone_label])
    setget_lead_properties(find_duplicate_properties(lead[_csv_owner_label]))


def setget_next_lead(lead=''):
    global _evaluated_lead
    if lead != '':
        _evaluated_lead = lead
    return next(_evaluated_lead)


def is_in_call_log(lead):
    """
    Checks if the supplied 'lead' is in '_call_log'
    If yes, return True
    :param lead:
    :return: True
    """
    global _call_log
    if lead in _call_log:
        return True


def main():
    print('### Inside main function.')

    with open(_csv_file_path) as csv_file:
        csv_data = csv.DictReader(csv_file)

        try:

            for x in csv_data:
                lead = x
                if is_in_call_log(lead[_csv_owner_label]):
                    continue
                else:
                    _next_lead = lead
                    build_lead_profile(_next_lead)
                    print(f'Owner: {setget_lead_owner()}')
                    print(f'Phone: {setget_lead_phone()}')
                    for i in setget_lead_properties():
                        print(f'Property: {i}')
                    print('\n')
                    ### Call API goes here
                    _call_log.append(_next_lead[_csv_owner_label])


        except Exception as error:
            print(f'### Error: {error}')


main()
