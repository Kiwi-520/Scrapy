## Case conversion
# text = "Hello World"
# print(text.lower())
# print(text.upper())
# print(text.title())
# print(text.capitalize())
# print(text.swapcase())

## whitespace
# text = "      Hello World  "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

## Search methods
# text = "Hello World. Hi"
# print(text.startswith("Hello"))
# print(text.endswith("Hello"))
# print(text.find("World"))
# print(text.rfind("o"))

## Count and replace
# text = "Hel.l,o world!"
# print(text.count("l"))
# print(text.replace(",", '').replace(".", ''))

# # Split
# text = "Hello hey!a-d-v-f-g-r-g-r-g"
# print(text.split("-"))

# # join
# print(",".join(["a", "b", "c"]))

# # Check methods
# text = "ASDFG"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isspace())
# print(text.isupper())
# print(text.islower())

# # Slicing
# text = "0123456789"
# print(text[0:6])
# print(text[:9])
# print(text[3:9])
# print(text[::-1]) #reverse

# # 1. Scraper output cleaner
# # A scraper returned this product title with messy formatting: " __Wireless Gaming Mouse -- RGB Edition__ ". Using only string methods, return it cleaned: no leading/trailing spaces, no underscores, no dashes. Expected: "Wireless Gaming Mouse  RGB Edition"

# formatting= " __Wireless Gaming Mouse -- RGB Edition__ "
# print(formatting.strip().replace("__", "").replace("--" ,""))

# # 2. URL slug generator
# # A blog CMS needs to convert post titles to URL slugs. Given: "How To Build A Web Scraper In Python". Convert it to: "how-to-build-a-web-scraper-in-python". No libraries. String methods only.

# text = "How To Build A Web Scraper In Python"
# print(text.lower().replace(" ", "-"))

# # 3. CSV row builder
# # You have these variables: name = "Disha", role = "Jr Data Engineer", company = "Sciative", salary = 480000. Build a single comma-separated string: "Disha,Jr Data Engineer,Sciative,480000". Then split it back into a list of 4 elements.

# name = "Disha"
# role = "Jr Data Engineer"
# company = "Sciative"
# salary = 480000
# print(",".join([name, role,company, str(salary)]))

# # 4. Masked email
# # A privacy system needs to mask emails before displaying. Given email = "disha.sharma@gmail.com", return "d***a@gmail.com" — first char, three stars, last char of the username, then the full domain. Handle the split on @ yourself.

# email = "disha.sharma@gmail.com"
# print(email[0] + "***" + email.split("@")[0][-1]+ "@"+email.split("@")[1])

# # 5. Log line parser
# # A server log line looks like: "[2026-06-01 09:45:33] ERROR: Database connection refused on port 5432". Extract and print separately: the date, the time, the level (ERROR), and the message. String methods only — no regex yet.

# log = "[2026-06-01 09:45:33] ERROR: Database connection refused on port 5432"
# print(
#     "Date: "+log[1: 11],
#     "Time: "+log[12: 21],
#     "Level: "+log[22:27],
#     "Message: "+log[29:]
# )


# # 6. Title formatter
# # A scraper collected book titles in all caps: "THE PRAGMATIC PROGRAMMER", "CLEAN CODE", "DESIGNING DATA-INTENSIVE APPLICATIONS". Write code that takes any of these and returns them in title case — but the word "A" should stay lowercase. So "DESIGNING DATA-INTENSIVE APPLICATIONS" becomes "Designing Data-Intensive Applications".

# caps = ["THE PRAGMATIC PROGRAMMER", "CLEAN CODE", "DESIGNING DATA-INTENSIVE A APPLICATIONS"]

# def title_case(word):
#     result = []
#     if "A" in word.split():
#         for j in word.split():
#             if j == "A":
#                 j = "a"
#                 result.append(j)
#             else:
#                 j = j.title()
#                 result.append(j)
#     else:
#         result.append(word.title())

#     return ' '.join(result)

# print(title_case(caps[1]))

# # 7. Duplicate word detector
# # Given a product description: "fast fast delivery with safe safe packaging and quick response". Find all words that appear more than once and return them as a list — without using Counter or any import. String and list methods only.

# description= "fast fast delivery with safe safe packaging and quick response"

# more = {x for x in description.split() if description.split().count(x) > 1}
# print(more)

