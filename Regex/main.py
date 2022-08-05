import re


def valid_name(name):

    length_start = re.compile(r'^[a-zA-Z].', flags=re.I)  # name starts with a-z chars
    special_char = re.compile(r'\W')
    underscore = re.compile(r'[a-z]_+', flags=re.I)
    length_alfa = re.compile(r'[a-zA-Z]', flags=re.I)  # define alfa char range
    length_num = re.compile(r'\d')  # define numeric char range

    alfa = length_alfa.findall(name)  # search alfa chars in name
    num = length_num.findall(name)  # search num chars in name

    if length_start.search(name):  # verify if the string starts with an alfa char
        if len(num) <= len(alfa):  # verify if the num chars quantity is equal or less than alfa chars
            if special_char.findall(name):
                return False

            if underscore.findall(name):
                return False

            else:
                return True


def valid_hash(hs):

    alfa = re.compile(r'[a-f]')  # define alfa char range
    num = re.compile(r'\d')  # define numeric char range

    length = re.findall(r'[a-f\d]', hs)

    if len(length) == 32:
        if alfa.findall(hs):
            if num.findall(hs):
                return True

    else:
        return False


def valid_ip(ip_code):

    formatter = ip_code.split('.')
    iprange_format = re.compile(r'^\d{1,3}\.+')

    if iprange_format.findall(ip_code):
        if len(formatter) == 4:
            for i in range(4):
                if int(formatter[i]) > 255:
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False


def valid_repository(rep):

    snakecase = re.compile(r'[a-z]_+', flags=re.I)
    caps = re.compile(r'[A-Z]+')
    bar = re.compile(r'-+')

    if snakecase.findall(rep):
        if bar.findall(rep) or caps.findall(rep):
            return False
        else:
            return True


def operation_type(op):
    if re.search(r'^pull$', op):
        return True

    if re.search(r'^push$', op):
        return True

    if re.search(r'^stash$', op):
        return True

    if re.search(r'^fork$', op):
        return True

    if re.search(r'^pop$', op):
        return True

    else:
        return False


try:
    validator = 0
    txt = input().split()

    user_id = txt[0]
    user_password = txt[1]
    ip = txt[2]
    email = txt[3]
    op_type = txt[4]
    repository = txt[5]
    hashcode = txt[6]

    if valid_name(user_id):
        validator += 1

    if valid_hash(hashcode):
        validator += 1

    if valid_ip(ip):
        validator += 1

    if operation_type(op_type):
        validator += 1

    if valid_repository(repository):
        validator += 1

    if validator == 5:
        print(True)

    else:
        print(False)

except:
    print(False)
