from backend.Constants import BusinessDatabase
from backend.handler import listen_for_json_updates

businessDb = BusinessDatabase()
listen_for_json_updates('./fromFront.json', './fromBack.json', businessDb)



