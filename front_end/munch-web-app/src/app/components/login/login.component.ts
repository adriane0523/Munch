import { Component, Input, OnInit } from '@angular/core';
import {LoginService} from "./login.service";
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { httpResult } from "src/lib/interfaces";
import {MatSnackBar} from '@angular/material/snack-bar';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  myForm!: FormGroup;

  constructor(private loginService: LoginService, 
    private fb: FormBuilder,
    private router: Router,
    private _snackBar: MatSnackBar
   )  { }

  ngOnInit(): void {
    this.myForm = this.fb.group({
      
      username: ['', [Validators.required, Validators.minLength(1)]],
      password: ['', [Validators.required, Validators.minLength(1)]]
    });
  }



  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.myForm.value);
    console.log("this is working");
    this.loginService.login(this.myForm.value["username"], this.myForm.value["password"]).subscribe((result:httpResult) => {
      console.log(result)
      if (result.result === "true"){
        this._snackBar.open("Successful Login", "Dismiss", {
          duration: 4000,
          });
        this.router.navigate(['/map'])
      }
      else{
      
      this._snackBar.open("Incorrect Login", "Dismiss", {
      duration: 4000,
      });
      }
    });
  }
}
