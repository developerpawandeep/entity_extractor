from bs4 import BeautifulSoup
import requests 
import os
import glob
import shutil



with open("Papers.html", encoding="utf-8") as f:
    data = f.read()
    soup = BeautifulSoup(data, 'html.parser')

links_with_text = []
for a in soup.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])


root="https://www.future-science.com/doi/"
     


final_links = [root + "pdf/" + url.replace(root,"") for url in links_with_text ]

root ="https://www.future-science.com/doi/pdf/"
os.mkdir("pdf")
j=1198
duplicacy = []
for item in final_links[1198:]:
    if item in duplicacy:
        continue
    duplicacy.append(item)
    try:
        r = requests.get(item,stream=True)
    except: pass
    with open("pdf/"+"doi"+str(j)+".pdf",'wb') as f:
        print('pass')
        for chunks in r.iter_content(chunk_size=1024):
            if chunks:
                f.write(chunks)
    j+=1
        
j=0






SOURCE_DIR = 'C:/Users/Dragneel/Desktop/pdf/pdf'
ROOT_DIR = 'C:/Users/Dragneel/Desktop/pdf/All_pdf'

j=0

# =============================================================================
# 
# for f in glob.glob('C:/Users/Dragneel/Desktop/pdf/pdf/*.pdf'): 
#     j+=1
# 
# =============================================================================
for fname in os.listdir(SOURCE_DIR):
    if fname.lower().endswith(".pdf"):
        os.mkdir(os.path.join(ROOT_DIR,fname))
        DEST_DIR=(os.path.join(ROOT_DIR,fname))
        shutil.move(os.path.join(SOURCE_DIR, fname), DEST_DIR)
        j+=1
        print(j)
      
# =============================================================================
#         
# for f in glob.glob('C:/Users/Dragneel/Desktop/pdf/pdf/*.pdf'):
#     os.mkdir("pdf"+str(j))
#     print(j)
#     j+=1
# 
# 
# =============================================================================



# =============================================================================
# from selenium import webdriver 
# import time 
#   
# # set webdriver path here it may vary 
# brower = webdriver.Chrome(executable_path ="chromedriver.exe") 
#   
# website_URL ="https://www.google.co.in/"
# brower.get(url) 
# html=brower.page_source
# 
# soup=BeautifulSoup(html,"lxml")
# 
# soup.find("div",{"class","()})  
# 
# =============================================================================

# =============================================================================
#         
# j=0
# new_links=[]      
# new_html=[]    
# for item in links_with_text:
#     print(j)
#     file_url = item   
#     page = requests.get(file_url)
#     soup = BeautifulSoup(page.text, 'html.parser')
#     for a in soup.find_all('a', href=True): 
#         if a.text: 
#             new_links.append(a['href'])
#     j+=1
#     
#     
# 
# =============================================================================

# =============================================================================
# i=0        
# 
#     
#     r = requests.get(file_url, stream = True) 
#     doc=(r.text)
#     with open("python.pdf","wb") as pdf: 
#         for chunk in r.iter_content(chunk_size=1024): 
#   
#             # writing one chunk at a time to pdf file 
#             if chunk: 
#                 pdf.write(chunk) 
# 
#             print(i)
#             i+=1
# =============================================================================
