
    FROM anaderi/rep-develop:latest

    ENV TEMP /tmp
    RUN mkdir $TEMP/workdir
    RUN cd $TEMP/workdir && git clone git@github.com:anaderi/ape01.git project
    RUN cd project
    # RUN git checkout <commit_hash>
    
    RUN cp $TEMP/project/./01-ipykee-github/notebook.ipynb /notebooks/ipykee_howto/01-ipykee-github.ipynb
    
    RUN cd / && rm -rf $TEMP/workdir
    