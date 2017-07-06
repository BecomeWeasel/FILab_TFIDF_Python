import urllib

fp = urllib.urlopen('https://www.acmicpc.net/ranklist')
source = fp.read()
fp.close()

print(source)
