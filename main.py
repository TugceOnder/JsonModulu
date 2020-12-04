import json
import os
class User :
  def _init_(self,username,password,email):
   self.username=username
   self.password=password
   self.email=email

class UserRepository:
 def _init_(self):
    self.users=[]
    self.isLoggedIn=False
    self.currentUser={}

    self.loadUser()


def loadUser(self):
  if os.path.exists('users.json'):
     with open('user.json','r',encoding='utf-8') as file:
      users=json.load(file)
      for user in users:
         user=json.loads(user)
         newUser=User(username = user['username'], password= user ['password'] ,email=user['username'])
         self.users.append(newUser)

     print(self.users)
def register(self,user: User):
  self.user.append(user) #Kullanıcı oluşturuldu
  self.savetoFile()
  print("Kullanıcı oluşturuldu ")

def login (self,username,password):
    for user in self.users:
      if user.username==username and user.password==password:
        self.isLoggedIn=True
        self.currentUser=user
        print('login yapıldı. ')
        break

def savetoFile(self):

   list =[]
   for user in self.users:
      list.append(json.dumps(user._dict_))
   with open ('user.json','w') as file :
      json.dumps(list,file)

repository= UserRepository()
while True:
  print('Menü'.center(50,'*'))
  secim =input('1- Register\n2- Login\n3- Logout\n4-identify')
  if secim=='5':
    break
  else:

   if secim =='1':
      username= input('username : ')
      password=input('password : ')
      email=input('email')
      user=User(username=username,password=password,email=email)
      repository.register(user)
   elif secim =='2':
     username=input('username: ')
     password=input('password:  ')
     repository.login(username,password)
   elif secim =='3':
     pass
   elif secim =='4':
     pass
   else:
     print('Yanlış seçim')
    