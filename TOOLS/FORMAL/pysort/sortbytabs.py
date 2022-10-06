import requests
def sort(url: str, output: str, _return: bool = False) -> list:
    '''
    docstring
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)
    s = []
    for i,v in enumerate(r.text.splitlines()):
        if v.isspace() or not v:
            continue
        t = 0
        for _ in v:
            if v[4*t:4*(t+1)]=='    ':
                t+=1
            else:break
        while t >= len(s):
            s.append("")
        s[t] += f"{v[4*t:]} # Line: {i + 1} | Tabs: {t}\n"
    if _return: return s
    with open(output,'a+') as f:
        f.truncate(0)

        for i in s:
            for l in i.splitlines():
                f.write(l+"\n")
