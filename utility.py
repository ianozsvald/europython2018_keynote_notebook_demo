
def fetch(experiment, csv_filename):
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    print("Fetching")
    SCOPE = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
    gc = gspread.authorize(credentials)
    wks = gc.open(experiment)
    print("Working from sheet:", wks.title)

    sheet = wks.sheet1
    csv_as_bytes = sheet.export('csv')
    with open(csv_filename, "wb") as f:
        print("Writing to:", csv_filename)
        f.write(csv_as_bytes)
    print("DONE")