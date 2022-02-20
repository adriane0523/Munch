import { Component, ElementRef, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CheckLoginService } from 'src/lib/check-login.service';
import { authToken, restaurant } from 'src/lib/interfaces/interfaces';
import { MapService } from './map.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {

  lat:number = 33.4255;
  lng:number = -111.9400;
  restautants:restaurant[] = [];
  myForm!: FormGroup;
  
  constructor(
    private mapService: MapService,
    private elementRef: ElementRef,
    private checkLogin: CheckLoginService,
    private router: Router,
    private fb: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.checkLogin.isUserLoggedIn().subscribe((result:authToken)=>{
        if (result && result.result === "false")
        {
          this.router.navigate(['/login'])
        }
    
    });

    this.mapService.get_home().subscribe((restaurants)=>
    {
      this.restautants = restaurants.result;
      this.restautants.sort((a,b)=>b.percentage - a.percentage)
      this.convertDollarsign();
    });

    this.myForm = this.fb.group({
      search: [''],
    });
  }

  search_query():void{
    this.mapService.search(this.myForm.value["search"]).subscribe((restaurants)=>
    {
      this.restautants = restaurants.result;
      this.restautants.sort((a,b)=>b.percentage - a.percentage)
      this.convertDollarsign();

    });

  }

  ngAfterViewInit():void{
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#fff';
 }

  convertDollarsign():void{
    for (let i = 0; i < this.restautants.length; i++)
    {
      if (this.restautants[i].price_level != '')
      {
        let x:number = +this.restautants[i].price_level
        this.restautants[i].price_level ='';
        while(x > 0)
        {
          this.restautants[i].price_level += '$';
          x--;
        }
      }
    }
  }

  getImage(r:restaurant):string{
    //const index = Math.floor((Math.random() * r.menu.length-1) + 0);
    const index = 0;
    if( r.menu[index] && r.menu[index] != undefined && r.menu[index].image && r.menu[index].image !=''){
      return 'http://127.0.0.1:5000/static/photos/' + r.menu[index].image
    }
    else return '';

  }
  toggle(event: any) {
    console.log(event);
  }

}
