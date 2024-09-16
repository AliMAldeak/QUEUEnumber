from flask import Flask, make_response ,request
from controller import Queue
from os import path
app = Flask(__name__)

controller = Queue()

app.config['UPLOAD_FOLDER'] = "img/"

@app.route("/newcustomer",methods=["POST"])
def new_customer():
    if request.json == None:
        return make_response({},406)
    else:
        datum = request.json
        customer = controller.add_customer(datum["image"],datum["name"])
        return make_response({"status":"success"},201)


@app.route("/nextcustomer" ,methods=["GET"])
def next_customer():
    customer = controller.serve_customer()
    return make_response({},200)

@app.route("/show",methods=["GET"])
def show_customer():

    data = controller.get_last()
    resp = make_response({"no":data["c"].number,"img":data["c"].image,"total":data["total"],"stall":controller.stall,"temp":controller.temp,"humi":controller.humi},200)

    resp.headers["Access-Control-Allow-Origin"] = "*"
    
    return resp

@app.route("/send_data",methods=["GET"])
def send_data():
    controller.stall = request.args.get('stall')
    controller.serve_customer()
    return make_response(f"data recived:{controller.stall}",200)

@app.route("/send_humi",methods=["GET"])
def send_humi():
    controller.temp = request.args.get('temp')
    controller.humi = request.args.get('humi')
    return make_response({"temp":controller.temp,"humi":controller.humi},200)
@app.route("/get_humi",methods=["GET"])
def get_humi():
    resp = make_response({"temp":controller.temp,"humi":controller.humi,"num":controller.rear},200)
    resp.headers["content-type"] = "application/json"
    return resp
if __name__ == '__main__':
    # app.run(host='192.168.168.39', port=5000 ,debug=True)
    app.run(host='0.0.0.0', port=8080 ,debug=True)




# if 'file' not in request.files:
#     print("fail no part")
#     return make_response({"status:no file part"},406)
# file = request.files['file']
# if file.filename == '':
#     print("fail no file")
#     return make_response({"status:no file selected"},406)
# if file:
#     file_path = path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)
#     customer = controller.add_customer(file_path)
#     print("success")