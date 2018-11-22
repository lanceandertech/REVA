import csv


def main():
    try:
        print('### Inside main function.')
        csv_file = open('test.csv')
        csv_data = csv.DictReader(csv_file)
        owner_label = 'Owner Name'
        phone_label = 'Phone'
        completed_lead = {}

        ### generator extracts property owner's name from csv_file row-by-row
        def lead_gen():
            for i in csv_data:
                yield i[owner_label]

        try:
            #print(next(lead_gen()))
            lead_name = next(lead_gen())
            property_constructor = ''
            completed_lead['owner'] = lead_name
            #completed_lead['phone'] = x[phone_label]
            completed_lead['properties'] = []


            ### lead_name from lead_gen() is matched against entire CSV doc for duplicate leads
            for x in csv_data:
                ###


                if x[owner_label] == lead_name:

                    ### combine address properties
                    try:
                        address_number = x['Site Address House Number']
                        address_prefix = x['Site Address Street Prefix']
                        address_name = x['Site Address Street Name1']
                        address_unit = x['Site Address Unit Number']
                        address_city = x['Site Address City/State']
                        address_zip = x['Site Address Zip']

                        completed_address = f'{address_number} {address_prefix} {address_name} {address_unit}, {address_city}-{address_zip}'

                        completed_lead['properties'].append(completed_address)
                        #print(completed_address)

                        print('inside deepest try block')
                        print(completed_lead['properties'])

                    except:
                        print('Error: Unable to construct properties.')
                print('inside for block')
                print(completed_lead['properties'])

            print('inside first try block')
            print(completed_lead['properties'])

            #print(completed_lead['properties'])

        except:
            print('### Error: Confusion with lead_name processing')

    except:
        print('### Error: Unable to open CSV')
    finally:
        csv_file.close()
        print('### CSV closed.')


main()
