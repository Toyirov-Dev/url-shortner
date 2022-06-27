import pyshorteners

url = input("link kiriting: ")
qisqa = pyshorteners.Shortener().tinyurl.short(url)
print("qisqa url -->", qisqa)