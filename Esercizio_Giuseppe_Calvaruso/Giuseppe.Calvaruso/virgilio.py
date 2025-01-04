import os

import json

class Virgilio():
     
    def __init__(self,directory):
        self.directory = directory
    
    class CanNotFindError(Exception):
        def __init__(self, message):
          super().__init__(message)
           
   
    
        
    
    def read_canto_lines(self,canto_number,strip_lines=False,num_lines=None):
       
       if canto_number<1 or canto_number>34:
        raise Virgilio.CanNotFindError("canto_number must be between 1 and 34")
       
       else:
        canto_vuoto=[]
        if not isinstance(canto_number,int):
            try:
             file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
            except IndexError:
               return "file non trovato"
               
            if num_lines :
                with open (file_path,"r", encoding="utf-8") as file :
                 lines = file.readlines()

                versi_iniziali=0
                for line in lines:
                    if versi_iniziali<num_lines:
                        if strip_lines :
                           canto_vuoto.append(line.strip())
                        else:   
                         canto_vuoto.append(line)
                        versi_iniziali +=1

                    else:
                        break
            return "\n".join(canto_vuoto)
        
        else:
           raise TypeError("canto_number must be an integer")
    

       
            
       
            
        
     

        
       
    
    def count_verses(self,canto_number):
     #  potrei semplificare il codice con questa scrittura di cui non ho dimestichezza : self.read_canto_line(canto_number)
        file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
        with open(file_path,"r", encoding="utf-8") as file:
            lines = file.readlines()   
        return f"\n il canto {canto_number} ha {len(lines)} versi"
            
    def count_tercets(self,canto_number): 
         file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
         with open(file_path,"r", encoding="utf-8") as file:
            lines = file.readlines()
            terzine_arrotondate = len(lines)//3  
         return f"\n il canto {canto_number} ha {terzine_arrotondate} terzine arrotondato per difetto "
    
    def count_word(self,canto_number,word):
        file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")


        with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()
             unione_linee = "".join(lines)
             parole_contate = unione_linee.count(word)
             
             return f"\nil canto {canto_number}, ha {parole_contate} {word}  ripetuti"

    def get_verse_with_word(self,canto_number,word):
             
        file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
        with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()
             for line in lines:
                 if word in line:
                     return line
                 
    def get_verse_with_words(self,canto_number,word):
        file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
        with open (file_path,"r", encoding="utf-8") as file :
             versi_con_parole_ripetute = []
             lines = file.readlines()
             for line in lines:
                 if word in line:
                     versi_con_parole_ripetute.append(line)

        return versi_con_parole_ripetute
    
    def get_longest_verse(self,canto_number):
        file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
       
        with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()
             verso_lungo = max(lines, key=len)
             
             return f"\n Il verso piu' lungo del canto {canto_number} e' {verso_lungo} di grandezza di {len(verso_lungo)} caratteri"
    
    def get_longest_canto(self):
        canti={}
        for canto_number in range(1,35):
         file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
         with open (file_path,"r", encoding="utf-8") as file :
          lines = file.readlines()   
         
         canti[canto_number]= len(lines)
         canto_piu_lungo_in_numero = max(canti,key=canti.get)
         lunghezza_canto_piu_lungo= canti[canto_piu_lungo_in_numero]
         return f"\nIl canto più lungo è il numero {canto_piu_lungo_in_numero} ed ha {lunghezza_canto_piu_lungo} versi."
    
    def count_words(self,canto_number,words=[]):
         
         file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
         with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()
             unione_linee = "".join(lines)
             for parola in unione_linee:
              if parola in unione_linee:
                 words[parola] += 1
             
         with open("words_count.json","w") as file:
          json.dump(words,file)
         return f"il canto{canto_number} ha la seguente lista di parole {words}"
    
        
    
    def get_hell_verses(self):
        versi=[]
        for canto_number in range(1,35):
         file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
         with open (file_path,"r", encoding="utf-8") as file :
          lines = file.readlines()  
          versi.extend(lines)
        return f" L'inferno Dantesco contiene tutti questi versi {versi}"
    
    def count_hell_verses(self):
        
        versi= 0
        for canto_number in range(1,35):
            file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
            with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()  
             versi += len(lines)
        return f"L'inferno ha un totale di {int(versi)} versi"
    
    def get_hell_verses_mean_len(self):
         versi= 0
         
         word = 0
         for canto_number in range(1,35):
            file_path = os.path.join(self.directory,f"Canto_{canto_number}.txt")
            with open (file_path,"r", encoding="utf-8") as file :
             lines = file.readlines()  
             versi += len(lines)
             for line in lines:
                 line = line.strip()
                 if line:
                     word += len(line.strip())
             
             lunghezza_media = word/versi


         return f"L'inferno ha i versi lunghi mediamente  {lunghezza_media} parole "
    
    
         
        


             
              
        
        
                

            


                     
        

             
            
             
             
            
       
            
        

        
           
        

    
             
            



"""Primo Esercizio"""

percorso_canti = "C:\\Users\dueam\Desktop\Giuseppe.Calvaruso"

# check percorso 
print(percorso_canti) 

# Creo canto con relativo percorso 
# il numero del canto potremmo prenderlo con un input 
canto_scelto = int(input("Ciao sono Virgilio, inserisci il numero del canto "))

canto = Virgilio(percorso_canti)

# Ho scelto il nome canto 2 perche' lavoro con quello
canto2 = canto.read_canto_lines(canto_scelto,True,4)
print(canto2)

 


"""Secondo Esercizio"""

versi_canto_2 = canto.count_verses(canto_scelto)
print(versi_canto_2)


"""Terzo Esercizio"""

terzine_canto_2 = canto.count_tercets(canto_scelto)
print(terzine_canto_2)


"""Quarto esercizio"""
parola_ripetuta = input("Inserisci la parola ripetuta:  ")
parole_ripetute_canto_2 = canto.count_word(canto_scelto,parola_ripetuta)
print(parole_ripetute_canto_2)

"""Quinto esercizio"""

primo_verso_parole_ripetute_canto_2 = canto.get_verse_with_word(canto_scelto,parola_ripetuta)
print (primo_verso_parole_ripetute_canto_2)

"""Sesto esercizio"""
tutti_i_versi_parole_ripetute_canto_2 = canto.get_verse_with_words(canto_scelto,parola_ripetuta)
print(tutti_i_versi_parole_ripetute_canto_2)


"""Settimo esercizio"""
verso_piu_lungo = canto.get_longest_verse(canto_scelto)
print(verso_piu_lungo)

"""Ottavo esercizio"""
canto_con_piu_versi = canto.get_longest_canto()

print(canto_con_piu_versi)

"""Nono esercizio """
lista_parole = canto.count_words(canto_scelto)
print(lista_parole)
"""Decimo esercizio"""
lista_tutti_versi = canto.get_hell_verses()
print(lista_tutti_versi)

"""undicesimo esercizio"""

versi_totali= canto.count_hell_verses()
print(versi_totali)

"""dodicesimo esercizio"""
media_versi = canto.get_hell_verses_mean()
print(media_versi)






            


