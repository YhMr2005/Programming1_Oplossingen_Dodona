def isGeldigISBN(nummer):
    if len(nummer) == 10:
        if nummer.isnumeric() or (nummer[:-1].isnumeric() and nummer.endswith('X')):
            if nummer.endswith('X'):
                if 10 == (int(nummer[0]) + 2*int(nummer[1]) + 3*int(nummer[2]) + 4*int(nummer[3]) + 5*int(nummer[4]) +
                    6*int(nummer[5]) + 7*int(nummer[6]) + 8*int(nummer[7]) + 9*int(nummer[8])) % 11:
                    return True
            elif int(nummer[9]) == (int(nummer[0]) + 2*int(nummer[1]) + 3*int(nummer[2]) + 4*int(nummer[3]) + 5*int(nummer[4]) +
                6*int(nummer[5]) + 7*int(nummer[6]) + 8*int(nummer[7]) + 9*int(nummer[8])) % 11:
                return True
    return False
                

isbn_nummers = []
invoer = input()
while invoer != 'stop':
    isbn_nummers.append(invoer)
    invoer = input()

for isbn in isbn_nummers:
    if isGeldigISBN(isbn):
        print('OK')
    else:
        print('FOUT')
