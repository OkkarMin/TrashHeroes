from SMART_trash import *

if __name__ == '__main__':
    new_AI = AI()
    new_AI.loadmodel('./material_recyclability_trained_model.h5')
    new_AI.loadLabel('./material_recyclability_Label.txt')
    print(new_AI.labels_list)
