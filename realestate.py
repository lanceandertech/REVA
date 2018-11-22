import datetime


class realestate:
    _realtor = 'Lawrence Anderson'
    _title = 'REALTOR®'
    _caldre = '02071890'
    _phone = '(213)328-3655'
    _email = 'lanceander.realestate@gmail.com'
    _website = 'realestatewithlawrence.com'
    _company = 'Coldwell Banker Gene Armstrong, Inc.'
    _office_address = '416 W Manchester Blvd'
    _office_city = 'Inglewood'
    _office_state = 'CA'
    _office_zipcode = '90047'

    def datestamp(self):
        rawdate = datetime.datetime.now()
        month = rawdate.strftime('%B')
        day = rawdate.strftime('%d')
        year = rawdate.strftime('%Y')

        return f'{month} {day}, {year}'

    # Creates the agents mail signature
    def signature(self):
        return f"""
        {self._realtor}, {self._title}
        CalDRE# {self._caldre} | Phone: {self._phone}
        {self._company}
        {self._office_address}
        {self._office_city}, {self._office_state}-{self._office_zipcode}
        """


class doc:
    def __init__(self):
        print('### You have executed the doc option.')

        # t1: ask is this document a followup or lead
        # t2: ask for client information
        # t3: write client information into template doc
        # t4: save output file in specific location


class call:
    def __init__(self):
        print('### You have executed the call option.')

        # t1: ask for csv location
        # t2: pull lead information from csv
        # t3: using twilio, cycle through and call each lead


class log:
    def __init__(self):
        print('### You have executed the log option.')
