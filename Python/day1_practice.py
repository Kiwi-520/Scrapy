# # textual data
# # string

# message = "Hello World"
# print(message)

# # message = "Bobby's World "
# # message2 = 'Bobby\'s World '
# # print(message2)

# # print(len(message2))

# print(message[0])
# print(message[0:5]) #slicing

# print(message.lower())
# print(message.count('Uni'))

# new_message = message.replace('World', "Universe") #not inplace.

# print(new_message)

# greeting = "Hello"
# name = "Michel"

# message = greeting + " " + name + '. Welcome!'

# message = f"{greeting}, {name.upper()}.Welcome!"

# print(message)

# # print(dir(name))
# # print(help(str))
# print(help(str.lower))


# --------------------------------------------------------------------------------
# # Numeric data
# # integer
# # double
# # float

# num = 3
# num2 = 3.00

# print(type(num))
# print(type(num2))



# # arithmatic operations

# print(3+2)
# print(3-2)
# print(3/2)
# print(3//2)
# print(3%2)
# print(3*2)
# print(3**2)

# print(3+2*10)
# print((3+2)*10)

# num += 4

# print(num)

# print(abs(-3))

# print(round(3.759, 2))

# # COmparisons
# # return booleans

# num1 = 2
# num2 = 3

# print(num1 == num2)
# print(num1 != num2)
# print(num1 <= num2)
# print(num1 >= num2)
# print(num1 < num2)
# print(num1 > num2)
# print(num1 is num2) #checks if the variables have same object id. They belong to same object in memory. so onyl num is num and num is not num 2 even if they same same value.


# # look like number but are strings

# num_1 = '100'
# num_2 = '200'

# print(num_1 + num_2)

# # casting

# num_1 = int(num_1)
# num_2 = int(num_2)

# print(num_1 + num_2)

# --------------------------------------------------------------------------------
# # Conditionals and booleans

# language = 'Java'

# if language == 'Python':
#     print('Language is python')
# elif language == 'Java':
#     print("Language is Java")
# else:
#     print('No match')

# # boolean operations

# # and, or, not

# user = "Admin"
# logged_in = False

# if user == "Admin" and logged_in:
#     print("Admin Page")
# elif not logged_in:
#     print("Please log in!")
# else:
#     print("Bad Creds")

# # object identity comparision `is`
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)
# print(a is b)

# # id check
# print(id(a))
# print(id(b))

# b = a
# print(a == b)
# print(a is b) # id(a) == id(b) this is what the is operator does.


# # False Values
# # False
# # None
# # Zero of any numeric type
# # Any empty sequence eg, '', [], ()
# # Any empty mapping eg, {} i.e. dictionary


# condition = {}
# if condition:
#     print('Evaluate to True')
# else:
#     print('Evaluate to False')

# --------------------------------------------------------------------------------


# # Comprehensions

# # # List

# # 1. E-commerce price cleaning
# # You have a list of prices scraped from a website but they came in as strings with the ₹ symbol: ["₹299", "₹1499", "₹89", "₹5999", "₹149"]. Create a list of just the numbers as integers.

# symbol= ["₹299", "₹1499", "₹89", "₹5999", "₹149"]

# clean_price = [int(x[1:]) for x in symbol]
# print(clean_price)

# # 2. Product name normalisation
# # A scraper collected product names with inconsistent casing: ["WIRELESS MOUSE", "mechanical Keyboard", "USB HUB", "laptop Stand", "WEBCAM hd"]. Create a list where every name is properly title-cased.

# casing= ["WIRELESS MOUSE", "mechanical Keyboard", "USB HUB", "laptop Stand", "WEBCAM hd"]

# casing_name = [x.title() for x in casing]
# print(casing_name)

# # 3. URL filter
# # You scraped 8 URLs from a page: ["https://shop.com/product/1", "https://shop.com/login", "https://shop.com/product/2", "https://shop.com/about", "https://shop.com/product/3", "https://shop.com/cart", "https://shop.com/product/4", "https://shop.com/contact"]. Create a list of only the product URLs.

