
infos=[]
file=open("continuous_Integration.txt","r")
for item in file:
   item=item.strip()
   infos.append(item)
file.close()
print(infos)
