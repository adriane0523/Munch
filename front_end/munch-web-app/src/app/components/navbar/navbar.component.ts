import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CheckLoginService } from 'src/lib/check-login.service';
import { authToken } from 'src/lib/interfaces/interfaces';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(
    private checkLogin: CheckLoginService,
    private router: Router) { }

  ngOnInit(): void {
  }

  isUserLoggedin(){
    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      console.log(result);
      if (result.result)
      {
        return true;
      }
      return false;
    });
  }
}
