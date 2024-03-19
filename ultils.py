# Base URL
base_url = "http://vietanhsongngu.com/tin-tuc-c5.htm/"

# File to write the URLs into
filename = "links.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Loop through the range of numbers you want to append to the base URL
    for i in range(1, 51):  # 51 is exclusive, so it goes from 1 to 50
        # Construct the full URL by appending the current number to the base URL
        full_url = f"{base_url}{i}"
        # Write the full URL to the file followed by a newline character
        file.write(full_url + "\n")

print(f"URLs have been written to {filename}")
