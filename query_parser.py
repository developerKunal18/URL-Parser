from urllib.parse import urlparse, parse_qs

url = input("Enter URL: ")

parsed = urlparse(url)
params = parse_qs(parsed.query)

if params:
    print("\nQuery Parameters:\n")

    for key, value in params.items():
        print(f"{key} = {value[0]}")
else:
    print("No query parameters found.")
