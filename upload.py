import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A43UUWZ0NrEy2WSvaWKi2STzis8JP9ou4XBMBqnq-5-XRRBpieoOC2Hxd3yvJ0VCbW7FpRaGBAioGjuCmVyWb089BMgTLMCu-iiQtUaa3O3BUv_ljfRp0LPkrFVbGxCnEhFWWjgqSbg'
    transferData = TransferData(access_token)

    file_from = 'upload.py'
    file_to = '/Class101/test.py'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()