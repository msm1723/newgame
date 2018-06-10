# kind of template file for docker env for apps
FROM python

RUN mkdir /container1/
#RUN apt-get update && apt-get upgrade

COPY . /appruntime/
#RUN chmod +x /container/path/program.sh

#VOLUME ["/devvolume"]

#EXPOSE 3000

ENTRYPOINT ["/bin/bash"]
