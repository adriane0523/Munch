import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { getRestaurants, restaurant, send_auth_token } from 'src/lib/interfaces/interfaces';

@Injectable({
  providedIn: 'root'
})
export class RestaurantPageService {


  private apiUrl = "http://127.0.0.1:5000/";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }
  
  get_restaurant(query:number): Observable<restaurant> {
    return this.http.get<restaurant>(this.apiUrl + "get_restaurant?query="+query, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<restaurant>('search'))
    );
  }

  like(query:number): Observable<send_auth_token> {
    return this.http.post<send_auth_token>(this.apiUrl + "like_restaurant?query="+query, {"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<send_auth_token>('like'))
    );
  }
}



