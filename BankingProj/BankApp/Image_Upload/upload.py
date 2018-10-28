def handle_uploaded_file(f):
    with open('BankApp/static/upload_folder/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)