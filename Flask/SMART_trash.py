import keras as k
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.models import model_from_json, load_model
from pprint import pprint
import tensorflow as tf
import csv
import os


class AI:
    def __init__(self):
        self.model = None
        self.labels_list = None
        self.session = tf.Session(graph=tf.Graph())

    def loadmodel(self, path):
        with self.session.graph.as_default():
            k.backend.set_session(self.session)
            self.model = load_model(path)

    def loadLabel(self, path):
        self.labels_list = dict()
        with open(path) as fp:
            line = fp.readline()
            cnt = 0
            while line:
                self.labels_list[line.strip()] = cnt
                line = fp.readline()
                cnt += 1

    # load and prepare the image
    def process_image(self, raw_image):
        '''
        Read image @filename directory and normalize.
        :param filename: path for image
        :return img: image data in array
        '''
        # load the image
        img = load_img(raw_image, target_size=(224, 224))
        # convert to array
        img = img_to_array(img)
        img /= 255.0
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)

        return img

    def write_csv_file(self, data, fileName):
        """
        Write into csv file @result directory.
        :param args: Arguments object.
        :param data: Result in dataframe.
        """
        with open(fileName, 'a', newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, value])
            writer.writerow(['', ''])

    def evaluate(self, image):
        '''
        Predict the recyclability of the input image.
        :param image: binary of an image.
        '''
        img = self.process_image(image)
        with self.session.graph.as_default():
            k.backend.set_session(self.session)
            y_prob = self.model.predict(img)

        y_classes = y_prob.argmax(axis=-1)
        result = [k for k, v in self.labels_list.items() if v == y_classes]

        # print('{}: {}'.format(result, max(y_prob[0])))
        # recyclability = (result[0].split('_'))[1]

        if((result[0] == 'cardboard') or (result[0] == 'metal_cans') or (result[0] == 'plastic_bottle')):
            return True
        else:
            return False

    # img = load_image('13Jan20-000.jpg')
    # evaluate(img)
