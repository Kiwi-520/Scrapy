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

# 1. Scraper output cleaner
# A scraper returned this product title with messy formatting: " __Wireless Gaming Mouse -- RGB Edition__ ". Using only string methods, return it cleaned: no leading/trailing spaces, no underscores, no dashes. Expected: "Wireless Gaming Mouse  RGB Edition"

formatting= " __Wireless Gaming Mouse -- RGB Edition__ "
print(formatting.strip().replace("__", "").replace("--" ,""))

# 2. URL slug generator
# A blog CMS needs to convert post titles to URL slugs. Given: "How To Build A Web Scraper In Python". Convert it to: "how-to-build-a-web-scraper-in-python". No libraries. String methods only.

text = "How To Build A Web Scraper In Python"
print(text.lower().replace(" ", "-"))

# 3. CSV row builder
# You have these variables: name = "Disha", role = "Jr Data Engineer", company = "Sciative", salary = 480000. Build a single comma-separated string: "Disha,Jr Data Engineer,Sciative,480000". Then split it back into a list of 4 elements.

name = "Disha"
role = "Jr Data Engineer"
company = "Sciative"
salary = 480000
print(",".join([name, role,company, str(salary)]))

# 4. Masked email
# A privacy system needs to mask emails before displaying. Given email = "disha.sharma@gmail.com", return "d***a@gmail.com" — first char, three stars, last char of the username, then the full domain. Handle the split on @ yourself.

email = "disha.sharma@gmail.com"
print(email[0] + "***" + email.split("@")[0][-1]+ "@"+email.split("@")[1])

# 5. Log line parser
# A server log line looks like: "[2026-06-01 09:45:33] ERROR: Database connection refused on port 5432". Extract and print separately: the date, the time, the level (ERROR), and the message. String methods only — no regex yet.

log = "[2026-06-01 09:45:33] ERROR: Database connection refused on port 5432"
print(log.startswith("[") and log.endswith("]"))

# 6. Title formatter
# A scraper collected book titles in all caps: "THE PRAGMATIC PROGRAMMER", "CLEAN CODE", "DESIGNING DATA-INTENSIVE APPLICATIONS". Write code that takes any of these and returns them in title case — but the word "A" should stay lowercase. So "DESIGNING DATA-INTENSIVE APPLICATIONS" becomes "Designing Data-Intensive Applications".

# 7. Duplicate word detector
# Given a product description: "fast fast delivery with safe safe packaging and quick response". Find all words that appear more than once and return them as a list — without using Counter or any import. String and list methods only.

# 8. API key validator
# An API key is valid only if: it is exactly 32 characters long, starts with "SK-", and contains only alphanumeric characters after the prefix. Given key = "SK-aB3xQ9mN2kL7pR4wT6vY1cE5jH8uZ0", write the validation logic using only string methods and return True or False.

# 9. MongoDB connection string builder
# You have: host = "localhost", port = 27017, db = "scraped_data", user = "admin", password = "secret123". Build the connection string: "mongodb://admin:secret123@localhost:27017/scraped_data". Use an f-string.

# 10. Word frequency counter
# Given a scraped paragraph: "data engineering is the foundation of data science and data analytics in modern data driven companies". Without any imports, build a dictionary where each unique word is a key and its count is the value. Then print only words that appear more than once — using only string methods and a plain loop. Tomorrow you will do this same problem in one line with a dict comprehension.

