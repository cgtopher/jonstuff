1) Create a Dockerfile in the root of the project
    - heres a good walkthrough https://pythonprogramminglanguage.com/python-flask-docker/
    
2) Create a profile on dockerhub
3) `docker login`
4) Build and push the image
5) make a directory named `chart`
6) cd into it and `helm init`
7) edit the yamls that spawn to have it pull your image and expose it at port 5000
8) cUrl localhost:5000/hello and get something back :) 