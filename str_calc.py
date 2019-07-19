delim_sign = "//"
    
def add(s=None):
    
    if not s:
        return 0
    
    s = s.strip()

    delim = ","
    
    if s.find(delim_sign) == 0:
        delim = s[2]
        s = s[3:]

    s = s.replace("\n", delim)

    res_sum = 0

    is_valid = True
    exception_data = None

    for str_number in s.split(delim):
        if not str_number:
            continue

        if str_number == delim:
            continue

        number = int(str_number)

        has_exception = False
        if number < 0:
            is_valid = False
            has_exception = True
            exception_data = exception_data or []
        
        if is_valid:
            res_sum += int(number)
        elif has_exception:
            exception_data.append(number)

    if has_exception:
        raise Exception(f"{exception_data} negatives not allowed")

    return res_sum

