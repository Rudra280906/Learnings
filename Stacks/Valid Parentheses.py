def isValid(s):
    string1 = []
    open_par = "[({"
    closed_par = "])}"
    for i in s:
        string1.append(i)
        if len(string1) >= 2:
            if open_par.find(string1[len(string1)-2]) == closed_par.find(string1[len(string1)-1]) and open_par.find(string1[len(string1)-2]) != -1:
                string1.pop()
                string1.pop()
    return string1 == []


print(isValid("()"))