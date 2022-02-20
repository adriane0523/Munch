import 'package:flutter/material.dart';
import 'types.dart' as types;

class Restaurant extends StatelessWidget {
  types.Restaurant restaurant;
  Restaurant({required this.restaurant});

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
        appBar: new AppBar(
          title: new Text(restaurant.name),
        ),
        body: Column(
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.only(
                  left: 5, right: 5.0, top: 50, bottom: 0),
              child: Text(
                restaurant.name +
                    "\n" +
                    restaurant.munchType +
                    '\n' +
                    restaurant.addr +
                    "\n" +
                    restaurant.googleRating +
                    " - " +
                    restaurant.googleTotalUserRating +
                    " | " +
                    restaurant.munchRating +
                    "\n\n" +
                    restaurant.hours +
                    "\n",
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ));
  }
}
