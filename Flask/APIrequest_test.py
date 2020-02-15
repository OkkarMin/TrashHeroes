import time
import requests
# from predict import *
from keras.preprocessing.image import load_img, img_to_array


url = 'http://45957256.ngrok.io'

files = {'files': open('./13Jan20-000.jpg', 'rb')}

start_time = time.time()
x = requests.post(url, files=files)
end_time = time.time()
time_taken = end_time - start_time
print(time_taken)

print(x.text)