# # 8. API key validator
# # An API key is valid only if: it is exactly 32 characters long, starts with "SK-", and contains only alphanumeric characters after the prefix. Given key = "SK-aB3xQ9mN2kL7pR4wT6vY1cE5jH8uZ0", write the validation logic using only string methods and return True or False.

# def API_validator(API_KEY):
#     is_valid = False
#     if API_KEY.startswith("SK-") and len(API_KEY) == 33 and API_KEY[3:].isalnum():
#         is_valid = True
#     print(is_valid)

# API_validator("SK-aB3xQ9mN2kL7pR4wT6vY1cE5jH8uZ0")

# # 9. MongoDB connection string builder
# # You have: host = "localhost", port = 27017, db = "scraped_data", user = "admin", password = "secret123". Build the connection string: "mongodb://admin:secret123@localhost:27017/scraped_data". Use an f-string.

# host = "localhost"
# port = 27017
# db = "scraped_data"
# user = "admin"
# password = "secret123"
# print(f"mongodb://{user}:{password}@{host}{port}/{db}")


# # 10. Word frequency counter
# # Given a scraped paragraph: "data engineering is the foundation of data science and data analytics in modern data driven companies". Without any imports, build a dictionary where each unique word is a key and its count is the value. Then print only words that appear more than once — using only string methods and a plain loop. Tomorrow you will do this same problem in one line with a dict comprehension.

# paragraph= "data engineering is the foundation of data science and data analytics in modern data driven companies"
# ffreq = {v:paragraph.count(v) for k,v in enumerate(paragraph.split()) if paragraph.count(v) > 1}
# print(ffreq)

# # f strings
# name = "John"
# # formatting
# price = 1234.56789
# print(f"{price:.2f}")

# # Comma formatting
# num = 1000000
# print(f"{num:,}")

# # Alignment
# print(f"{name:>10}")
# print(f"{name:<10}")
# print(f"{name:^10}")

# Regex expressions

import re

# # functions

# # 1. re.serach(pattern, string)

# text = "The crowd drifted out after the football game."
# match = re.search("football", text)
# print(match)

# ### print(help(re))
# print(match.end())
# print(match.start())

# # 2. re.findall(pattern, string)
# text = "The football game is intresting. The crowd drifted out after the football game."
# match2 = re.findall("football", text)
# print(match2)

# # 3. re.split(split_term, phrase/string)
# split_term = "@"

# phrase = "The foot@ball game is intre@sting. The crowd drif@ted out aft@er the foot@ball game."
# match3 = re.split(split_term, phrase)
# print(match3)

# # 4. re.sub(pattern, to change to, phrase/text/string)
# text = "There weren't any cafes. They weren't listening. THose weren't work anymore."
# match4 = re.sub("weren\'t", "were not", text)
# print(match4)

# # Metacharacters
# # *, +, ?, {n}, {x,y}, {x,}

# # * 0 or more
# # + 1 or more
# # ? 0 or 1
# # {n} n times
# # {x, y} mini x max y times
# # {x,  }mini x no max

def multi_re_find(patterns, phrase):
    for i in patterns:
        print(f"Searching for patterns {i}.")
        print(re.findall(i, phrase))

# test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssss...sdddd"
# test_patterns = [
#     'sd*',
#     'sd+',
#     'sd?',
#     'sd{3}',
#     'sd{2,3}',
#     'sd{3,}'
# ]

# multi_re_find(test_patterns, test_phrase)

# # Special sequences

# # escape codes \

# # \d -> digit 0132
# # \D -> non-digit ADFV
# # \w -> alphanumeric AS23
# # \W -> non-alphanumeric !@#$
# # \s -> whitespace ' '
# # \S -> non-whitespace ''

# text = 'Jersey number of Cristiano Ronaldo is 7, his 78 twitter account is @Cristiano. '

# patterns_1 = [
#     r'\d+',
#     r'\D+',
#     r'\w+',
#     r'\W+',
#     r'\s+',
#     r'\S+',
#     r".+",
#     r"Ronaldo", #match rolando anywhere in the text
#     r"^Jersey",
#     r"\bRonaldo\b", #whoel word anywhere
#     r"@Cristiano\.\s*$"
# ]

# multi_re_find(patterns_1, text)

# # Character sets

# # used frind gourps in the strings
# # uses brackets

# patterns_2 = [
#     '[sd]', #either a s or d
#     's[sd]+',# starts with s and then followed by one or more s or d
# ]
# text = "sdsd...sssddd...sdddsddd...dsds...dssss...sdddd"

# multi_re_find(patterns_2, text)

