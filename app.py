from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from ec_val import material

app = Flask(__name__)

# dic = {0 : 'Cat', 1 : 'Dog'}
dic = {0: 'Stone', 1: 'Metal', 2: 'Greenwall',  3: 'Glass',  4: 'Brick',
       5: 'Concrete', 6: 'Wood',  7: 'Mud',  8: 'Formwork', 9: 'Asphalt', 10: 'Marble'}

# Works with custom CNN:
model = load_model('model.h5')

# Does not work with custom ResNet model below:
# model = load_model('test_resnet.h5')

model.make_predict_function()


def predict_label(img_path):
    i = image.load_img(img_path, target_size=(100, 100))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1, 100, 100, 3)
    # p = model.predict_classes(i)
    p = model.predict(i)
    classes_x = np.argmax(p, axis=1)
    # return dic[p[0]]
    return dic[classes_x[0]]


def predict_texture(img_path):
    i = image.load_img(img_path, target_size=(100, 100))
    i = image.img_to_array(i)/255.0
    i = i.reshape(1, 100, 100, 3)
    # p = model.predict_classes(i)
    p = model.predict(i)
    classes_x = np.argmax(p, axis=1)
    # return dic[p[0]]
    return dic[classes_x[0]]


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return "Please subscribe  Artificial Intelligence Hub..!!!"


@app.route("/submit", methods=['POST'])
def get_output():
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)

        val = material[p]
        print(img_path)

        return render_template("index.html", prediction=p, img_path=img_path, val=val)


@app.route("/index3")
def index3():
    return render_template("index3.html")

# No 'GET' request required here - because we are checking the REQUEST  in if condition


@app.route("/submit3", methods=['POST'])
def get_output3():
    if request.method == 'POST':
        # name attribute being called here - whichever is selected the val of that is returned
        result = request.form["Texture"]
        p = predict_texture("static/assets/" + result + ".png")
        print(p)
        return render_template("index3.html", prediction=p, result=result)


@app.route("/index2")
def index2():
    return render_template("index2.html")


@app.route("/submit2", methods=['POST'])
def get_output2():
    if request.method == 'POST':
        # name attribute being called here - whichever is selected the val of that is returned
        result = request.form["select-gan"].split("_")[1]
        pre_img_path = "static/assets/Test_" + result + ".jpg"
        img_path = "static/assets/placeholder" + result + ".png"

        if result == "001":
            details = "XXX001"
        elif result == "002":
            details = "XXX002"
        elif result == "003":
            details = "XXX003"
        return render_template("index2.html", pre_img_path=pre_img_path, img_path=img_path, details=details, result=result)


if __name__ == '__main__':
    #app.debug = True
    app.run(debug=True)
