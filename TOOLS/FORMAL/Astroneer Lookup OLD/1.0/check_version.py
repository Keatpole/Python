def run(version, appname, link):
    import requests

    try:
        request2 = requests.get(f"http://www.isangedal.7m.pl/websites/version/{appname}.php")
        request2.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"Was unable to check for new version.")
        return
    
    try:
        request = requests.get(request2.text)
        request.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"Was unable to check for new version.")
        return

    if request.status_code == 200:
        if str(version) != str(request.text):            
            if request2.status_code == 200:
                print(f"OUTDATED VERSION: Please install to the newest version ASAP.\n{link}")
            else:
                print("Was unable to check for new version.")
        else:
            print(f"You are on the newest version. Enjoy!")
    else:
        print("Was unable to check for new version.")