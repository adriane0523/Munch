import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { CheckLoginService } from 'src/lib/check-login.service';
import { authToken, restaurant } from 'src/lib/interfaces/interfaces';
import { PreferencesService } from './preferences.service';

@Component({
  selector: 'app-preferences',
  templateUrl: './preferences.component.html',
  styleUrls: ['./preferences.component.scss']
})
export class PreferencesComponent implements OnInit {

  current_user = '';
  liked_restaurants:restaurant[] = [];

  constructor( 
    private checkLogin: CheckLoginService,
    private router: Router,
    private _snackBar: MatSnackBar,
    private preferenceService: PreferencesService,
    ) { }

  ngOnInit(): void {
    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      if (result && result.result === "false")
      {
        this.router.navigate(['/login'])
      }
    });

    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      if (result && result.result === 'true')
      {
        this.current_user = result.username;
      }
    });

    this.preferenceService.get_liked_restaurants().subscribe((result:restaurant[])=> {
      this.liked_restaurants = result;
    })
  }

}