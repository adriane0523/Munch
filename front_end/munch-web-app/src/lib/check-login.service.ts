import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpHelperService } from 'src/lib/httpHelper.service';
import { authToken,  } from 'src/lib/interfaces/interfaces'
import { Observable, of } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class CheckLoginService {

  private apiUrl = "http://127.0.0.1:5000/check_login";
  constructor(
    private http: HttpClient,
    private httpHelper: HttpHelperService,
  ) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  isUserLoggedIn():Observable<authToken>{
    return this.http.post<authToken>(this.apiUrl, {"auth_token":localStorage.getItem("token")}, this.httpOptions).pipe(
      tap(_ => console.log("Success")),
      catchError(this.httpHelper.handleError<authToken>('check-login'))
    );
  }
}
