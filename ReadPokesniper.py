try:
    # For Python 3.0 and later
    from urllib.request import Request, urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}) # This is to pretend the request comes from known web browser to avoid access denied
    response = urlopen(req)

    data = response.read().decode("utf-8")

    return json.loads(data)


lastcoords = []
while True:
    url = "http://pokesnipers.com/api/v1/pokemon.json"
    ret = get_jsonparsed_data(url)
    if len(lastcoords) > 5:
        lastcoords.clear()

#    print(ret)
    list_ = ['Lapras', 'Snorlax', 'Dragonite', 'Wigglytuff', 'Slowbro', 'Exeggutor']
    for c in ret['results']:
        if any(word in c.get('name') for word in list_):
            message = 'Rare pockemon in ' + c.get('coords') + ' until ' + c.get('until')

            if(c.get('coords') not in lastcoords):
                lastcoords.append(c.get('coords'))
                # beep me
                import winsound
                Freq = 2500  # Set Frequency To 2500 Hertz
                Dur = 500  # Set Duration To 1000 ms == 1 second
                winsound.Beep(Freq, Dur)
                # show me where
                import ctypes  # An included library with Python install.
                ctypes.windll.user32.MessageBoxW(0, message, 'Catch!!!', 0)
                break

    import time
    time.sleep(3)
