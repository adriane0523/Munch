import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { CheckLoginService } from 'src/lib/check-login.service';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { add_friends, authToken, get_friends, send_auth_token } from 'src/lib/interfaces/interfaces';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  private apiUrl = "http://127.0.0.1:5000/";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }
  
  add_friend(username:string): Observable<add_friends> {
    return this.http.post<add_friends>(this.apiUrl + "friend", {"auth_token":localStorage.getItem("token"), "username":username}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<add_friends>('add friend'))
    );
  }

  get_friends(): Observable<get_friends> {
    return this.http.post<get_friends>(this.apiUrl + "get_friends", {"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<get_friends>('add friend'))
    );
  }
}


