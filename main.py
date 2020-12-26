import inotify.adapters
from utils import *
notifier = inotify.adapters.Inotify()
notifier.add_watch('/home/khunjahad/syncthing_search/uploads')

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CREATE' in event[1]:
            file=event[3]
            filename,extension=file.split(".")
            file_path=str(event[2])+"/"+file
            print("The name of the complete file is : ",file)
            print("The filename without extension is : ",filename)
            print("The extension of the file is : ",extension)
            print("The file_path of the file is : ",file_path)
            count,extracted_path=extract_text(filename,file_path,extension)
            reduced_text=reduce_text(count/2,extracted_path)
            
            summary=summarizer(reduced_text)
            saving_path="/home/khunjahad/syncthing_search/downloads/"+str(filename)+".txt"
            
            with open(saving_path,"w") as f:
                print(summary,file=f)