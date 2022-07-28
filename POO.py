# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:40:46 2022

@author: cash
"""

class Users:
    pass

jone=Users()  

jone.id=1

jone.name="jone"

jone.password="12345"

del jone.password


def check_pass_word(user,password):
    return user.password==password

check_pass_word(jone,'12345')

###################################

class Users:
    def check_pass_word(self,password):
        return self.password==password
    
###################################

class User:
   
  def __init__(self, id, name, password):
      
      self.id=id
      self.name=name
      self.password=password
      
  def chec_pass_word(self,password):
      return self.password==password      
    
john = User(1, 'john', '12345')   
john.check_pwd('toto') 
john.check_pwd('12345')

##################################

import crypt
##################################

class Fakefile:
    def read(self, size=0):
        return ""
    def write(self,s):
        return 0
    def close(self):
        pass


f=Fakefile()    
print('foo', file=f)


###################################

class User:
    
    def __init__(self,id, name, password):
        self.id=id
        self.name=name
        self.password=password
        
    def chec_pass_word(self,password):
        return self.password==password
    
    def post(self,message):
        return Post(self,message)
    

class Post:
    def __init__(self,autor,message):
      self.autor=autor
      self.message=message
      
    def format(self):
          return "{} est l'auteur du message : {}".format(self.autor.name,self.message)



user=User(1,'jonh',"123")
p=user.post("comment ça va ?")
print(p.format())

###################################




