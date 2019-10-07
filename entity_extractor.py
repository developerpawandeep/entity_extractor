import scispacy
import spacy

nlp = spacy.load("en_core_sci_lg")

#nlp1 = spacy.load("en-ner-jnlpba-md")



import pandas as pd 


df=pd.read_csv("C:/Users/Dragneel/Desktop/Biotechniques-Articles - Papers.csv")
df=df.drop(['Unnamed: 2','Volume'],axis=1)

df=df.dropna()

#df=df.drop(df.index[3])
#df=df.drop(df.index[5])
#df.drop(df.index[])


doc=df['Title'].tolist()
df.to_csv('last_5_final.csv')

to_process=[]
item_list=[]
i=0
entities=[]
for item in doc:
    print(i)
    try:
        doc1=nlp(item)
        #doc2=nlp1(item)
        #print(list(doc1.sents))
        #print(doc1.ents)
        #print(doc2.ents)
        entities.append((doc1.ents))
        item_list.append(item)
    except:
        pass
    i+=1

output=[]
for item in entities:     #type is <class 'tuple'>
    print(item)
    
    
merge_to_dx=pd.DataFrame(item_list,columns=['title'])   
dx = pd.DataFrame(entities, columns =['1', '2', '3','4','5','6','7','8','9','10','11']) 
 
dt = pd.concat([merge_to_dx, dx], axis=1, sort=False)

export_csv = dt.to_csv (r'C:/Users/Dragneel/Desktop/out.csv', index = None, header=True)


dn=pd.read_csv("C:/Users/Dragneel/Desktop/out.csv")
