
export interface login {
  result:string;
  auth_token:string;
  description:string;
  }

export interface logout{
  result:string;
  description:string;
}

export interface authToken{
  auth_token:string;
  result:string;
  username:string;
}

export interface getRestaurants{
  result:restaurant[];
  description:string;
}
export interface restaurant{
 
  id:number;
  place_id:string;
  name:string;
  addr:string;
  latitude:string;
  longitude:string;
  hours:string;
  google_rating:string;
  google_total_user_rating:string;
  munch_rating:string;
  google_type:string;
  munch_type:string;
  price_level:string;
  menu: menu[];
}

export interface menu{
  id:number;
  header_name:string;
  name:string;
  description:string;
  contains:string;
  price:string;
  image:string;
  restaurant_id:number;
}

export interface register{
  result:string;
  emai:string;
  username:string;
}
