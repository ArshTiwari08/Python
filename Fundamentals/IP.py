def isValid(s):
    n = len(s)
    if n == 1:
        return True
    val = int(s)
    if s[0] == '0' or val > 255:
        return False
    return True

def generateIpRec(s, index, curr, cnt, res):
    temp = ""
    if index >= len(s):
        return
    if cnt == 3:
        temp = s[index:]
        if len(temp) <= 3 and isValid(temp):
            res.append(curr + temp)
        return
    for i in range(index, min(index + 3, len(s))):
        temp += s[i]
        if isValid(temp):
            generateIpRec(s, i + 1, curr + temp + ".", cnt + 1, res)

def generateIp(s):
    res = []
    generateIpRec(s, 0, "", 0, res)
    return res

if __name__ == "__main__":
    s = "254525423"
    res = generateIp(s)
    for ip in res:
        print(ip)