# page= ["https://shop.com/product/1", "https://shop.com/login", "https://shop.com/product/2", "https://shop.com/about", "https://shop.com/product/3", "https://shop.com/cart", "https://shop.com/product/4", "https://shop.com/contact"]

# product_url = [x for x in page if "product" in x]

# print(product_url)

# # 4. Email domain extractor
# # You have a list of customer emails: ["alice@gmail.com", "bob@company.com", "carol@gmail.com", "dan@yahoo.com", "eve@company.com"]. Create a list of just the domains (the part after @).

# emails= ["alice@gmail.com", "bob@company.com", "carol@gmail.com", "dan@yahoo.com", "eve@company.com"]

# # def domian_extractor(email):
# #     domain = ''
# #     for i in email:
# #         if i == "@":
# #             ind = email.find(i)
# #             for j in range(ind+1, len(email)):
# #                 domain += email[j]
# #     return domain

# # domains = [domian_extractor(x) for x in emails]

# # # for i in emails:
# # #     domains.append(domian_extractor(i))

# # print(domains)

# domains = [x.split("@")[1] for x in emails]
# print(domains)


# # 5. Temperature converter
# # A sensor logged temperatures in Celsius: [0, 20, 37, 100, -10, 25, 42]. Your US client needs Fahrenheit. Create the converted list. Formula: (C × 9/5) + 32.

# Celsius= [0, 20, 37, 100, -10, 25, 42]

# Fahrenheit = [ ((x * 9/5) + 32) for x in Celsius]

# print(Fahrenheit)

# # 6. Out of stock filter
# # You have stock data as a list of tuples: [("Laptop", 0), ("Mouse", 45), ("Keyboard", 0), ("Monitor", 12), ("Webcam", 0), ("Headset", 7)]. Create a list of only the product names that are out of stock.

# tuples= [("Laptop", 0), ("Mouse", 45), ("Keyboard", 0), ("Monitor", 12), ("Webcam", 0), ("Headset", 7)]

# out_of_stock_products = [x[0] for x in tuples if x[1] == 0]

# print(out_of_stock_products)

# # 7. Word length filter
# # A scraper pulled keywords from meta tags: ["ai", "machine learning", "data", "web scraping", "ml", "python", "deep learning", "api"]. Create a list of only keywords longer than 5 characters.

# meta_tags= ["ai", "machine learning", "data", "web scraping", "ml", "python", "deep learning", "api"]

# valid_tags = [x for x in meta_tags if len(x) > 5]

# print(valid_tags)

# # 8. Log file error extractor
# # You have server log lines: ["INFO: server started", "ERROR: connection timeout", "INFO: request received", "ERROR: database down", "WARNING: high memory", "ERROR: null pointer"]. Create a list of only the error messages, and strip the "ERROR: " prefix from each.

# log_lines= ["INFO: server started", "ERROR: connection timeout", "INFO: request received", "ERROR: database down", "WARNING: high memory", "ERROR: null pointer"]

# error_log = [x.replace("ERROR: ", '') for x in log_lines if x.startswith("ERROR")]

# print(error_log)

# # 9. ID formatter
# # A database returned user IDs as plain integers: [1, 23, 456, 7, 89, 1234]. Your API needs them formatted as strings with leading zeros to always be 4 digits: ["0001", "0023", "0456"] and so on. Create the formatted list.

# plain_integers= [1, 23, 456, 7, 89, 1234]

# # def formating (integer):
# #     size = len(str(integer))
# #     no_of_zero = 4-size
# #     number = "0"*no_of_zero+str(integer)
# #     return number

# formatted_list = [str(x).zfill(4) for x in plain_integers]

# print(formatted_list)

# # 10. Duplicate phone number cleaner
# # A form collected phone numbers but some have spaces, some have dashes: ["98765-43210", "912 345 6789", "9876543210", "700-123-4567", "700 123 4567"]. Create a list where every number has all spaces and dashes removed.

# dashes= ["98765-43210", "912 345 6789", "9876543210", "700-123-4567", "700 123 4567"]

# cleaned_numbers = [x.replace("-", "").replace(" ", "") for x in dashes]

# print(cleaned_numbers)

