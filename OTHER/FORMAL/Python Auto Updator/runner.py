import requests

def run(website):
    '''
    docstring because pylint is dumb

    :param: Website
    '''

    try:
        r = requests.get(website)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        print("Code is not available.")
        
        return False

    exec(r.text)

    return True