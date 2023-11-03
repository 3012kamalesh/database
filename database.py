import pymongo
con=pymongo.MongoClient("mongodb+srv://kamalesh:kamalesh3012@cluster0.kdaisi3.mongodb.net/?retryWrites=true&w=majority")
##print("connection successfully")
db=con["chocalatecafe"]
##print("db created successfully")
col=db["chocalate store"]
##print("collection of chocalate details created successfully")
mychoc=[
    {
        "name":"diarymilk",
        "quantity":20,
        "price":[10,20,30],
        },
    {
        "name":"kitkat",
        "quantity":30,
        "price":[15,10,5],
        },
    {
        "name":"darkchacalte",
        "quantity":20,
        "price":[10,15,20],
        },
    {
        "name":"5star",
        "quantity":30,
        "price":[5,20,30]
        }
    ]
x=col.insert_many(mychoc)
##print(x.inserted_ids)
print('welocme to shop sir')
sale=str(input("what you want"))
x=col.find({},{"name":1,"price":1})
for i in x:
    mychoc=i["name"]
    print(mychoc)
print("we have collection of choclate")
sales=str(input("what type of chochalte"))
c = col.find_one({"name": sales})
if c:
    print('Yes, sir, it is available')
    quantity_price = int(input("how many chocolate you want: "))
    
####    if quantity_price <= c['quantity']:
    print('Yes, sir, the requested price is available for this chocolate')
print("list of price")
for j in c["price"]:
    print(j)
amount=int(input("have list of price select one option 0,1,2:"))
b = quantity_price*c["price"][amount]
print(f" the value of {quantity_price} and the total price is {b}")
