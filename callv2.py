import csv

lead_owner = ''
lead_phone = ''
lead_properties = []

def main():
    print('### Inside main function.')

    try:
        csv_file = open('test.csv')
        csv_data = csv.DictReader(csv_file)

        owner_label = 'Owner Name'
        phone_label = 'Phone'

        def lead_gen():
            """
            Extracts property owner's name from csv_file row-by-row
            :yields: generates a row from CSV file
            """
            for lead in csv_data:
                yield lead

        def number_of_rows():
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

        try:
            def build_next_lead():
                """

                :return:
                """
                print('### Beginning to structure lead')
                current_lead = next(lead_gen())
                #print(f'Current lead >> {current_lead}')
                setget_lead_owner(current_lead[owner_label])
                setget_lead_phone(current_lead[phone_label])
                #print(f'Owner: {setget_lead_owner()}')
                #print(f'Phone: {setget_lead_phone()}')

                def find_duplicate_properties():
                    """
                    Scans 'csv_data' to check if the lead has multi[;e properties
                    All properties are consolidated into an array
                    :return: consolidated properties in an array
                    """
                    try:
                        print('### inside duplicate properties')
                        properties = []
                        for x in csv_data:
                            if x[owner_label] == current_lead[owner_label]:
                                address_number = x['Site Address House Number']
                                address_prefix = x['Site Address Street Prefix']
                                address_name = x['Site Address Street Name1']
                                address_unit = x['Site Address Unit Number']
                                address_city = x['Site Address City/State']
                                address_zip = x['Site Address Zip']

                                completed_address = f'{address_number} {address_prefix} {address_name} {address_unit}, {address_city}-{address_zip}'

                                properties.append(completed_address)
                                #print(completed_address)
                        return properties
                        #print(properties)
                    except Exception as error:
                        print('Error in find_duplicate_properties()')
                        print(error)

                print(find_duplicate_properties())

            build_next_lead()

        except:
            print('### Error: Unable to create lead.')

    except:
        print('### Error: Unable to open CSV.')
    finally:
        csv_file.close()
        print('### CSV closed.')


main()
