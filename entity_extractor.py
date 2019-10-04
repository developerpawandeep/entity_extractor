import scispacy
import spacy

nlp = spacy.load("en_core_sci_lg")




import pandas as pd 


df=pd.read_csv("C:/Users/Dragneel/Desktop/Biotechniques-Articles - Papers.csv")
df=df.drop(['Unnamed: 2','Volume'],axis=1)

df=df.dropna()

#df=df.drop(df.index[3])
#df=df.drop(df.index[5])
#df.drop(df.index[])


doc=df['Title'].tolist()


to_process=[]

i=0
entities=[]
for item in doc:
    print(i)
    try:
        doc1=nlp(item)
        #print(list(doc1.sents))
        print(doc1.ents)
        entities.append((doc1.ents))
    except:
        pass
    i+=1

output=[]
for item in entities:     #type is <class 'tuple'>
    print(item)
    
dt = pd.DataFrame(entities, columns =['1', '2', '3','4','5','6','7','8','9','10','11']) 
  

export_csv = dt.to_csv (r'C:/Users/Dragneel/Desktop/out.csv', index = None, header=True)


dn=pd.read_csv("C:/Users/Dragneel/Desktop/out.csv")
