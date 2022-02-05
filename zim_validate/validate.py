import re


def national_id(value, dashes=True):
    """You can validate zimbabwean national ID using this method.
    If dashes are mandatory the ID will be in the format 12-3456789-X-01
    If the dashes are not mandatory the format will be 123456789X01
    :param value: The string to be tested
    :param dashes: (Optional) If you want to make dashes compulsory
    :return: boolean

    """
    is_valid = False
    if dashes:
        pattern = re.compile(r"^([0-9]{2}-[0-9]{6,7}-[a-z,A-Z]-[0-9]{2})$")
    else:
        pattern = re.compile(r"^([0-9]{2}[0-9]{6,7}[a-z,A-Z][0-9]{2})$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def passport(value):
    """
    This method is used to validate zim passport.
    All Zimbabwean passports are in the format AB123456
    :param value: The string to be tested
    :return: boolean
    """
    is_valid = False
    pattern = re.compile(r"^[A-Z]{2}[0-9]{6}$")

    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def number_plate(value, space=True):
    """
    This method is used to validate zim vehicle number plates.
    All Zimbabwean number plates are in the format ABC1234
    :param value: The string to be tested
    :param space: If you want a space between the first three letters and the preceding letters numbers
    :return: boolean
    """
    is_valid = False
    if space:
        pattern = re.compile(r"^[a-zA-Z]{3}\s[0-9]{4}$")
    else:
        pattern = re.compile(r"^[a-zA-Z]{3}[0-9]{4}")

    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def id_or_passport(value, id_dashes=True):
    """You can validate Zimbabwean national ID and passport using this single method.
        All Zimbabwean passports are in the format AB123456
        If dashes are mandatory the ID will be in the format 12-3456789-X-01
        If the dashed are not mandatory the format will be 123456789X01
    :param value: The string to be tested
    :param id_dashes: (Optional) If you want to make dashes compulsory
    :return: boolean
    """
    is_valid = False
    if id_dashes:
        pattern = re.compile(r"^([0-9]{2}-[0-9]{6,7}-[a-z,A-Z]-[0-9]{2})$|^[A-Z]{2}[0-9]{6}$")
    else:
        pattern = re.compile(r"^([0-9]{2}[0-9]{6,7}[a-z,A-Z][0-9]{2})$|^[A-Z]{2}[0-9]{6}$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def telecel_number(value, prefix=True):
    """
    This can be used to check if the given mobile number is a valid Telecel number.
    All numbers
    :param value: The string to be tested
    :param prefix: (Optional) If you want to make the prefix 263 mandatory
    :return: boolean
    """

    is_valid = False
    if prefix:
        pattern = re.compile(r"^26373[0-9]{7}$")
    else:
        pattern = re.compile(r"^073[0-9]{7}$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def netone_number(value, prefix=True):
    """
    This can be used to check if the given mobile number is a valid Netone number.
    All numbers
    :param value: The string to be tested
    :param prefix: (Optional) If you want to make the prefix 263 mandatory
    :return: boolean
    """

    is_valid = False
    if prefix:
        pattern = re.compile(r"^26371[0-9]{7}$")
    else:
        pattern = re.compile(r"^071[0-9]{7}$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def econet_number(value, prefix=True):
    """
    This can be used to check if the given mobile number is a valid Econet number.
    All numbers
    :param value: The string to be tested
    :param prefix: (Optional) If you want to make the prefix 263 mandatory
    :return: boolean
    """

    is_valid = False
    if prefix:
        pattern = re.compile(r"^2637[7-8][0-9]{7}$")
    else:
        pattern = re.compile(r"^07[7-8][0-9]{7}$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def mobile_number(value, prefix=True):
    """
    This can be used to check if the given mobile number is a valid number for Econet
    ,Netone and Telecel

    All numbers
    :param value: The string to be tested
    :param prefix: (Optional) If you want to make the prefix 263 mandatory
    :return: boolean
    """

    is_valid = False
    if prefix:
        pattern = re.compile(r"^2637[13478][0-9]{7}$")
    else:
        pattern = re.compile(r"^07[13478][0-9]{7}$")
    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def password(value):
    """
    Regex to validate is the password has at least one upper case, one lowercase,
    one special character at least one number
    and a minimum length of 8
    :param value:
    :return: boolean
    """

    is_valid = False
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid


def license_number(value, space=True):
    """
    Regex to validate is the string passed is a valid Zimbabwean driver's license
    :param value: The string passed
    :param space: (Optional) if you want a space between the first 6 numbers and the last two letters
    :return: boolean
    """

    is_valid = False
    if space:
        pattern = re.compile(r"^[0-9]{6}\s[a-zA-Z]{2}$")
    else:
        pattern = re.compile(r"^[0-9]{6}[a-zA-Z]{2}$")

    try:
        if re.fullmatch(pattern, value):
            is_valid = True
    except re.error:
        is_valid = False
    return is_valid