# # 11. Discount calculator
# # You have products and their original prices: [("Shirt", 800), ("Jeans", 1500), ("Shoes", 2200), ("Cap", 400), ("Jacket", 3500)]. There's a 20% discount on everything above ₹1000. Create a list of final prices — discounted where applicable, original where not.

# original_prices= [("Shirt", 800), ("Jeans", 1500), ("Shoes", 2200), ("Cap", 400), ("Jacket", 3500)]

# final_price = [x[1]-x[1]*0.2 if x[1] > 1000 else x[1] for x in original_prices]
# print(final_price)

# # A MongoDB# 12. MongoDB document field extractor query returned this list of documents: [{"name": "Alice", "score": 88}, {"name": "Bob", "score": 42}, {"name": "Carol", "score": 91}, {"name": "Dan", "score": 55}, {"name": "Eve", "score": 73}]. Create a list of names of students who scored above 70.

# documents= [{"name": "Alice", "score": 88}, {"name": "Bob", "score": 42}, {"name": "Carol", "score": 91}, {"name": "Dan", "score": 55}, {"name": "Eve", "score": 73}]
# names = [x["name"] for x in documents if x["score"] > 70]
# print(names)

# # 13. File extension filter
# # A directory scan returned these filenames: ["report.pdf", "data.csv", "image.png", "notes.txt", "results.csv", "chart.png", "summary.pdf", "raw_data.csv"]. Create a list of only the CSV filenames.

# filenames= ["report.pdf", "data.csv", "image.png", "notes.txt", "results.csv", "chart.png", "summary.pdf", "raw_data.csv"]
# csv_files = [x for x in filenames if "csv" in x]
# print(csv_files)

# # 14. Scraped review cleaning
# # Reviews came in with extra whitespace from poor HTML parsing: ["  Great product!  ", "Fast delivery.   ", "  Poor quality", "  Exactly as described.  ", "Not worth it.  "]. Create a list of cleaned reviews with all leading and trailing whitespace removed.

# reviews = ["  Great product!  ", "Fast delivery.   ", "  Poor quality", "  Exactly as described.  ", "Not worth it.  "]
# clean_reviews = [x.strip() for x in reviews]
# print(clean_reviews)

# # 15. API response flattener
# # An API returned nested data — a list of orders where each order has multiple items: [["laptop", "mouse"], ["keyboard"], ["monitor", "webcam", "headset"], ["usb hub", "cable"]]. Create a single flat list containing every individual item across all orders.

# items= [["laptop", "mouse"], ["keyboard"], ["monitor", "webcam", "headset"], ["usb hub", "cable"]]
# flat = [item for row in items for item in row]
# print(flat)


# # Problem 15 is the hardest. If you can solve that one without looking anything up, your comprehension foundation is solid.

# # Dictionary

# # 1. Product inventory flip
# # You have a dictionary mapping product names to their IDs: {"laptop": 101, "mouse": 102, "keyboard": 103, "monitor": 104}. Create a new dictionary where the IDs are keys and product names are values.

# product_data = {"laptop": 101, "mouse": 102, "keyboard": 103, "monitor": 104}
# neat_data = {str(v):k for k,v in product_data.items()}
# print(neat_data)

# # 2. Student grade classifier
# # You have scores: {"Alice": 88, "Bob": 42, "Carol": 91, "Dan": 55, "Eve": 73, "Frank": 38}. Create a dictionary with the same names as keys but values replaced with "pass" if score is 50 or above, "fail" if below.

# scores= {"Alice": 88, "Bob": 42, "Carol": 91, "Dan": 55, "Eve": 73, "Frank": 38}
# result_data = {k:("Pass" if v>=50 else "Fail") for k,v in scores.items()}
# print(result_data)

# # 3. Price increase
# # A store is raising all prices by 15%: {"rice": 60, "wheat": 45, "sugar": 55, "salt": 20, "oil": 120}. Create a new dictionary with updated prices. Round each to the nearest integer.

# prices = {"rice": 60, "wheat": 45, "sugar": 55, "salt": 20, "oil": 120}
# new_prices = {k:round((0.15*v+v)) for k,v in prices.items()}
# print(new_prices)

