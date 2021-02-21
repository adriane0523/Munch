import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import {RegisterService } from './register.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  Roles: any = ['Admin', 'Author', 'Reader'];
  

  myForm!: FormGroup;
  check: boolean = false;

  constructor(
    private fb: FormBuilder,
    private registerService : RegisterService,
    private router: Router,
    ) {}

  ngOnInit(): void {
    this.myForm = this.fb.group({
      email: ['',[Validators.required, Validators.pattern('[a-z0-9.@]*')]],
      username: ['', [Validators.required, Validators.minLength(1)]],
      password: ['', [Validators.required, Validators.minLength(1)]],
      password_again: ['', [Validators.required, Validators.minLength(1)]]
    });
  }

  onSubmit() {
    // TODO: Use EventEmitter with form value
    console.warn(this.myForm.value);
    console.log("this is working");
    this.registerService.register(this.myForm.get("username")!.value, 
    this.myForm.get("password")!.value,this.myForm.get("email")!.value).subscribe(result=>{
        console.log(result);
      if (result.result ==="True")
      {
        this.router.navigate(['/login'])
      } 
    });
  }

  checkPasswords(){
    const password = this.myForm.get("password")!.value;
    const password_again = this.myForm.get("password_again")!.value;
    if(this.myForm.valid && (password === password_again))
    {
      return false;
    }
    else{
      return true;
    }
  }

  
}


