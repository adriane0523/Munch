import 'package:flutter/material.dart';
import 'package:munch_mobile/profile.dart';
import 'home.dart';

class History extends StatelessWidget {
  showAlertDialog(BuildContext context) {
    // set up the button
    Widget okButton = TextButton(
        child: Text("OK"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("History"),
      content: Text(
          "This page shows your restaurant history. You can enter them manually or automically (Confirm them using the check or X)"),
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

  addRestaurantDialog(BuildContext context) {
    // set up the button
    Widget noButton = TextButton(
        child: Text("Cancel"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    Widget yesButton = TextButton(
        child: Text("Finish"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("Adding Restaurant"),
      content: Container(
          height: 300.0,
          width: 750.0,
          child: Column(children: <Widget>[
            Padding(
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
              padding: const EdgeInsets.only(
                  left: 0.0, right: 0.0, top: 15, bottom: 0),
              child: TextField(
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Restaurant Name',
                    hintText: 'Enter Restaurant Name'),
              ),
            ),
            Padding(
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
              padding: const EdgeInsets.only(
                  left: 0.0, right: 0.0, top: 15, bottom: 0),
              child: TextField(
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Location',
                    hintText: 'Enter Restaurant Location'),
              ),
            ),
            Padding(
              //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
              padding: const EdgeInsets.only(
                  left: 0.0, right: 0.0, top: 15, bottom: 0),
              child: TextField(
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Your Reccomendation',
                    hintText: 'Enter one item you reccomend'),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Padding(
                    //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
                    padding: const EdgeInsets.only(
                        left: 15.0, right: 15.0, top: 15, bottom: 0),
                    child: new ElevatedButton.icon(
                        onPressed: () {
                          // do something
                        },
                        icon: Icon(Icons.thumb_up),
                        label: Text('Like'))),
                Padding(
                    //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
                    padding: const EdgeInsets.only(
                        left: 15.0, right: 15.0, top: 15, bottom: 0),
                    child: new ElevatedButton.icon(
                        onPressed: () {
                          // do something
                        },
                        icon: Icon(Icons.thumb_down),
                        label: Text('Dislike'))),
              ],
            )
          ])),
      actions: [
        noButton,
        yesButton,
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

  showConfirmDenyDialog(BuildContext context) {
    // set up the button
    Widget noButton = TextButton(
        child: Text("No"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    Widget yesButton = TextButton(
        child: Text("Yes"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
          showReccomendationDialog(context);
        });

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("Did you eat here?"),
      actions: [
        noButton,
        yesButton,
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

  showReccomendationDialog(BuildContext context) {
    // set up the button
    Widget noButton = TextButton(
        child: Text("Cancel"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    Widget yesButton = TextButton(
        child: Text("Done"),
        onPressed: () {
          Navigator.of(context).pop(); // dismiss dialog},
        });

    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      title: Text("Reccomendation"),
      content: Container(
        height: 130.0,
        width: 750.0,
        child: Column(children: <Widget>[
          TextField(
            decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Your Reccomendation',
                hintText: 'Enter one item or leave blank'),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Padding(
                  //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
                  padding: const EdgeInsets.only(
                      left: 15.0, right: 15.0, top: 15, bottom: 0),
                  child: new ElevatedButton.icon(
                      onPressed: () {
                        // do something
                      },
                      icon: Icon(Icons.thumb_up),
                      label: Text('Like'))),
              Padding(
                  //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
                  padding: const EdgeInsets.only(
                      left: 15.0, right: 15.0, top: 15, bottom: 0),
                  child: new ElevatedButton.icon(
                      onPressed: () {
                        // do something
                      },
                      icon: Icon(Icons.thumb_down),
                      label: Text('Dislike'))),
            ],
          )
        ]),
      ),
      actions: [
        noButton,
        yesButton,
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
        centerTitle: true,
        title: Text("History", textAlign: TextAlign.center),
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
          ),
          IconButton(
            icon: Icon(
              Icons.add,
              color: Colors.white,
            ),
            onPressed: () {
              addRestaurantDialog(context);

              // do something
            },
          )
        ],
      ),
      body: ListView.builder(
          itemCount: 10,
          itemBuilder: (BuildContext context, int index) {
            return ListTile(
                contentPadding: EdgeInsets.only(top: 15.0, right: 5),
                leading: Icon(Icons.arrow_right),
                trailing: Column(children: [
                  Icon(Icons.cancel, color: Colors.red),
                  Icon(
                    Icons.check,
                    color: Colors.green,
                  )
                ]),
                onTap: () {
                  showConfirmDenyDialog(context);
                }, // Handle your onTap here.
                title: Text("Restaurant item $index"),
                subtitle: const Text('Chinese - dumplings - fusion\n' +
                    '1081 W 1st street - ' +
                    '2 days ago'));
          }),
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
        currentIndex: 1, //New
      ),
    );
  }
}
