<h1 align="center">Munch</h1>

<br>
![image](https://user-images.githubusercontent.com/38186787/154870073-3c4c14f9-4315-4a91-b7c5-3346f7da7c6d.png)


## :dart: About ##

Munch is a project that aims to recommend restaurants based on your personal preferances and liked restaurants.
The web app offers everything from a functional login and register system, recommendation score, friend system, search, and info display.


Mobile Demo:
https://youtu.be/n2AeTzv0zl8

Web App Demo:
https://youtu.be/TbIBv9u7GXU

## :rocket: Technologies ##

The following tools were used in this project:
Web app
- [Angular](https://angular.io/)
- [TypeScript](https://www.typescriptlang.org/)

Mobile
- [Flutter](https://flutter.dev)

API
- Python(https://www.python.org/)
- Flask(https://flask.palletsprojects.com/en/2.0.x/)


## :white_check_mark: Architecture ##
Login and register utilizes JWT Architecture. All session tokens are stored locally on the web browser and tokens are generated server side

 ![image](https://user-images.githubusercontent.com/38186787/154869758-e7fff702-31b5-4e35-bb1f-4cc86f438280.png)
 
Recommendation and searching utilizes the sklearn library where we vectorize the liked restaurants and friend-liked restaurants into a TF-ID matrix and find the cosine similarity based on the search params of other restaurants.

![image](https://user-images.githubusercontent.com/38186787/154869982-11fa4afb-9e4a-40bd-8ade-1e8d2bc3bcee.png)


## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/adriane0523/munch

# Access API
$ cd munch/Api

# Install dependencies
$ python -m venv venv
$ soruce venv/bin/activate
$ pip install -r requirements.txt
$ flask run

# Run the FE web app
$ cd front_end/munch-web-app
$ npm install 
$ ng serve

# Run the FE Mobile
$ cd front_end/munch_mobile
# Within code editor open ios sim or android
# Run debug

```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/adriane0523 target="_blank">{{YOUR_NAME}}</a>

&#xa0;

<a href="#top">Back to top</a>
