import os
import dropbox

def upload_file(img_name):
    access_token = "sl.A4GhM3D2d-WOlNETpRJaV2KiwZtpKF6iEr4dbCa0tQZtFye4hQcHAGkLzYPPuhsct7nBEuVi1POlsJNQxyPZ5MTEV6e38fzyRTv8pw0yk86YZkow75pvCpC-mD3O5njmhetXBfKX8YY"
    file =img_name
    file_from = file
    file_to="/Python/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
        
list=os.listdir('F:/Naman/WhiteHat.jr/Whitehat activity/Regular Classes/Class101/testFolder')
print(list)

for i in list:
    org=os.path.splitext(i)[1]
    if org=='.py':
        print(i)
        upload_file(i)


    