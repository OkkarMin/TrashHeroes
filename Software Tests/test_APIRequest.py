import time
import requests


url = "http://45957256.ngrok.io"

files = {"files": open("./image.jpg", "rb")}

start_time = time.time()


response = requests.post(url, files=files)

end_time = time.time()

time_taken = end_time - start_time

print("Time taken - ", time_taken)
print(response.text)
