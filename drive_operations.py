from googleapiclient.http import MediaFileUpload

def list_files(service, page_size=10):
    results = service.files().list(pageSize=page_size).execute()
    items = results.get('files', [])
    return items

def upload_file(service, file_name, mime_type='text/plain'):
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_name, mimetype=mime_type)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

def delete_file(service, file_id):
    service.files().delete(fileId=file_id).execute()
