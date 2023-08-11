How to build the docker image
sudo docker build -t lexical-maestro-llm .


VAR1 could be representing my stage (local, dev, qa, prod)
docker run --env VAR1=value1 --env VAR2=value2 ubuntu env | grep VAR

How to run the docker container
docker run -p 8000:8000 --network host lexical-maestro-llm
sudo docker run -p 8000:8000 lexical-maestro-llm 

How to tag
sudo docker tag aae9abe750b4 thomasmousseau/lexical-maestro:myfirstimage

How to push to docker hub
sudo docker push thomasmousseau/lexical-maestro:myfirstimage  