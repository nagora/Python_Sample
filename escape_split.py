# Sample code -1  to split the string and escape the split delimiter position
import re


def split_1():
    data = "ab,cj\,shdhdkdm,dhj,dsdgj\,asdhask,kil,"  # need to add "delim" at the last to get the last string as well
    pattern = re.compile(r"[^\\],")
    split_data =[]
    matches = pattern.finditer(data)

    len_from = 0
    for match in matches:
        start, end = (match.start(), match.end())
        print "String: %s" % data[len_from:end - 1]
        split_data.append(data[len_from:end - 1].replace("\\,",","))
        len_from = end

    return split_data

print split_1()


def split_2(s, delim):
    ret = []
    current = []
    itr = iter(s)
    next_value = ''
    for ch in itr:
        if ch == '\\':
            next_char = next(itr)
            if next_char == ",":
                try:
                    current.append(",")
                except StopIteration:
                    pass
            else:
                next_value = ch + next_char

        elif ch == delim:
            ret.append(''.join(current))
            current = []
        else:
            current.append(next_value)
            next_value = ''
            current.append(ch)
    ret.append(''.join(current))
    return ret


print split_2("ab,cj\,shdhdkdm,dhj,dsdgj\,asdhask,kil", ",")
