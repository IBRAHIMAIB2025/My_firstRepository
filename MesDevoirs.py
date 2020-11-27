# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:23:34 2019

@author: conte

import os
print(os.listdir)
fichier=open("monfichier.txt","w",encoding="utf-8")
fichier.write("Good morning everyone\n")
fichier.write("This is my first file\n\n")
fichier.write("This file contains my information\n")
fichier.close();

f=open("monfichier.txt","r")
p=open("test.txt","w")
for line in f:
     if(len(line)==1):
         continue
     p.write(line.split("\n")[0]+" ok\n")
f.close()
p.close()
"""

import os
import sys


def readFichier(chemin):
    if (os.path.exists(chemin)):
        with open(chemin,'r') as fi:
            print(fi.read())
    else:
        chemin=input('Donner le chemin absolue ou f pour arreter\n')
        while(chemin!='f' and chemin!='F'):
            if(os.path.exists(chemin)):
                with open(chemin,'r') as fi:
                    print(fi.read())
                    break
            else:
                chemin=input('Donner le chemin absolue ou f pour arreter\n')

#readFichier('monfichier.txt')

def majFichier(chemin,message):
    if(os.path.exists(chemin)):
        with open(chemin,'a') as fi:
            fi.write('\n'+message)
    else:
        with open(chemin,'w') as fi:
            fi.write(message)
            
#majFichier('monfichier.txt','I had had my first certificate in programmation')         

def check_home(chemin):
    sys.path.append(chemin)
    liste_elem=[]
    list_file=[]
    list_dir=[]
    if(os.path.exists(chemin)):
        os.chdir(chemin)
        sys.path.append(chemin)
        liste_elem=os.listdir()
        print("")
        print("LA LISTE DES FICHIERS EST:")
        
        for elem in liste_elem:
           
            if(os.path.isfile(elem)):
                print(elem)
                list_file.append(elem)
        print("")
        print("LA LISTE DES REPERTOIRES EST:")
        for elem in liste_elem:
            
            if(os.path.isdir(elem)):
                print(elem)
                list_dir.append(elem)
    print("On a ",len(list_file)," fichiers et ",len(list_dir)," repertoires")
    sys.path.remove(chemin)

#check_home("C:/") 

def count_word(chemin):
    liste=[]
    nbre_elem=[]
    ind_nb=0
    my_word=""
    if(os.path.exists(chemin)):
        with open(chemin,'r') as fi:
            for line in fi:
                    liste.extend(line.split(" "))
            for elem in liste:
                if(elem=='\n' or elem==''):
                    liste.remove(elem)
            for elem in liste:
                nbre_elem.append(liste.count(elem))
            for val in nbre_elem:
                if(val==max(nbre_elem)):
                    ind_nb=nbre_elem.index(val)
            for elem in liste:
                if(liste.index(elem)==ind_nb):
                    my_word=elem
            print('<'+my_word+'>',' is the word is more repeat in this file')
                
            print('There are ',len(liste),' words in this file')
    else:
        print('File doesn\'t exists, please try again')
            
#count_word('../exopython.txt')
        

  
#convertTempTofile('G:/essai')
matrice1=[3,2,5,6,4,9]
matrice2=[6,8,9,10,3,5]
def somMatrice(ma1,ma2):
    Matrice=[]
    for i in range(len(matrice1)):
        som=matrice1[i]+matrice2[i]
        Matrice.append(som)
       
    print('La somme des deux matrices est: ',Matrice)
#somMatrice([3,2,5,6,4,9],[6,8,9,10,3,5])                   

def delete_double_word(chemin):
    liste_word=[]
    new_liste_word=[]
    liste_global = []
    liste = []
    if(os.path.exists(chemin)):
        with open(chemin,'r') as fi:
            for line in fi:
                liste_word = line.split()
                
                for p in liste_word:
                    if liste_word.count(p)>1:
                        if p not in new_liste_word:
                            new_liste_word.append(p)
                            ind = liste_word.index(p)
                            liste_word[ind] = 'Toto'
                            for elem in new_liste_word:
                                for supp in liste_word:
                                    if elem == supp:
                                        liste_word.remove(supp)
                
                liste_global.append(" ".join(liste_word))
       
        for elemg in liste_global:
            liste.append(elemg)
            liste.append("\n")
        liste_global=" ".join(liste)
        
        with open("C:/Users/conte/Desktop/conte/ess.txt", 'w') as bon:
            bon.write(liste_global)
            
#delete_double_word("C:/Users/conte/Desktop/conte/essai.txt")

#instruction qui affiche le path d'installation du path de python

#print(sys.executable)

                   