# # Exclusion
# # ^
# # used to explcude things from the match. below used to exclude !, ., , ," ", ? from the string text_2.
# text_2 = "WHat is the jersery number of Cristian ROnaldo? is it 7 or 9?"
# print(re.findall('[^!,.? ]+', text_2))

# # Character Range
# # allows to define the huge character rnage neede for the pattern serch

# test_phrase = 'It was 7 in Manchester United, he was given that number right after Beckham left.'

# patterns_4 = [
#     '[a-z]+', #lower case aplhabets sequence
#     '[A-Z]+', #upper case aplhabets sequence
#     '[a-zA-Z]+', #lower or upper case aplhabets sequence mixed random
#     '[A-Z][a-z]+', #upper case followed by lower case aplhabets sequence
#     '[0-9]+', #digits sequence
# ]

# multi_re_find(patterns_4, test_phrase)

# Common regex questions

# # Extract numbers
# nums = "the whale is 23 feet, 56 incehes fines, 780 kg body weughts"

# print(re.findall(r"\d+", nums))

# # Extract emails
# emails = "the email is disha@gmail.com"

# print(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', emails))

# # Extract urls
# urls = "The website washttps://www.google.com"
# print(re.findall(r'https?://\S+', urls))

# # 1. Price extractor
# # A scraped HTML fragment looks like: "Buy now for only ₹1,299.00 or pay ₹433.00 per month for 3 months". Extract all numbers that represent prices — your output should be ['1,299.00', '433.00']. Use re.findall.

# like = "Buy now for only ₹1,299.00 or pay ₹433.00 per month for 3 months"
# print(re.findall(r'\d+(?:,\d+)*(?:\.\d+)', like))

# # 2. Email extractor
# # A contact page returned raw text: "Reach us at support@sciative.com or hr@sciative.com. For billing: billing@sciative.in". Extract all email addresses as a list.

# text = "Reach us at support@sciative.com or hr@sciative.com. For billing: billing@sciative.in"
# print(re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text))

# # 3. Phone number validator
# # Indian phone numbers are 10 digits and start with 6, 7, 8, or 9. Given: numbers = ["9876543210", "1234567890", "7001234567", "98765432", "8800112233"]. Use re.match to filter and return only valid Indian phone numbers.

# numbers = ["9876543210", "1234567890", "7001234567", "98765432", "8800112233"]
# # for i in numbers:
# #     print(re.match(r'^[6-9]\d{9}$', i))

# # filtered list
# valid = [x for x in numbers if re.match(r'^[6-9]\d{9}$', x)]
# print(valid)

# # 4. HTML tag stripper
# # A scraper returned text with leftover HTML: "<h1>Best Laptops</h1> in <b>2026</b> for <span class='highlight'>students</span>". Use re.sub to remove all HTML tags and return clean text: "Best Laptops in 2026 for students".

# html_data ="<h1>Best Laptops</h1> in <b>2026</b> for <span class='highlight'>students</span>"
# # tags = ["<h1>", "</h1>", "<b>", "</b>", "<span class='highlight'>", "</span>"]
# # for i in tags:
# #     ans = re.sub(i, "", html_data)
# #     html_data = ans
# # print(html_data)

# clean = re.sub(r"<[^>]+>", "", html_data)
# print(clean)

# # 5. Date format standardiser
# # Dates came in three formats across different pages: "01/06/2026", "01-06-2027", "01.06.2028". Write one regex pattern using re.sub that converts all three formats to "01-06-2026" — replacing / and . with -.

# dates = ["01/06/2026", "01-06-2027", "01.06.2028"]

# print([re.sub('[/.]', "-", date) for date in dates])

# # 6. URL protocol extractor
# # Given a list of URLs: ["https://shop.com", "http://old-site.com", "ftp://files.server.com", "https://api.service.io"]. Use re.match to extract just the protocol part from each: ["https", "http", "ftp", "https"].

# URLs= ["https://shop.com", "http://old-site.com", "ftp://files.server.com", "https://api.service.io"]

# # domains = [re.split(":", x)[0] for x in URLs if re.match(r"[a-z]+", x)]
# # print(domains)

# protocols = [re.match(r"[a-z]+", i).group() for i in URLs]
# print(protocols)

# # for i in URLs:
# #     match = re.match(r"[a-z]+", i)
# #     if match:
# #         result = match.group()
# #         print(result)

