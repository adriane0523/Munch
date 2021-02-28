import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {


  constructor(public router: Router) {

  }
    
  isOnLogin():boolean{
    return (this.router.url !== '/login' && this.router.url !== '/register');

  }

  backgroundColor():string{
    if (this.isOnLogin()){
      return '#fed8b1';
    }
    else return '#fff';
  }

  title = 'munch-web-app';
}
