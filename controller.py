import base64
from io import BytesIO
from PIL import Image
from datetime import datetime

# unused
class Stall:
    def __init__(self):
        self.is_busy = False
        self.number = 0


class Customer:
    def __init__(self, image, no):
        self.image = image
        self.number = no
        self.is_served = False

    def set_served(self):
        self.is_served = True

    def __str__(self) -> str:
        return f"{self.number},{self.image}"

class Queue:
    def __init__(self):
        self.customer_list = [Customer("",0)]
        self.front = 0
        self.rear = 0
        self.temp = 0
        self.humi = 0 
        self.stall = 0

    def is_empty(self):
        return self.front == 0 and self.rear == 0

    def add_customer(self, image,name):
        # if self.is_empty():
        #     self.front +=1
        self.rear +=1
        image_path = self.decodeImage(image,name)
        no = len(self.customer_list) 
        customer = Customer(image_path, no)
        self.customer_list.append(customer)
        return customer

    def serve_customer(self):
        if not self.is_empty():
            customer = self.customer_list[self.front]
            if self.rear == self.front and customer.is_served == True:
                return {}
            customer.set_served()
            self.front += 1
            if self.front >= self.rear:
                self.front = self.rear
            return customer
    def show_list(self):
        l = []
        for i in self.customer_list:
            l.append(f"{i.number},{i.image},{i.is_served}")
        print(l)
        print(self.front)
        print(self.rear)
    def get_last(self):
        self.show_list()
        if len(self.customer_list) != 0 and self.front != 0:
            last_c = self.customer_list[self.front]
            if not last_c.is_served:
                return {"total":len(self.customer_list),"c":last_c}
            else:
                return {"total":len(self.customer_list),"c":Customer("",0)}
        else:
            return {"total":len(self.customer_list),"c":Customer("",0)}

    def decodeImage(self,base64Encoding,name):
        base64Encoding = "data:image/png;base64," + base64Encoding
        starter = base64Encoding.find(',')
        image_data = base64Encoding[starter+1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        d = datetime.now()
        n = f"{d.year}_{d.month}_{d.day}_{d.hour}_{d.minute}_{d.second}"
        im.save('img/' + n + ".png")
        return 'img/' + n + ".png"

#old serve customer logic
# waiting = Customer("",0)
#         length = len(self.customer_list)
#         if length == 0:
#             return waiting
#         if self.front == length - 1 and self.front != -1:
#             return waiting
#         if self.front != -1:
#             self.customer_list[self.front - 1].set_served()