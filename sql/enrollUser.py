from .insert_data_users import *

class enrollUser:
	def __init__(self,dbname):
		self.user = db(dbname)
	
	def storeFingerprint(self, userID, fingerID, blob):
		print(userID)
		print(fingerID)
		print(type(blob))
		self.user.insertTuple('fingerprint', [fingerID, userID, blob, 0])
	
	def enrollNewUser(self,name,emailID,phoneCall,phoneWhatsapp,roomNo,pin,isAdmin,doorAccess,inventoryAccess):
		for i in [name,emailID,phoneCall,roomNo,pin]:
			if (i==""):
				print("empty string")
				return False
		password = self.createPassword(pin)
		self.user.insertTuple('users', [name, emailID, phoneCall, phoneWhatsapp, roomNo, password['salt'], password['hash'], isAdmin, doorAccess, inventoryAccess],['NAME','EMAIL_ID','PHONE_CALL','PHONE_WHATSAPP','ROOM_NO','SALT','HASHED_PASSWORD','ISADMIN','DOOR_ACCESS','INVENTORY_ACCESS'])
		return True
		
	def createPassword(self,text):
		password = {}
		#changed the salt algo to be ascii
		password['salt'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
		# print salt
		password['salt'].encode('utf-8')
		text.encode('utf-8')
		text = text + password['salt']
		#text.encode('utf-8')
		hash_object = hashlib.sha256(text.encode('utf-8'))
		password['hash'] = hash_object.hexdigest()
		return password

# def main():
# 	obj = enrollUser('SIMS.db')
# 	obj.enrollNewUser('yashdeep1','yashdeep97@gmail.com','9010712068','9665333384','bm036','1234',123,1,1,1)

# if __name__ == '__main__':
#     main()