# # 7. Duplicate whitespace cleaner
# # Scraped text often has irregular spacing: "This   is  a   badly   formatted    sentence from   a   website". Use re.sub to replace any sequence of whitespace with a single space.

# data = "This   is  a   badly   formatted    sentence from   a   website"
# print(re.sub(r"\s+", " ", data ))

# # 8. Password strength checker
# # A password is strong if it has at least 8 characters, contains at least one uppercase letter, one lowercase letter, one digit, and one special character from !@#$%. Given password = "Secure@123", use re.search with separate patterns to check each condition and print which ones pass or fail.

# def multi_re_find(patterns, phrase):
#     for i in patterns:
#         print(f"Searching for patterns {i}.")
#         if re.search(i, phrase):
#             print("True")
#         else:
#             print("False")

# patterns = [
#     r"[\w\W]{8,}",
#     r"[A-Z]+",
#     r"[a-z]+",
#     r"[0-9]+",
#     r"[!@#$%]"
# ]

# password = "Secure@123"

# multi_re_find(patterns, password )

# # 9. Log level extractor
# # A log file has lines like: "2026-06-01 INFO Server started", "2026-06-01 ERROR Connection failed", "2026-06-01 WARNING High memory usage". Use re.findall to extract all log levels (INFO, ERROR, WARNING) from a multi-line string.

# log = ["2026-06-01 INFO Server started", "2026-06-01 ERROR Connection failed", "2026-06-01 WARNING High memory usage"]
# levels = []
# for i in log:
#     levels.append(re.findall(r"\b(INFO|CRITICAL|ERROR|WARNING|DEBUG)\b", i)[0])
# print(levels)

# # 10. XPath-style attribute extractor
# # A raw HTML string: '<a href="https://shop.com/product/1" class="product-link" id="p1">Buy</a>'. Use re.findall to extract all attribute values — your output should be ["https://shop.com/product/1", "product-link", "p1"]. The pattern should match anything inside double quotes.

# string= '<a href="https://shop.com/product/1" class="product-link" id="p1">Buy</a>'
# values = re.findall(r'"([^"]+)"', string)
# print(values)

# File handling

# with open("data.txt", "w") as f:
#     content = "Data use form here"
#     lines = ["2", "3", "%", "**"]
#     # f.write(content)
#     f.writelines(lines)

# # read methods
# f.read() #reads entire file
# f.readline() #reads one line
# f.readlines() #reads list of lines

# # write
# f.write()
# f.writelines()

# File modes
# r read
# w write
# rb wb read write binary


# csv
# import csv

# # read csv
# with open("data.csv", "w") as f:
#     f.write("Name, place, Animal, Thing \n")
#     f.write("John, Home, Cat, Table \n")

# with open("data.csv", "r") as f:
#     content = csv.reader(f)
#     for row in content:
#         print(row)

# # dictreader
# with open("data.csv", 'r') as f:
#     content = csv.DictReader(f)
#     for row in content:
#         print(dict(row))
# # writer
# with open("data.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows([["Name" ,"place" ,"Animal" ,"Thing"],
#                        ["Name" ,"place" ,"Animal" ,"Thing"],
#                        ["Name" ,"place" ,"Animal" ,"Thing"],
#                        ["Name" ,"place" ,"Animal" ,"Thing"]])
#     # writer.writerow(["Name" ,"place" ,"Animal" ,"Thing"])


# with open("data.csv", "r") as f:
#     content = csv.reader(f)
#     for row in content:
#         print(row)

import json

# json_text = '''
# {
#     "name": "John",
#     "age": "45"
# }
# '''
# data = json.loads(json_text)
# print(data)
# print(type(data))
# print(data["name"])

# print(json.dumps(data, indent=4))
# print(type(json.dumps(data)))

# with open("products.json") as f:
#     text = json.load(f)
# print(text)

# with open("data.json", "w") as f:
#     json.dump(text, f)

# with open("data.json") as f:
#     print(json.load(f))

# data = {
# "user": {
#     "name": "John",
#     "address": {
#         "city": "Mumbai",
#         "state": "Maharashtra"
#     }
# }
# }

# print(data["user"]["address"]["city"])

# # JSON with list
# # common API response

# data_list = {
#     "products": [
#         {
#             "name" : "Laptop",
#             "price": "$400"
#         },
#         {
#             "name" : "Laptop",
#             "price": "$400"
#         }
#     ]
# }

# product_1 = data_list["products"][0]["name"]
# print(product_1)

# product_2 = data_list["products"][1]["name"]
# print(product_2)

