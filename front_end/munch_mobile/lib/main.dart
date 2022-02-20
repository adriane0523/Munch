import 'dart:convert';
import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:munch_mobile/history.dart';
import 'package:munch_mobile/profile.dart';
import 'package:munch_mobile/register.dart';
import 'home.dart';
import 'types.dart' as types;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  static String apiUrl = 'http://127.0.0.1:5000/';
  static final storage = new FlutterSecureStorage();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => LoginDemo(),
        '/home': (context) => Home(),
        '/register': (context) => Register(),
        '/history': (context) => History(),
        '/profile': (context) => Profile(),
      },
      theme: ThemeData(
          primaryColor: Color.fromRGBO(225, 139, 34, 1),
          elevatedButtonTheme: ElevatedButtonThemeData(
            style: ElevatedButton.styleFrom(
              primary: Color.fromRGBO(225, 139, 34, 1),
            ),
          ),
          textButtonTheme: TextButtonThemeData(
              style: TextButton.styleFrom(
            primary: Color.fromRGBO(225, 139, 34, 1),
          ))),
    );
  }
}

class LoginDemo extends StatefulWidget {
  @override
  Login createState() => Login();
}

class Login extends State<LoginDemo> {
  Future<types.Status> login(String username, String password) async {
    Response response = await post(
      Uri.parse(MyApp.apiUrl + '/login'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(
          <String, String>{'username': username, 'password': password}),
    );

    if (response.statusCode == 200) {
      return types.Status.fromJson(jsonDecode(response.body));
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.
      throw Exception('Failed to login.');
    }
  }

  Future<types.Status> checkLogin() async {
    String token = await MyApp.storage.read(key: 'apiToken') ?? '';
    Response response = await post(
      Uri.parse(MyApp.apiUrl + '/check_login'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{'auth_token': token}),
    );

    if (response.statusCode == 200) {
      return types.Status.fromJson(jsonDecode(response.body));
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.
      throw Exception('Users already exists');
    }
  }

  @override
  void initState() {
    checkLogin().then((value) => {
          if (value.status == true)
            {
              Navigator.push(
                context,
                PageRouteBuilder(
                  pageBuilder: (_, __, ___) => Home(),
                  transitionDuration: Duration(seconds: 0),
                ),
              )
            }
        });

    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final passwordController = TextEditingController();
    final usernameController = TextEditingController();
    return Scaffold(
      backgroundColor: Colors.white,
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.only(top: 150.0),
              child: Center(
                child: Container(
                    width: 200,
                    height: 150,
                    margin: const EdgeInsets.only(
                        left: 0, right: 0, top: 0, bottom: 80),
                    /*decoration: BoxDecoration(
                        color: Colors.red,
                        borderRadius: BorderRadius.circular(50.0)),*/
                    child: Image.asset('assets/images/logo.png')),
              ),
            ),
            Padding(
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
              padding: EdgeInsets.symmetric(horizontal: 15),
              child: TextField(
                controller: usernameController,
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Username',
                    hintText: 'Enter valid username'),
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(
                  left: 15.0, right: 15.0, top: 15, bottom: 0),
              //padding: EdgeInsets.symmetric(horizontal: 15),
              child: TextField(
                controller: passwordController,
                obscureText: true,
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Password',
                    hintText: 'Enter secure password'),
              ),
            ),
            TextButton(
              onPressed: () {
                //TODO FORGOT PASSWORD SCREEN GOES HERE
              },
              child: Text(
                'Forgot Password',
                style: TextStyle(
                    color: Color.fromRGBO(225, 139, 34, 1), fontSize: 15),
              ),
            ),
            Container(
              height: 50,
              width: 250,
              decoration: BoxDecoration(
                  color: Color.fromRGBO(225, 139, 34, 1),
                  borderRadius: BorderRadius.circular(20)),
              child: TextButton(
                onPressed: () {
                  login(usernameController.text, passwordController.text)
                      .then((value) async => {
                            if (value.status == true)
                              {
                                await MyApp.storage.write(
                                    key: 'apiToken', value: value.authToken),
                                Navigator.push(
                                  context,
                                  PageRouteBuilder(
                                    pageBuilder: (_, __, ___) => Home(),
                                    transitionDuration: Duration(seconds: 0),
                                  ),
                                )
                              }
                            else
                              {
                                ScaffoldMessenger.of(context).showSnackBar(
                                  SnackBar(
                                    content: const Text(
                                        'Incorrect username or password'),
                                    duration: const Duration(seconds: 2),
                                    action: SnackBarAction(
                                      label: 'OK',
                                      onPressed: () {},
                                    ),
                                  ),
                                )
                              }
                          });
                },
                child: Text(
                  'Login',
                  style: TextStyle(color: Colors.white, fontSize: 25),
                ),
              ),
            ),
            SizedBox(
              height: 130,
            ),
            new TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  new MaterialPageRoute(builder: (context) => new Register()),
                );
              },
              child: Text(
                'New User? Create Account',
                style: TextStyle(color: Color.fromRGBO(225, 139, 34, 1)),
              ),
            )
          ],
        ),
      ),
    );
  }
}
