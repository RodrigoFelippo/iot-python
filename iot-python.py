# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:01:46 2017

@author: rfpereira
"""
#import random
from firebase import firebase

firebase = firebase.FirebaseApplication('https://iot-tutorial-ce820.firebaseio.com/')
#result = firebase.post('/user',{'Three':{'ThreeChild':'threeChildValue'}})
#resultPut = firebase.put('','lampada','on')
#result = firebase.post('/lampada',{'ID': random.randrange[100000, 999999,6]})

#print(result)
#print(resultPut)

while True:
    
    server = firebase.get('/server',None)
    if(server == "on"):
        firebase.put('','lampada','on')
        firebase.put('','server','off')