# Solve Me First

# Tính tổng của 2 số nguyên a và b

import math


def solveMeFirst(a, b):
    return a+b

# Simple Array Sum

# Tỉnh tổng tất cả các phần tử trong mảng ar


def simpleArraySum(ar):
    return sum(ar)


# Compare the Triplet

# Trong một cuộc thi, có 2 thí sinh A và B đã thi đấu với các nội dung như nhau
# Kết quả của họ được ghi trong mảng số nguyên tương ứng với tên a[] và b[]
# Ban tổ chức cần tổng hợp lại kết quả để công bố người chiến thắng.
# Quá trính tổng hợp kết quả được tính như sau:
#   - Điểm số của 2 thí sinh phải là điểm số của 1 nội dung
#   - Thí sinh nào cao điểm hơn thì sẽ được cộng 1 điểm vào điểm tổng hợp
#   - Trường hợp hòa, cả 2 thí sinh sẽ không được cộng điểm nào.
#   - Kết quả tổng hợp sẽ được lưu dưới dạng [resA, resB]
# Viết hàm tổng hợp kết quả thi đấu của 2 thí sinh trên

# Ví dụ:
#       A       B
#     ----- | ------
#       5   |   2
#       7   |   7
#       9   |   8
#       2   |   8
# -> [2, 1]

def compareTriplets(a, b):
    resultA = 0
    resultB = 0
    for i in range(a.__len__()):
        if a[i] > b[i]:
            resultA += 1
        elif a[i] < b[i]:
            resultB += 1
        else:
            continue
    return [resultA, resultB]

# A Very Big Sum

# Tỉnh tổng tất cả các phần tử trong mảng ar.
# Tuy nhiên, các phần tử có thể có giá trị rất lớn.


def simpleArraySum(ar):
    return sum(ar)

# Diagonal Difference

# Cho một ma trận vuông bậc n. Tính hiệu số của 2 đường chéo của ma trận đó
# Ví dụ:
#       1   3   4
#       4   2   1
#       9   2   5
# -> Hiệu 2 đường chéo: |(1+2+5)-(4+2+9)| = |8-15| = 7


def diagonalDifference(arr):
    length = arr.__len__()
    primaryDiag = []
    secondaryDiag = []
    for i in range(length):
        primaryDiag.append(arr[i][i])
        secondaryDiag.append(arr[i][abs(i-length+1)])
    return abs(sum(primaryDiag)-sum(secondaryDiag))

# Plus Minus

# Cho một mảng số nguyên arr.
# Tính tỉ lệ các số nguyên dương, số nguyên âm và số 0 xuất hiện trong mảng đó
# In kết quả bao gồm 6 chữ số thập phân ra màn hình
# Ví dụ:
# arr=[-1,-2, 8, 2, 4, 0]
# -> [0.500000, 0.333333, 0.166667]


def plusMinus(arr) -> None:
    print(str.format('{0:.6f}', len(
        [item for item in arr if item > 0])/len(arr)))
    print(str.format('{0:.6f}', len(
        [item for item in arr if item < 0])/len(arr)))
    print(str.format('{0:.6f}', len(
        [item for item in arr if item == 0])/len(arr)))


def staircase(n):
    step = ""
    for index in range(n):
        step += "#"
        print(step.rjust(n))


def miniMaxSum(arr):
    min_value = 0
    max_value = 0
    length = len(arr)
    arr.sort()
    for i in range(length-1):
        min_value += arr[i]

        max_value += arr[length-i-1]
    print(f"{min_value} {max_value}")


def birthdayCakeCandles(candles) -> int:
    return candles.count(max(candles))


def timeConversion(s):
    result = s[:8].split(":")
    if "AM" in s and result[0] == "12":
        result[0] = "00"
    elif "PM" in s and result[0] != "12":
        result[0] = str.format("{00:d}", int(result[0])+12)
    return f"{result[0]}:{result[1]}:{result[2]}"


def gradingStudents(grades):
    roundedGrades: list = []
    for grade in grades:
        baseGrade = 5*math.ceil(grade/5)
        if grade >= 38 and baseGrade - grade < 3:
            print(baseGrade)
            roundedGrades.append(baseGrade)
        else:
            roundedGrades.append(grade)
    return roundedGrades


def kangaroo(x1, v1, x2, v2):
    if v1 == v2 or (x2-x1)/(v1-v2) < 0:
        return "NO"

    return "YES" if (x2-x1) % (v1-v2) == 0 else "NO"


def getTotalX(a, b):
    ans = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            ans += 1
    return ans