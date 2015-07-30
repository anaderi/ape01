FROM anaderi/rep-develop:latest

RUN mkdir -p /notebooks/ipykee_howto
RUN cd /notebooks/ipykee_howto && git clone https://github.com/anaderi/ape01.git ape01 # && git checkout <commit_hash>
ENV PROJECT_PATH /notebooks/ipykee_howto/ape01
RUN cp $PROJECT_PATH/./01-ipykee-github/notebook.ipynb $PROJECT_PATH/01-ipykee-github.ipynb