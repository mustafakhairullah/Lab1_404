import requests

print(requests.__version__)

r = requests.get("http://google.com/")

source = requests.get(
    "https://raw.githubusercontent.com/mustafakhairullah/Lab1_404/master/version_resource.py")
print(source.text)
