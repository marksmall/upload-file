from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from httplib2 import Http
from oauth2client import file, client, tools

import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive.file'

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    """Generate service to interact with Google Drive."""
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    drive_service = build('drive', 'v3', http=creds.authorize(Http()))

    today = datetime.date.today()
    print('Today: %s' % today)
    
    file_metadata = {'name': str(today) + ' - Weekly Tech Team Meeting Notes'}
    media = MediaFileUpload('./tech-team-template.odt', mimetype='application/vnd.oasis.opendocument.text')
    upload = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % upload.get('id'))

if __name__ == '__main__':
    main()
