import boto3
import json
import base64
import os

GET_PATH = '/myDropbox/get'
PUT_PATH = '/myDropbox/put'
VIEW_PATH = '/myDropbox/view'
bucket_name = os.environ['s3_bucket_name']

s3 = boto3.client('s3')

def list_files_for_owner(owner):
    files = []
    prefix = f"{owner}/"  # Assuming folder names are based on owners
    
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response.get('Contents', []):
        files.append(obj['Key'].split('/')[-1])
    
    return files
    
def get_file_url(owner, file_name):
    files = list_files_for_owner(owner)
    if file_name not in files:
        return None
    file_key = f'{owner}/{file_name}'
    try:
        file_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': file_key}, ExpiresIn=3600)
        return file_url
    except Exception as e:
        print(f"Error generating URL for {file_key}: {e}")
        return None

def create_folder(folder_path):
    try:
        s3.put_object(Bucket=bucket_name, Key=(folder_path))
    except Exception as e:
        print(f"Error creating folder {folder_path}: {e}")

def upload_file_to_s3(file_content, file_key):
    try:
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_key)
    except Exception as e:
        print(f"Error uploading file {file_key}: {e}")

def lambda_handler(event, context):
    path = event['path']
    body = json.loads(event["body"])
    
    if path == PUT_PATH:          # PUT METHOD
        owner = body.get('owner')
        file_name = body.get('file_name')
        file_content_base64 = body.get('file_content_base64')
        
        if not (owner and file_name and file_content_base64):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Owner, file_name, or file_content_base64 field is missing'})
            }
        
        # Create folder if it doesn't exist
        folder_path = f"{owner}/"
        create_folder(folder_path)
        
        # Decode base64 content
        file_content = base64.b64decode(file_content_base64)
        
        # Upload file to S3
        file_key = f"{owner}/{file_name}"
        upload_file_to_s3(file_content, file_key)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'post': 'OK'})
        }
    elif path == GET_PATH:        # GET METHOD
        file_name = body.get('file_name')
        owner = body.get('owner')
        if not (file_name and owner):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'File name or owner field is missing'})
            }
        
        
        file_url = get_file_url(owner, file_name)
        if file_url:
            return {
                'statusCode': 200,
                'body': json.dumps({'file_url': file_url})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'File not found'})
            }
    elif path == VIEW_PATH:       # VIEW METHOD
        owner = body.get('owner')
        if owner:
            files = list_files_for_owner(owner)
            return {
                'statusCode': 200,
                'body': json.dumps({'files': files})
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Owner field is missing'})
            }
    return {
        'statusCode': 200,
        'body': json.dumps({'error': 'OK', 'path': path})
    }

