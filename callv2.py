import csv


def main():
    print('### Inside main function.')

    try:
        """Open csv file
        """
        csv_file = open('test.csv')
        csv_data = csv.DictReader(csv_file)

        owner_label = 'Owner Name'
        phone_label = 'Phone'
        completed_lead = {}

        def lead_gen():
            """
            Extracts property owner's name from csv_file row-by-row
            :yields: generates a row from CSV file
            """
            for lead in csv_data:
                yield lead['Owner Name']

        def number_of_rows():
            """
            Converts csv_data to a list
            Uses len() to get number of rows from list
            :return: number of rows in CSV file
            """
            csv_list = list(csv_data)
            csv_length = len(csv_list)
            return csv_length

        """T1: get lead owner name
           t2: Match lead owner against rest of csv
           t3: if match is found, reconstruct and add properties to array
        """
        try:
            def build_lead():
                """

                :return:
                """
                print('### Beginning to structure lead')
                current_lead = next(lead_gen())
                lead_owner = ''
                lead_phone = ''
                lead_address = []

                def find_duplicates():
                    for x in csv_data:
                        if x[owner_label] == current_lead:
                            address_number = x['Site Address House Number']
                            address_prefix = x['Site Address Street Prefix']
                            address_name = x['Site Address Street Name1']
                            address_unit = x['Site Address Unit Number']
                            address_city = x['Site Address City/State']
                            address_zip = x['Site Address Zip']

                            completed_address = f'{address_number} {address_prefix} {address_name} {address_unit}, {address_city}-{address_zip}'

                            lead_owner = x[owner_label]
                            lead_phone = x[phone_label]
                            lead_address.append(completed_address)

                find_duplicates()

                def complete_lead():
                    

            build_lead()

        except:
            print('### Error: Unable to create lead.')

    except:
        print('### Error: Unable to open CSV.')
    finally:
        csv_file.close()
        print('### CSV closed.')


main()