# data_list2= {
#     "products": [
#         {"name":"Laptop","price":50000},
#         {"name":"Phone","price":20000},
#         {"name":"Tablet","price":30000}
#     ]
# }

# names = [x["name"] for x in data_list2["products"]]
# print(names)

# prices = [product["price"] for product in data_list2["products"]]
# print(prices)

# JSON with API

# import requests

# response = requests.get("url")
# data = response.json()

# get() safety

# dummy = {
#     "name": "John"
# }

# # print(dummy["salary"])
# print(dummy.get("salary", 0))

# loads()   # string -> python
# dumps()   # python -> string

# load()    # file -> python
# dump()    # python -> file

# 1. Write and read back
# Create a file called products.txt. Write these 5 product names to it, one per line: Laptop, Mouse, Keyboard, Monitor, Webcam. Close it. Open it again, read all lines, strip whitespace from each, and print the list.

import csv
product = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]
with open("products.txt", "w") as f:
    for i in product:
        f.write(i+"\n")


with open("products.txt", "r") as f:
    data = f.readlines()
    print(data)

    data = [x.strip() for x in data]
    print(data)


# 2. Word count from file
# Using the file you created in problem 1, read it and print how many characters the longest product name has — without hardcoding anything.

print(len(max(data, key = len)))

# 3. JSON write
# You have a list of dictionaries: products = [{"name": "Laptop", "price": 45000, "stock": 12}, {"name": "Mouse", "price": 499, "stock": 200}, {"name": "Keyboard", "price": 1299, "stock": 85}]. Write this to a file called products.json with indentation of 2 spaces.

products = [{"name": "Laptop", "price": 45000, "stock": 12}, {"name": "Mouse", "price": 499, "stock": 200}, {"name": "Keyboard", "price": 1299, "stock": 85}]

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)

# 4. JSON read and filter
# Read products.json back. Using what you know, print only the products where stock is greater than 100.

with open("products.json") as f:
    content = json.load(f)
    print(content)
    print([x['name'] for x in content if x["stock"] > 100])

# 5. JSON update and rewrite
# Read products.json. Increase every price by 10%. Write the updated data back to the same file. Read and print it again to confirm.

with open("products.json") as f:
    content = json.load(f)

with open("products.json", "w") as f:
    for x in content:
        x["price"] = x["price"]+x["price"]*0.1
    json.dump(content, f, indent=2)

# 6. Append to file
# Open products.txt in append mode. Add two new products: "Webcam" and "Headset". Read the file again and print all contents — confirm no old data was lost.


with open("products.txt", "a") as f:
    f.writelines(["Webcam\n", "Headset\n"])

with open("products.txt", "r") as f:
    # print(f.readlines())
    for i in f.readlines():
        print(i.strip())

# 7. CSV write without library
# Using only file handling and string methods — no csv import — write a CSV file called inventory.csv with a header row name,price,stock and 3 data rows of your choice.

with open("inventory.csv", "w") as f:
    f.write("name,price,stock\n")
    f.writelines("Abby,234,3\nDebbie,599,6\nEbbie,800,9\n")

# 8. Line number printer
# Read any text file you have. Print each line with its line number in front, like: "1: Laptop", "2: Mouse" etc. Use enumerate.

with open("products.txt", "r") as f:
    data = f.readlines()
    for i,j in enumerate(data, start = 1):
        print(f"{i}: {j.strip()}")

# 9. JSON with nested structure
# Create and write this to order.json: an order with order_id, customer_name, and a list called items where each item has product and quantity. Make up 3 items. Then read it back and print only the product names from the items list.

orders = {
    "order": [
        {
        "order_id": 45,
        "customer_name": "John",
        "items": [
            {
                "product": "Coffee",
                "quantity":2
            },
            {
                "product": "Tea",
                "quantity":4
            },
            {
                "product": "Milk",
                "quantity":3
            }
            ]
        },
    ]
}
with open("order.json", "w") as f:
    json.dump(orders, f, indent=2)

with open("order.json") as f:
    order_info = json.load(f)
    print(order_info)
    print([x["product"] for x in order_info["order"][0]["items"]])

# 10. Safe file reader
# Write a function called safe_read(filepath) that tries to open and return the contents of a file. If the file does not exist, it should not crash — it should print "File not found: {filepath}" and return None. Test it with a real file and a fake filename.
def safe_read(filepath):
    try:
        with open(filepath, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

print(safe_read("product.txt"))