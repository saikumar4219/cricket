from io import StringIO
from typing import NoReturn
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from os import write
from bs4 import BeautifulSoup
import cv2  
import urllib.request
import numpy as np
import face_recognition
import requests


      


sai=""
content=""
cont={}
l=[]
result=""

def upload(request):
    context={}
    if request.method=='POST':
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        # context['url']=fs.url(name)
        global sai
        sai=upload_file.name
        
        context['url']=upload_file.name  
        content=result(request)
      
        l=content.split('@')
        
        n=len(l)
        # cont['str3']=l[0]
        cont['n']=n
        s="s"
        for i in l:
            cont[s]=i
            s+='1'

           
        # cont['str']=content
        cont['str1']=upload_file.name
    return render(request,'cricket/upload.html',cont)
            
    



def result(request):
    
    
    # url="https://images.news18.com/ibnlive/uploads/2021/09/virat-kohli-bat-skipper-16318006124x3.jpg"
    # urlr="https://pbs.twimg.com/profile_images/1455439930428047363/fv34BaHQ_400x400.jpg"
    # url_response=urllib.request.urlopen(url);
    # url_responser=urllib.request.urlopen(urlr);
    # img_array=np.array(bytearray(url_response.read()),dtype=np.uint8)
    # img_arrayr=np.array(bytearray(url_responser.read()),dtype=np.uint8)
    # img=cv2.imdecode(img_array,1)
    # imgr=cv2.imdecode(img_arrayr,1) 
    ls={"kohli.jpg":"https://www.espncricinfo.com/player/virat-kohli-253802","shardulthakur.jpg":"https://www.espncricinfo.com/player/shardul-thakur-475281","rohit.jpg":"https://www.espncricinfo.com/player/rohit-sharma-34102"}
    
    print(list(ls.keys()))
    for names in list(ls.keys()):
        
        img=cv2.imread(f"media/pics/{names}")
        rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img_encoding=face_recognition.face_encodings(rgb_img)[0]
        img2=cv2.imread(f"media/{sai}")
        rgb_img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
        img_encoding2=face_recognition.face_encodings(rgb_img2)[0]
        result=face_recognition.compare_faces([img_encoding],img_encoding2)
        print(result)
        resultr=result.pop(0)
        result.clear()
        if resultr==True:
            global res
            res=names
            break
            
      
    if(True):
        htmltext=requests.get(ls[res]).text
        soup=BeautifulSoup(htmltext,'lxml')
        playercardpadding=soup.find_all('div',class_="player_overview-grid")
        playerbiodata=soup.find_all('div',class_="more-content-gradient-content")

        str=""
        str2=""
        str3="bio data:"
        for playerdata in playercardpadding:
     
            for data in playerdata:
                data1=data.p.text
                data2=data.h5.text
                str=str+data1+" : "+data2+"\n"+"@"
 
    
        for bio in playerbiodata:
            for bio1 in bio:
                bio2=bio1.text
                str2=str2+bio2+"@"
        str3=str+str2+"@"   
    

    return str3


    