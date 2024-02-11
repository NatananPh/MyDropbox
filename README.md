# MyDropbox
This repository is for 2110524 Cloud Computing Technologies course Activity 5

#### Source Code Files:

1. **myDropboxClient_6330161821.py**
   - **Functionality**: This script provides a command-line interface for interacting with the myDropbox API. It allows users to perform operations such as viewing files, uploading files, and downloading files.
   
2. **myDropbox_6330161821.py**
   - **Functionality**: This is the AWS Lambda function responsible for handling API requests made to the myDropbox service. It implements the logic for uploading files to Amazon S3, retrieving file URLs, and listing files in a folder based on the owner's name.

#### HOWTO for myDropbox API:

##### Endpoints:
- **PUT** `/myDropbox/put`: Uploads a file to the myDropbox service.
- **GET** `/myDropbox/get`: Retrieves the URL of a file stored in the myDropbox service.
- **GET** `/myDropbox/view`: Retrieves a list of files in a folder based on the owner's name.

##### Request/Response Formats:

1. **PUT /myDropbox/put**

   - **Request Format**:
     ```
     {
         "owner": "string",
         "file_name": "string",
         "file_content_base64": "string"
     }
     ```

   - **Response Format**:
     ```
     {
         "GET": "OK"
     }
     ```

2. **GET /myDropbox/get**

   - **Request Format**:
     ```
     {
         "owner": "string",
         "file_name": "string"
     }
     ```

   - **Response Format**:
     ```
     {
         "file_url": "string" (URL of the file),
         "error": "string" (if file not found)
     }
     ```

3. **GET /myDropbox/view**

   - **Request Format**:
     ```
     {
         "owner": "string"
     }
     ```

   - **Response Format**:
     ```
     {
         "files": ["string"] (list of file names),
         "error": "string" (if owner field is missing)
     }
     ```

##### Usage Example:

- **View Files:**
   ```
   GET /myDropbox/view
   Request Body:
   {
       "owner": "nut"
   }
   Response Body:
   {
       "files": ["file1.txt", "file2.txt"]
   }
   ```

- **Upload File:**
   ```
   PUT /myDropbox/put
   Request Body:
   {
       "owner": "nut",
       "file_name": "file.txt",
       "file_content_base64": "base64_encoded_content"
   }
   Response Body:
   {
       "GET": "OK"
   }
   ```

- **Download File:**
   ```
   GET /myDropbox/get
   Request Body:
   {
       "owner": "nut",
       "file_name": "file.txt"
   }
   Response Body:
   {
       "file_url": "https://s3.amazonaws.com/bucketname/foldername/file.txt",
       "error": "File not found"
   }
   ```

### HOWTO for Client Code:

#### Client Code Functionalities:

- **View Files:** Displays a list of files stored in the myDropbox service for a specified owner.
- **Upload File:** Uploads a file to the myDropbox service.
- **Download File:** Downloads a file from the myDropbox service.

#### Usage Example:

- **View Files:**
  ```
  >> view
  Viewing files...
  file1.txt
  file2.txt
  ```

- **Upload File:**
  ```
  >> put file.txt
  Uploading file...
  File uploaded successfully.
  ```

- **Download File:**
  ```
  >> get file.txt nut
  Downloading file...
  File downloaded successfully.
  ```
