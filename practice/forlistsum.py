from googlesearch.googlesearch import GoogleSearch


prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"TOTAL : {total}")

ok =input('search something....')
response = GoogleSearch().search(ok)
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())