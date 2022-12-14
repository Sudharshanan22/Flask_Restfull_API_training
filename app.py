
from flask import Flask,request
from flask_restful import Api,Resource,reqparse
from security import auth,identity,users
from flask_jwt import JWT,jwt_required


app = Flask(__name__)
app.secret_key = 'Itsmesoopen'
api = Api(app)
jwt= JWT(app,auth,identity)

item_lst = [{"name":"chair","price":300}]

class Item(Resource):
    #@jwt_required()
    parser = reqparse.RequestParser()
    parser.add_argument("price",type=float,required=True,help="This field can not be left blank")
    def get(self,name):
        for myitem in item_lst:
            if name == myitem['name']:
                return myitem
        return f"the {name} do not exist in our item list"

    def post(self,name):
        for myitem in item_lst:
            if name == myitem['name']:
                return f"{name} already exist in the item list"
        data =  Item.parser.parse_args()                       #request.get_json()
        item = {"name":name,"price":data["price"]}
        item_lst.append(item)
        return item

    def delete(self,name):
        for myitem in item_lst:
            if myitem['name'] == name:
                item_lst.remove(myitem)
                return f"{name} is removed from item list",item_lst
        return f"{name} does not exist either it might not be created or might have been deleted"

    def put(self,name):
        data = Item.parser.parse_args()     #request.get_json()
        for myitem in item_lst:
            if myitem['name'] == name:
                myitem = {"name":name,"price":data["price"]}
                return f"{name} is updated with the new value"
        item = {"name":name,"price":data["price"]}
        item_lst.append(item)
        return f"{name} is newly created"

class ItemList(Resource):
    def get(self):
        return item_lst


api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
app.run(debug=True)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
