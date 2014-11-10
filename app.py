user_input = input('isogram: ')
length = len(user_input)


# test for repeating characters
chars = []
for i in user_input:
    if i in chars:
        # repeating character found
        nonrepeating = False
        print('Invalid isogram: repeating characters found.')
    else:
        # no repeating characters found
        nonrepeating = True
        chars.append(i)


# see if string is 5, 6, or 7 characters long
if length in range(5,8) and nonrepeating:
    isogram = ['iii', 'sss', 'ooo', 'ggg', 'rrr', 'aaa', 'mmm']
    isogram = isogram[0:length]

    # get the correct template
    with open('template-%s.js' % (length), 'r') as template_file:
        template = template_file.read()

    # replace the individual characters
    count = 0
    for i in user_input:
        template = template.replace(isogram[count], i)
        count += 1

    # print ga script
    print(template)

elif length > 7:
    print('String is too long.')

elif length < 5:
    print('String is too short.')
