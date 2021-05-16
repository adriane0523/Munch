import { ThrowStmt } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { CheckLoginService } from 'src/lib/check-login.service';
import { authToken, user } from 'src/lib/interfaces/interfaces';
import { AccountService } from './account.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.scss']
})
export class AccountComponent implements OnInit {

  current_user = '';
  myForm!: FormGroup;
  users:user[];

  

  constructor( private checkLogin: CheckLoginService,
    private router: Router,
    private accountService:AccountService,
    private _snackBar: MatSnackBar,
    private fb: FormBuilder,
    ) { }

  ngOnInit(): void {
    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      if (result && result.result === "false")
      {
        this.router.navigate(['/login'])
      }
    });

    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
      console.log("test" + result);

      if (result && result.result === 'true')
      {
        this.current_user = result.username;
      }
    });

    this.myForm = this.fb.group({
      username: [''],
    });

    this.get_friends();
  }

  add_friends():void{
    console.log(this.myForm.value["username"]);
    this.accountService.add_friend(this.myForm.value["username"]).subscribe((result)=> {
      if(result.result === 'True'){
        this._snackBar.open("Added " + this.myForm.value["username"] , "Dismiss", {
          duration: 5000,
          });
      }
      else{
        this._snackBar.open("Friend Already Added or User does not exist " + this.myForm.value["username"] , "Dismiss", {
          duration: 5000,
          });

      }
      this.get_friends();
      console.log(result)
    });
  }

  get_friends():void{
    this.accountService.get_friends().subscribe((result)=> {
      console.log(result);
      this.users = result.result;
    
    });
  }

}
