def Zellercongruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    K = year % 100
    J = year // 100
    h = (q + int((13 * (m + 1)) / 5) + K + int(K / 4) + int(J / 4) + (5 * J)) % 7
    return (h + 5) % 7

def switch(h):
    return {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }[h]

def parseInput():
    dateString = input().strip()
    _ = input().strip()
    items = {}
    while True:
        line = input().strip()
        if line.lower() == "start":
            break
        parts = line.split()
        itemName = parts[0].upper()
        prices = [float(price) for price in parts[1:]]
        items[itemName] = prices
    queries = []
    while True:
        line = input().strip()
        if line.lower() == "end":
            break
        queries.append(line.upper())
    return dateString, items, queries

def discount(total, day, date):
    newYearDiscount = 0.2 if date == "1 1" else 0
    weekendDiscount = 0.1 if day in [5, 6] else 0
    newYearDiscountAmount = total * newYearDiscount
    weekendDiscountAmount = total * weekendDiscount
    totalAfterDiscounts = total - newYearDiscountAmount - weekendDiscountAmount
    myList = []
    if newYearDiscount > 0:
        myList.append("%20 New Year Discount")
    if weekendDiscount > 0:
        myList.append("%10 Weekend Discount")
    discount = " + ".join(myList) if myList else "No Discount"
    return totalAfterDiscounts, discount

def calculate():
    dateString, items, queries = parseInput()
    day, monthString, year = dateString.split()
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"].index(monthString) + 1
    dayOfWeek = Zellercongruence(int(day), month, int(year))
    weekday = switch(dayOfWeek)
    print(weekday)
    total = 0
    for item in queries:
        price = int(items.get(item, [0]*7)[dayOfWeek])
        print(f"{item} {price}")
        total += price
    adjustedMonth = month if month <= 12 else month - 12
    total, discounts = discount(total, dayOfWeek, f"{int(day)} {adjustedMonth}")
    print(f"Total: {total:.1f} ({discounts})")

calculate()
