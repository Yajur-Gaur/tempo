from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from tika import parser
import tika
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk

from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

nltk.download('punkt')
tika.initVM()

model_name = 'google/pegasus-xsum'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def reduce_text(count,path):
	"""
	generates summaries of individual corpus using sumy library
	"""
	LANGUAGE = "english"
	SENTENCES_COUNT = count
	parser = PlaintextParser.from_file(path, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	summary=""
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		summary+=str(sentence)
	summary=summary.lower()
	return summary

def preprocess_text(text):
    text=text.lstrip()
    stop="\n"*20
    line_space=text.find(stop)
    text=text[:line_space]
    text=text.rstrip()
    text = re.sub(r'\d+', '', text)
    text=text.splitlines()
    text= [x for x in text if len(x.split())>5]
    text= " ".join(text)
    return text
    
def extract_text(filename,file_path,extension):
    extracted_path="/home/khunjahad/syncthing_search/extracted_text/"+str(filename)+".txt"
    
    file_data = parser.from_file(file_path)
    text = file_data["content"]
    text=preprocess_text(text)
    with open(extracted_path,"w") as f:
        print(text,file=f)
    extracted_text=text.split(".")
    count=len(extracted_text)
    return count,extracted_path
    
def preprocess_summarizer(text):
    lines=text.splitlines()
    lines= [line for line in lines if len(line.split())>5]
    text= " ".join(lines)
    text=text.split(".")
    text=[x for x in text if len(x.strip())>0]
    total_sentence=len(text)
    
    batches=[]
    ind=0
    while(ind+5<total_sentence):
        temp=[]
        text=".".join(text[ind:ind+5])
        temp.append(text)
        ind=ind+5
        batches.append(temp)
    temp=[]
    text=".".join(text[ind:total_sentence])
    temp.append(txt)
    batches.append(temp)
    return batches
    
def summarizer(text):
    batches=preprocess_summarizer(text)
    
    batch = tokenizer.prepare_seq2seq_batch(batches, truncation=True, padding='longest',return_tensors="pt").to(torch_device)
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    summary="\n".join(tgt_text)
    return summary
