import { ChangeDetectionStrategy, Injectable } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CheckLoginService } from 'src/lib/check-login.service';
import { authToken } from 'src/lib/interfaces/interfaces';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class NavbarComponent implements OnInit {
  loggedIn = false
  username = ''
  constructor(
    private checkLogin: CheckLoginService,
    private router: Router) { }

  ngOnInit(): void {
    this.isUserLoggedin();

  }

  get getLogin():boolean{
    return this.loggedIn;
  }

  isUserLoggedin(){
    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      console.log("test" + result);

      if (result && result.result === 'true')
      {
        this.loggedIn = true;
        this.username = result.username;
      }

    });
  }


  logout(){
    this.checkLogin.logout().subscribe((result:authToken)=>{
      if (result && result.result === 'true')
      {
        this.router.navigate(['/login'])
      }
    });
 
  }

}
