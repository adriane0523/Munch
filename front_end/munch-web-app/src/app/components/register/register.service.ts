import { Injectable } from '@angular/core';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { register } from 'src/lib/interfaces/interfaces';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  private apiUrl = "http://138.197.222.225/register";

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService
  ) { }



  register(username:string, password:string, email:string): Observable<register> {
    return this.http.post<register>(this.apiUrl, {username:username, password:password, email:email}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<any>('login'))
    );
  }

}
