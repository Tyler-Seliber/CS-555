def isValidTag(tag):
    return tag in ['INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']

f = open('family.ged', 'r')
for line in f:
    print('--> ' + line, end='')
    # Parse the line
    params = line.split(' ')
    level = params[0]
    # Remove the newline character
    params[-1] = params[-1].strip('\n')

    # Determine tag and arguments
    try:
        # Exception to general formatting rule
        if level == '0' and (params[2] == 'INDI' or params[2] == 'FAM'):
            tag = params[2]
            isValid = 'Y'
            args = params[1]
        else:
            tag = params[1]
            isValid = 'Y' if isValidTag(tag) else 'N'
            args = ' '.join(params[2:])
        # Print the output
        print('<-- ' + level + '|' + tag + '|' + isValid + '|' + args)

    except IndexError: # No arguments
        tag = params[1]
        isValid = 'Y' if isValidTag(tag) else 'N'
        # Print the output
        print('<-- ' + level + '|' + tag + '|' + isValid)

f.close()