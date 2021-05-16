import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { getRestaurants, restaurant, send_auth_token } from 'src/lib/interfaces/interfaces';

@Injectable({
  providedIn: 'root'
})
export class MapService {


  private apiUrl = "http://138.197.222.225/";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }

  get_home(): Observable<getRestaurants> {
    return this.http.post<getRestaurants>(this.apiUrl + "home", {"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<getRestaurants>('home'))
    );
  }

  search(query:string): Observable<getRestaurants> {
    return this.http.post<getRestaurants>(this.apiUrl + "search?query="+query,{"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<getRestaurants>('search'))
    );
  }
}
