import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'history.dart';
import 'home.dart';
import 'main.dart';
import 'types.dart' as types;

class Profile extends StatelessWidget {
  Future<types.Status> logout() async {
    String token = await MyApp.storage.read(key: 'apiToken') ?? '';
    Response response = await post(
      Uri.parse(MyApp.apiUrl + '/logout'),
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
      throw Exception('Failed to login.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text("Profile", textAlign: TextAlign.center),
        actions: <Widget>[
          IconButton(
            icon: Icon(
              Icons.group_add_outlined,
              color: Colors.white,
            ),
            onPressed: () {
              logout().then((value) => {
                    if (value.status == true)
                      {Navigator.pushReplacementNamed(context, '/')}
                  });
            },
          ),
          IconButton(
            icon: Icon(
              Icons.logout,
              color: Colors.white,
            ),
            onPressed: () {
              logout().then((value) => {
                    if (value.status == true)
                      {Navigator.pushReplacementNamed(context, '/')}
                  });
            },
          ),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        onTap: (value) {
          if (value == 0) {
            Navigator.push(
              context,
              PageRouteBuilder(
                pageBuilder: (_, __, ___) => Home(),
                transitionDuration: Duration(seconds: 0),
              ),
            );
          } else if (value == 1) {
            Navigator.push(
              context,
              PageRouteBuilder(
                pageBuilder: (_, __, ___) => History(),
                transitionDuration: Duration(seconds: 0),
              ),
            );
          } else if (value == 2) {
            Navigator.push(
              context,
              PageRouteBuilder(
                pageBuilder: (_, __, ___) => Profile(),
                transitionDuration: Duration(seconds: 0),
              ),
            );
          }
        },

        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Reccomendations',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.list),
            label: 'History',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: 'Profile',
          ),
        ],
        currentIndex: 2, //New
      ),
    );
  }
}
