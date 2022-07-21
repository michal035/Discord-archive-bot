import requests

downloadUrl = ''
 
req = requests.get(downloadUrl)

bytes = int(req.headers['Content-Length'])
megabyte = float(bytes/1000000)


print(megabyte)
print(req.headers)

def download_file(url, filename=''):
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]
        if megabyte > 10:
            pass
        else:
            with requests.get(url) as reqq:
                with open(filename, 'wb') as f:
                    for chunk in reqq.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return filename

    except Exception as e:
        print(e)
        return None



download_file(downloadUrl, '')




