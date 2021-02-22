import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { getRestaurants, restaurant } from 'src/lib/interfaces/interfaces';

@Injectable({
  providedIn: 'root'
})
export class MapService {


  private apiUrl = "http://127.0.0.1:5000/home";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }

  get_home(): Observable<getRestaurants> {
    return this.http.post<getRestaurants>(this.apiUrl, {}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<getRestaurants>('home'))
    );
  }
}
