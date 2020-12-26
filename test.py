f=open("./downloads/sample4.txt","r")
text=f.read()
lines=text.splitlines()
lines= [line for line in lines if len(line.split())>5]
text= " ".join(lines)
text=text.split(".")
text=[x for x in text if len(x.strip())>0]
total_sentence=len(text)
#print(text)
f.close()
print(total_sentence)
# making batches of the text for google pegasus

batches=[]
# we make batches of 
ind=0

while(ind+5<total_sentence):
    batches.append(".".join(text[ind:ind+5]))
    ind=ind+5
batches.append(".".join(text[ind:total_sentence]))

print(len(batches))
print(batches)