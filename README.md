Here's an updated version of the README with the API request body formats included for all APIs:

# MyDropbox

This repository is for the 2110524 Cloud Computing Technologies course Activity 5.

## Source Code Files:

1. **myDropboxClient_6330161821.py**
   - **Functionality**: This script provides a command-line interface for interacting with the MyDropbox API. It allows users to perform operations such as viewing files, uploading files, downloading files, logging in, logging out, creating a new user, and sharing files.
   
2. **myDropbox_6330161821.py**
   - **Functionality**: This is the AWS Lambda function responsible for handling API requests made to the MyDropbox service. It implements the logic for uploading files to Amazon S3, retrieving file URLs, listing files in a folder based on the owner's name, user authentication, and file sharing.

## HOWTO for MyDropbox API:

### Endpoints:
- **PUT** `/myDropbox/put`: Uploads a file to the MyDropbox service.
- **GET** `/myDropbox/get`: Retrieves the URL of a file stored in the MyDropbox service.
- **GET** `/myDropbox/view`: Retrieves a list of files in a folder based on the owner's name.
- **POST** `/myDropbox/newuser`: Creates a new user in the MyDropbox system.
- **POST** `/myDropbox/login`: Authenticates a user in the MyDropbox system.
- **POST** `/myDropbox/logout`: Logs out the current user from the MyDropbox system.
- **POST** `/myDropbox/share`: Shares a file stored in the MyDropbox service with another user.
- **GET** `/myDropbox/quit`: Quits the MyDropbox application.

### Request/Response Formats:

1. **PUT /myDropbox/put**

   - **Request Format**:
     ```json
     {
         "owner": "string",
         "file_name": "string",
         "file_content_base64": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "GET": "OK"
     }
     ```

2. **GET /myDropbox/get**

   - **Request Format**:
     ```json
     {
         "owner": "string",
         "file_name": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "file_url": "string" (URL of the file),
         "error": "string" (if file not found)
     }
     ```

3. **GET /myDropbox/view**

   - **Request Format**:
     ```json
     {
         "owner": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "files": ["string"] (list of file names),
         "error": "string" (if owner field is missing)
     }
     ```

4. **POST /myDropbox/newuser**

   - **Request Format**:
     ```json
     {
         "username": "string",
         "hashed_password": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "message": "string" (confirmation message),
         "error": "string" (if username already exists)
     }
     ```

5. **POST /myDropbox/login**

   - **Request Format**:
     ```json
     {
         "username": "string",
         "password": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "message": "string" (confirmation message),
         "error": "string" (if invalid username or password)
     }
     ```

6. **POST /myDropbox/logout**

   - **Request Format**:
     ```json
     {
         "username": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "message": "string" (confirmation message)
     }
     ```

7. **POST /myDropbox/share**

   - **Request Format**:
     ```json
     {
         "owner": "string",
         "file_name": "string",
         "shared_with": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "message": "string" (confirmation message),
         "error": "string" (if file sharing fails)
     }
     ```

8. **GET /myDropbox/quit**

   - **Request Format**:
     ```json
     {
         "username": "string"
     }
     ```

   - **Response Format**:
     ```json
     {
         "message": "string" (confirmation message)
     }
     ```

##### Usage Examples:

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

This README provides instructions for using the MyDropbox system, including API endpoints, request/response formats, client code functionalities, and usage examples.
