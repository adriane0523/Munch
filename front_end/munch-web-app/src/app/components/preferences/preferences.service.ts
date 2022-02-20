import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { tap, catchError } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { add_friends, get_friends, restaurant } from 'src/lib/interfaces/interfaces';


@Injectable({
  providedIn: 'root'
})
export class PreferencesService {
  private apiUrl = "http://127.0.0.1:5000/";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }
  
  get_liked_restaurants(): Observable<restaurant[]> {
    return this.http.post<restaurant[]>(this.apiUrl + "get_like_restaurant", {"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<restaurant[]>('add friend'))
    );
  }
}

