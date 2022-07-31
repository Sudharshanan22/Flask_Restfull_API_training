
mydict = [{'name':'mango','expdate':'12/12'},{'name':'carrot','expdate':'11/10'}]

def fun(name):
    print(f" the initial dict is {mydict}")
    for a in mydict:
        if  a['name'] == name:
            print(f"name value matches with this entry >> {a}")
            mydict.remove(a)
            print(f"initial dict post function {mydict}")
fun('carrot')
