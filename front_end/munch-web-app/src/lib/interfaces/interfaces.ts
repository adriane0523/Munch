
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

export interface register{
  result:string;
  emai:string;
  username:string;
}
