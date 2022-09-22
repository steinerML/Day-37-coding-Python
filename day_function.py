from datetime import date

def text_today():
    today = date.today()
    return today.strftime("%A %d %B %Y")
print("Vandaag is het", text_today())