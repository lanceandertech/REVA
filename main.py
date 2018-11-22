import realestate


def main():
    print('### REVA has loaded.')

    # cycles 'option' input until acceptable option is received
    acceptable_option = False
    while acceptable_option == False:
        print('### Options are: "doc","call","log"')
        option = input('What option do you want to execute? ')
        if (option == 'doc') or (option == 'call') or (option == 'log'):
            acceptable_option = True
            print('### option accepted.')
        else:
            print('Your entry is not an acceptable option.')

    # build switch using a dictionary
    command = dict(
        call=realestate.call,
        doc=realestate.doc,
        log=realestate.log
    )
    # using 'option' input, execute command switch
    command[option]()


if __name__ == '__main__': main()