# # 4. Scraper metadata builder
# # You have two separate lists: fields = ["title", "price", "rating", "stock"] and values = ["Wireless Mouse", "₹499", "4.3", "In Stock"]. Create a dictionary pairing each field to its value.

# fields = ["title", "price", "rating", "stock"]
# values = ["Wireless Mouse", "₹499", "4.3", "In Stock"]

# # new_dict = dict(zip(fields, values))
# new_dict = {k:v for k,v in zip(fields, values)}
# print(new_dict)

# # 5. Filter high-value customers
# # You have customer purchase totals: {"Riya": 12000, "Arjun": 4500, "Sneha": 23000, "Karan": 8900, "Pooja": 31000, "Vikram": 3200}. Create a dictionary of only customers who spent more than ₹10,000, but with their values converted to thousands — so 12000 becomes 12.

# customer_purchase = {"Riya": 12000, "Arjun": 4500, "Sneha": 23000, "Karan": 8900, "Pooja": 31000, "Vikram": 3200}
# premium_customer = {k:v/1000 for k,v in customer_purchase.items() if v > 10000}
# print(premium_customer)

# # Set

# # 1. Unique domains
# # A scraper collected these emails across multiple pages, with duplicates: ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com", "dan@company.com", "eve@yahoo.com", "frank@gmail.com"]. Create a set of unique domains only.

# emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com", "dan@company.com", "eve@yahoo.com", "frank@gmail.com"]

# # def domian_extractor(email):
# #     domain = ''
# #     for i in email:
# #         if i == "@":
# #             ind = email.find(i)
# #             for j in range(ind+1, len(email)):
# #                 domain += email[j]
# #     return domain

# unique_domains = {x.split("@")[1] for x in emails}
# print(unique_domains)

# # 2. Common products finder
# # Two warehouses reported their stock: warehouse_a = ["laptop", "mouse", "keyboard", "monitor", "webcam"] and warehouse_b = ["headset", "mouse", "laptop", "usb hub", "keyboard"]. Using set comprehensions on both, find products available in both warehouses.

# warehouse_a = ["laptop", "mouse", "keyboard", "monitor", "webcam"]
# warehouse_b = ["headset", "mouse", "laptop", "usb hub", "keyboard"]
# # set_a = {a for a in warehouse_a}
# # set_b = {b for b in warehouse_b}
# # common = set_a & set_b
# common = [x for x in warehouse_a if x in warehouse_b]
# print(common)

# # 3. Unique error codes
# # A server log has repeated error codes: [404, 200, 500, 404, 301, 200, 403, 500, 404, 200, 301]. Create a set of only the error codes — the ones that are not 200.

# codes= [404, 200, 500, 404, 301, 200, 403, 500, 404, 200, 301]
# error_codes = {x for x in codes if x != 200}
# print(error_codes)

# # 4. Unique word lengths
# # You have a list of keywords scraped from product descriptions: ["fast", "reliable", "cheap", "durable", "light", "smart", "strong", "safe"]. Create a set of the unique word lengths present in this list.

# product_descriptions= ["fast", "reliable", "cheap", "durable", "light", "smart", "strong", "safe"]
# word_lengths = {len(x) for x in product_descriptions}
# print(word_lengths)

# # 5. Suspicious IP filter
# # A server logged these IPs and you want unique ones that made more than one appearance: ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1", "10.0.0.1", "192.168.1.2"]. Create a set of IPs that appear more than once. You'll need to count first — use ips.count(ip) inside your comprehension.

# ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1", "10.0.0.1", "192.168.1.2"]
# frequent_ip = {ip for ip in ips if ips.count(ip) > 1}
# print(frequent_ip)

# # Generators

# # 1. Memory-efficient total revenue
# # You have 1 million sales records but only need the total. Prices are strings with currency symbols: prices = ["₹299", "₹1499", "₹89", "₹5999", "₹149"] (imagine this list has a million entries). Use a generator expression with sum() to get the total without building an intermediate list.

# prices = ["₹299", "₹1499", "₹89", "₹5999", "₹149"]
# gen = sum(int(x[1:]) for x in prices)
# print(gen)

