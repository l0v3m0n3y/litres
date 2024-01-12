import requests
class Client():
	def __init__(self):
		self.api="https://api.litres.ru"
		self.headers ={'Content-Type': 'application/json'}
		self.sid=None
	def account_info(self):
		return requests.get(f"{self.api}/foundation/api/users/me",headers=self.headers).json()
	def user_recommendations(self):
		return requests.get(f"{self.api}/foundation/api/arts/personal-recommendations",headers=self.headers).json()
	def banners_list(self):
		return requests.get(f"{self.api}/advertising/api/services/litres/places/web-header-full-width/banners",headers=self.headers).json()
	def my_authors(self):
		return requests.get(f"{self.api}/foundation/api/users/me/authors",headers=self.headers).json()
	def my_folders(self):
		return requests.get(f"{self.api}/foundation/api/users/me/folders",headers=self.headers).json()
	def genres_list(self,only_root:bool=True):
		return requests.get(f"{self.api}/foundation/api/genres?only_root={only_root}",headers=self.headers).json()
	def rating(self,collection_id,rating):
		data={"rating":rating}
		return requests.put(f"{self.api}/foundation/api/arts/{collection_id}/rating",json=data,headers=self.headers).json()
	def delete_wishlist(self,collection_id):
		return requests.delete(f"{self.api}/foundation/api/wishlist/arts/{collection_id}",headers=self.headers).json()
	def add_wishlist(self,collection_id):
		return requests.put(f"{self.api}/foundation/api/wishlist/arts/{collection_id}",headers=self.headers).json()
	def search(self,q,limit):
		return requests.get(f"{self.api}/foundation/api/search?limit={limit}&q={q}&types=text_book&types=audiobook&types=podcast&types=podcast_episode",headers=self.headers).json()
	def get_collection_info(self,collection_id):
		return requests.get(f"{self.api}/foundation/api/homepage/arts?collection_id={collection_id}",headers=self.headers).json()
	def arts_list(self):
		return requests.get(f"{self.api}/foundation/api/homepage/arts",headers=self.headers).json()
	def login(self,email,password):
		data={"login":email,"password":password}
		data=requests.post(f"{self.api}/foundation/api/auth/login",json=data,headers=self.headers)
		self.sid=data.json()['payload']['data']['sid']
		self.headers['cookie']=data.headers["set-cookie"]
		self.headers['request-session-id']=self.sid
		return data.json()