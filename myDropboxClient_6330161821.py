import requests
import os
from dotenv import load_dotenv
import base64

load_dotenv()

url = os.environ.get("URL")

def get_file_content_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content_binary = file.read()
            file_content_base64 = base64.b64encode(file_content_binary).decode('utf-8')
            return file_content_base64
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def view_files():
    try:
        owner = "nut"  # Hard code owner for activity 5
        if not owner:
            print("Owner's name cannot be empty.")
            return

        # API Gateway endpoint URL
        endpoint_url = f"{url}/view"

        # Request body
        body = {
            'owner': owner
        }

        # Make GET request to the API endpoint
        response = requests.get(endpoint_url, json=body)

        # Check response status code
        if response.status_code == 200:
            files = response.json().get('files')
            if files:
                for file in files:
                    print(file)
            else:
                print("No files found for this owner.")
        else:
            print("Error:", response.text)
    except Exception as e:
        print("Error:", e)

def upload_file(file_name):
    try:

        file_path = f'./{file_name}'
        file_content_base64 = get_file_content_base64(file_path)
        
        owner = "nut"  # Hard code owner for activity 5
        if not owner:
            print("Owner's name cannot be empty.")
            return

        # API Gateway endpoint URL
        endpoint_url = f"{url}/put"

        # Request body
        body = {
            'owner': owner,
            'file_name': file_name,
            'file_content_base64': file_content_base64
        }

        # Make PUT request to the API endpoint
        response = requests.put(endpoint_url, json=body)

        # Check response status code
        if response.status_code == 200:
            print("File uploaded successfully.")
        else:
            print("Error:", response.text)
    except Exception as e:
        print("Error:", e)

def download_file(file_name, owner):
    try:
        # API Gateway endpoint URL
        endpoint_url = f"{url}/get"

        # Request body
        body = {
            'owner': owner,
            'file_name': file_name
        }

        # Make GET request to the API endpoint
        response = requests.get(endpoint_url, json=body)

        # Check response status code
        if response.status_code == 200:
            file_url = response.json().get('file_url')
            if file_url:
                print("Downloading file...")
                response = requests.get(file_url)
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                print("File downloaded successfully.")
            else:
                print("File not found.")
        else:
            print("Error:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print(
        """Welcome to myDropbox Application
======================================================
Please input command (newuser username password password, login
username password, put filename, get filename, view, or logout).
If you want to quit the program just type quit.
======================================================"""
    )
    while True:
        command = input(">> ").strip().split()

        if command[0] == "view":
            print("Viewing files...")
            view_files()
        elif command[0] == "put":
            if len(command) == 2:
                upload_file(command[1])
            else:
                print("Invalid command. Usage: put filename")
        elif command[0] == "get":
            if len(command) == 3:
                download_file(command[1], command[2])
            else:
                print("Invalid command. Usage: get filename owner")
        elif command[0] == "quit":
            break
        else:
            print("Invalid command.")
