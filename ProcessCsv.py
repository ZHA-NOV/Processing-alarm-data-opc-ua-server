#%%
#asyncio demo
import asyncio, datetime
async def hello():
    print(f'[{datetime.datetime.now()}] Hello...')
    await asyncio.sleep(1)  # some I/O-intensive work
    print(f'[{datetime.datetime.now()}] ...World!')

asyncio.run(hello())

#%% use csv library to read files and compare hash value for content check
import csv
import hashlib

def read_csv_file(filename):
    """Read the CSV file and return its content as a list of lists."""
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        return [row for row in csv_reader]

def calculate_hash(content):
    """Calculate the SHA-256 hash of the content."""
    hash_object = hashlib.sha256()
    hash_object.update(content.encode('utf-8'))
    return hash_object.hexdigest()

def main():
    filename = 'example.csv'  # Replace this with the path to your CSV file

    try:
        # Read the CSV file
        content = read_csv_file(filename)

        # Convert the content to a string (you may need to adjust this depending on your CSV format)
        content_str = '\n'.join([','.join(row) for row in content])

        # Calculate the hash of the content
        new_hash = calculate_hash(content_str)

        # Load the previously stored hash (if available)
        try:
            with open('previous_hash.txt', 'r') as hash_file:
                previous_hash = hash_file.read().strip()
        except FileNotFoundError:
            previous_hash = None

        if previous_hash == new_hash:
            print("The content has not changed.")
        else:
            print("The content has changed.")
            # Save the new hash for future comparisons
            with open('previous_hash.txt', 'w') as hash_file:
                hash_file.write(new_hash)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()


#%%
# if there are no updated alarm files on the remote device, no file will be downloaded via smbget