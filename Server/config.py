import pymongo
import certifi 
connection_string = "mongodb+srv://djdrwattz:passwordSusej771@fsdi-107.o5qid.mongodb.net/?retryWrites=true&w=majority&appName=fsdi-107" 

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.get_database("organika") #notes
