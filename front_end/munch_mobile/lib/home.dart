import 'dart:convert';
import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:munch_mobile/history.dart';
import 'package:munch_mobile/profile.dart';
import 'package:munch_mobile/restaurant.dart';
import 'home.dart';
import 'main.dart';
import 'types.dart' as types;

class Home extends StatelessWidget {
  Future<List<types.Restaurant>> getRestaurants() async {
    Response response =
        await get(Uri.parse(MyApp.apiUrl + '/get_all_restaurants'));

    if (response.statusCode == 200) {
      var tagObjsJson = jsonDecode(response.body)['restaurants'] as List;
      List<types.Restaurant> tagObjs = tagObjsJson
          .map((tagJson) => types.Restaurant.fromJson(tagJson))
          .toList();

      return tagObjs;
    } else {
      // If the server did not return a 201 CREATED response,
      // then throw an exception.
      throw Exception('Failed to fetch all restaruants.');
    }
  }

  showAlertDialog(BuildContext context) {
    // set up the button
    Widget okButton = TextButton(
        child: Text("OK"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("Restaurant reccomendation"),
      content: Text(
          "This page shows all your reccomendations based on your friends (check marks) and other people with similar taste."),
      actions: [
        okButton,
      ],
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Reccomendations"),
        actions: <Widget>[
          IconButton(
            icon: Icon(
              Icons.info,
              color: Colors.white,
            ),
            onPressed: () {
              showAlertDialog(context);

              // do something
            },
          )
        ],
      ),
      body: Container(
          child: FutureBuilder<List<types.Restaurant>>(
              future: getRestaurants(),
              builder: (BuildContext context, AsyncSnapshot snapshot) {
                if (snapshot.hasData) {
                  return ListView.builder(
                      padding: EdgeInsets.all(8),
                      itemCount: snapshot.data.length,
                      itemBuilder: (BuildContext context, int index) {
                        return ListTile(
                            contentPadding: EdgeInsets.only(top: 3.0, right: 2),
                            leading: Icon(Icons.arrow_right),
                            trailing: Icon(Icons.check, color: Colors.green),
                            onTap: () {
                              Navigator.push(
                                context,
                                new MaterialPageRoute(
                                    builder: (context) => new Restaurant(
                                          restaurant: snapshot.data[index],
                                        )),
                              );
                            }, // Handle your onTap here.
                            title: Text(snapshot.data[index].name),
                            subtitle: Text(snapshot.data[index].priceLevel +
                                " | " +
                                snapshot.data[index].munchType +
                                "\n" +
                                snapshot.data[index].googleRating +
                                " - " +
                                snapshot.data[index].googleTotalUserRating +
                                " | " +
                                snapshot.data[index].munchRating));
                      });
                } else {
                  return Center(child: CircularProgressIndicator());
                }
              })),

      // ListView.builder(
      //     itemCount: 10,
      //     itemBuilder: (BuildContext context, int index) {
      //       return ListTile(
      //           contentPadding: EdgeInsets.only(top: 10.0, right: 5),
      //           leading: Icon(Icons.arrow_right),
      //           trailing: Icon(Icons.check, color: Colors.green),
      //           onTap: () {
      //             Navigator.push(
      //               context,
      //               new MaterialPageRoute(
      //                   builder: (context) => new Restaurant()),
      //             );
      //           }, // Handle your onTap here.
      //           title: Text("Restaurant item $index"),
      //           subtitle: const Text('Chinese - dumplings - fusion\n' +
      //               '1081 W 1st street - 2mi - 4/5\n' +
      //               'Friend reccomended the Pizza'));
      //     }),
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
        currentIndex: 0, //New
      ),
    );
  }
}
