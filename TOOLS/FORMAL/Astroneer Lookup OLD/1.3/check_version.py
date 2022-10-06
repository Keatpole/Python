import requests

def run(version, appname):
    # Get the html from "http://www.isangedal.7m.pl/websites/version/{appname}.php"
    # This will return a new url. Go to that url and get the html.
    # That html will contain the version number.
    # If the version number is equal to "version", return "OK"
    # If the version number is LESS than "version", return "AHEAD"
    # If the version number is GREATER than "version", print "link" which is the link to download the latest version then return "OUTDATED"
    # If any other error occurs, return "ERROR"
    # Let's do it!
    r = requests.get(f"http://www.isangedal.7m.pl/websites/version/{appname}.php")

    if r.status_code == 200:
        r2 = requests.get(r.text)

        text = float(r2.text)
        #print(text, version)

        if r2.status_code == 200:
            if version == text:
                return "OK"
            elif version > text:
                return "AHEAD"
            else:
                return "OUTDATED"
        else:
            return "ERROR"
    else:
        return "ERROR"
    
    try:
        r = requests.get(f"http://www.isangedal.7m.pl/websites/version/{appname}.php")

        if r.status_code == 200:
            r2 = requests.get(r.text)

            if r2.status_code == 200:
                if r2.text <= version:
                    return "OK"
                else:
                    print(link)
                    return "OUTDATED"
            else:
                return "ERROR"
        else:
            return "ERROR"
    except:
        return "ERROR"

'''def run(version, appname, link):
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
        print("Was unable to check for new version.")'''