# # 2. First out-of-stock item
# # You have a huge product catalogue as a list of tuples: catalogue = [("Laptop", 12), ("Mouse", 0), ("Keyboard", 5), ("Monitor", 0), ("Webcam", 3)]. Use a generator with next() to find the name of the first product with zero stock — without scanning the entire list.

# catalogue = [("Laptop", 12), ("Mouse", 0), ("Keyboard", 5), ("Monitor", 0), ("Webcam", 3)]
# zero_stock = (x[0] for x in catalogue if x[1] == 0)
# print(next(zero_stock))

# # 3. Large file line counter
# # You have a list of log lines (imagine this is a file with millions of lines): logs = ["INFO: started", "ERROR: crash", "INFO: retry", "ERROR: timeout", "INFO: done"]. Use a generator expression with sum() to count only the ERROR lines — efficiently, without building a filtered list first.

# logs = ["INFO: started", "ERROR: crash", "INFO: retry", "ERROR: timeout", "INFO: done"]
# error_lines = sum(1 for x in logs if x.startswith("ERROR"))
# print(error_lines)

# # 4. Highest discounted price
# # Products have original prices and you want the highest price after a 30% discount, without storing all discounted prices in memory: originals = [800, 1500, 2200, 400, 3500, 950, 1200]. Use a generator with max().

# originals = [800, 1500, 2200, 400, 3500, 950, 1200]
# highest_price = max((x - x*0.3) for x in originals)
# print(highest_price)

# # 5. Pipeline chaining
# # You have raw scraped data: raw = ["  ₹1,299  ", "  ₹4,999  ", "  ₹799  ", "  ₹12,499  "]. Using a single generator expression passed directly into sum(), strip whitespace, remove ₹ and commas, convert to integers, and get the total — all in one line, no intermediate variables.

# raw = ["  ₹1,299  ", "  ₹4,999  ", "  ₹799  ", "  ₹12,499  "]
# total = sum(int(x.strip().replace('₹','').replace(',','')) for x in raw)
# print(total)

# # # Nested

# # 1. Matrix flattener
# # You have a 2D matrix representing weekly sales across 3 products: sales = [[120, 340, 90], [200, 150, 310], [80, 420, 175]]. Create a single flat list of all 9 numbers.

# sales = [[120, 340, 90], [200, 150, 310], [80, 420, 175]]
# flat = list((x for row in sales for x in row))
# print(flat)

# # 2. Multiplication table
# # Create a 10x10 multiplication table as a list of lists — where the element at row i, column j is i * j. Rows and columns should run from 1 to 10. Your output should be a list of 10 lists, each containing 10 values.

# multiplication_table = [[i*j for i in range(1, 11)] for j in range(1, 11)]
# print(multiplication_table)

# # 3. Multi-page scrape flattener
# # A scraper returned results page by page, where each page is a list of product names: pages = [["laptop", "mouse", "keyboard"], ["monitor", "webcam"], ["headset", "usb hub", "cable", "stand"]]. Create a single flat list of all products, but only include products whose names are longer than 5 characters.

# pages = [["laptop", "mouse", "keyboard"], ["monitor", "webcam"], ["headset", "usb hub", "cable", "stand"]]
# all = (x for row in pages for x in row if len(x) > 5 )
# print(list(all))

# # 4. CSV row parser
# # You received raw CSV data as a list of strings: rows = ["alice,28,engineer", "bob,34,manager", "carol,25,analyst", "dan,41,director"]. Create a list of lists where each inner list contains the three fields for that person as separate elements — so [["alice", "28", "engineer"], ["bob", "34", "manager"], ...].

# rows = ["alice,28,engineer", "bob,34,manager", "carol,25,analyst", "dan,41,director"]
# clean = (x.split(",") for x in rows)
# print(list(clean))

# # 5. Coordinate grid
# # You are building a grid-based game. Generate all coordinates (x, y) for a 5x5 board where both x and y go from 0 to 4 — but exclude the main diagonal, meaning any coordinate where x == y. Your result should be a list of tuples.

# board = list(((x,y) for x in range(0, 5) for y in range(0,5) if x!=y))
# print(board)