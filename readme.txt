1) First update local packages,set git and ananconda using the following commands :
    a) sudo apt update
    b) sudo apt install git
    c) mkdir -p ~/miniconda3
    d) wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    e) bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    f) echo "PATH=$PATH:$HOME/miniconda3/bin" >> ~/.bashrc
    g) source ~/.bashrc
    h) rm -rf ~/miniconda3/miniconda.sh
    i) ~/miniconda3/bin/conda init bash
    j) ~/miniconda3/bin/conda init zsh

2) Installing Java for tika
	a) sudo apt-get update && sudo apt-get upgrade
	b) sudo apt-get install software-properties-common
	c) sudo add-apt-repository ppa:linuxuprising/java
	d) sudo apt-get update
	e) sudo apt-get install oracle-java11-installer
	f) update-alternatives --config java
	g) sudo nano /etc/environment
	h) JAVA_HOME="/your/java/installation-path"
	i) JAVA_HOME="/usr/lib/jvm/java-11-oracle" (example of h)
	j) source /etc/environment
	k) echo $JAVA_HOME
	
3) Create a new conda environment and setup dependencies 
    a) conda create --name pdf_search python=3.6
    b) conda activate pdf_search
    c) git clone "repo which will be added later on"
    d) cd into the repo 
    e) conda install -c gwerbin configspace
    f) git clone https://github.com/Tessellate-Imaging/Monk_Object_Detection.git
    g) cd Monk_Object_Detection/1_gluoncv_finetune/installation && cat requirements_cuda10.1.txt | xargs -n 1 -L 1 pip install
    h) cd ../
    i) python -m pip install -r requirement.txt

4) Install the some softwares that are used
    a) sudo apt-get install tesseract-ocr-all 
    b) sudo apt install poppler-utils


5)  python main.py

# for winows ocr link -- https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0-bibtag19.exe
# conda install -c conda-forge poppler
# pip instal Cython First
