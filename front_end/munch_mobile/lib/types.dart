class Status {
  final String authToken;
  final bool status;

  Status({required this.authToken, required this.status});

  factory Status.fromJson(Map<String, dynamic> json) {
    return Status(
      authToken: json['auth_token'] == null ? '' : json['auth_token'],
      status: json['status'],
    );
  }
}

// class Restaurants {
//   final List<Restaurant> restaurants;

//   Restaurants({required this.restaurants});

//   factory Restaurants.fromJson(Map<Restaurant, dynamic> json) {
//     return Restaurants(
//       restaurants: json['restaurants'],
//     );
//   }
// }

class Restaurant {
  final String placeId;
  final String name;
  final String addr;
  final String latitude;
  final String longitude;
  final String hours;
  final String googleRating;
  final String googleTotalUserRating;
  final String munchRating;
  final String googleType;
  final String munchType;
  final String priceLevel;
  final List<MenuItem> menu;

  Restaurant(
      {required this.placeId,
      required this.name,
      required this.addr,
      required this.googleRating,
      required this.googleTotalUserRating,
      required this.googleType,
      required this.hours,
      required this.latitude,
      required this.longitude,
      required this.menu,
      required this.munchRating,
      required this.munchType,
      required this.priceLevel});

  factory Restaurant.fromJson(Map<String, dynamic> json) {
    return Restaurant(
        placeId: json['auth_token'] == null ? '' : json['auth_token'],
        name: json['name'] == null ? '' : json['name'],
        addr: json["addr"] == null ? '' : json['addr'],
        googleRating:
            json["google_rating"] == null ? '' : json['google_rating'],
        googleTotalUserRating: json["google_total_user_rating"] == null
            ? ''
            : json['google_total_user_rating'],
        googleType: json["googleType"] == null ? '' : json['googleType'],
        hours: json["hours"] == null ? '' : json['hours'],
        latitude: json["latitude"] == null ? '' : json['latitude'],
        longitude: json['longitude'] == null ? '' : json['longitude'],
        menu: json["menu"] == null
            ? []
            : (json["menu"] as List)
                .map((tagJson) => MenuItem.fromJson(tagJson))
                .toList(),
        munchRating: json["munch_rating"] == null ? '' : json['munch_rating'],
        munchType: json["munch_type"] == null ? '' : json['munch_type'],
        priceLevel: json["price_level"] == null ? '' : json['price_level']);
  }
}

class MenuItem {
  final String headerName;
  final String name;
  final String description;
  final String contains;
  final String price;
  final String image;
  final int restaurantId;

  // ignore: non_constant_identifier_names
  MenuItem(
      {required this.headerName,
      required this.name,
      required this.description,
      required this.contains,
      required this.image,
      required this.price,
      required this.restaurantId});

  factory MenuItem.fromJson(Map<String, dynamic> json) {
    return MenuItem(
        headerName: json["hedaderName"] == null ? '' : json["header_name"],
        name: json["name"],
        description: json["description"] == null ? '' : json["description"],
        contains: json["contains"] == null ? '' : json["contains"],
        price: json["price"] == null ? '' : json["price"],
        image: json["image"] == null ? '' : json["image"],
        restaurantId: json["restaurantId"] == null ? '' : json["restaurantId"]);
  }
}

class User {
  final String name;
  final String username;
  final String email;
  final String preferances;
  final String firebaseId;
  final String registeredOn;

  // ignore: non_constant_identifier_names
  User(
      {required this.name,
      required this.username,
      required this.email,
      required this.preferances,
      required this.firebaseId,
      required this.registeredOn});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
        name: json["name"],
        username: json["username"] == null ? '' : json["username"],
        email: json["email"] == null ? '' : json["email"],
        preferances: json["preferances"] == null ? '' : json["preferances"],
        firebaseId: json["firebaseId"] == null ? '' : json["firebaseId"],
        registeredOn: json["registeredOn"] == null ? '' : json["registeredOn"]);
  }
}
