MicroServices Demo
==================

For the presentation:
https://docs.google.com/presentation/d/1uQl8CN142gVnno5WZ7DK5JqHoOkTYCwrBFQyEc-4E7w/edit?usp=sharing

userservice/
- Requires python (2.7)
- Requires pip
- Requies virtualenv

    ../userservice/$ virtualenv .
    ../userservice/$ pip install -r dependencies.txt
    ../userservice/$ source bin/activate
    ../userservice/$ python app/server.py


spamservice/
- Requires node
- deps in package.json

    ../spamservice$ npm install
    ../spamservice$ node app/index.js


generatorservice/
- Requires python (2.7)
- Requires pip
- Requies virtualenv

    ../generatorservice/$ virtualenv .
    ../generatorservice/$ pip install -r dependencies.txt
    ../generatorservice/$ source bin/activate
    ../generatorservice/$ python app/generator.py


