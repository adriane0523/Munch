import { Component, Input, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { restaurant } from 'src/lib/interfaces/interfaces';
import { RestaurantPageService } from './restaurant-page.service';

@Component({
  selector: 'app-restaurant-page',
  templateUrl: './restaurant-page.component.html',
  styleUrls: ['./restaurant-page.component.scss']
})
export class RestaurantPageComponent implements OnInit {
  id: number = -1;
  private sub: any;
  restaurant:restaurant;

  constructor(private route: ActivatedRoute, 
    private restaurantPageService: RestaurantPageService,
    private router: Router,
    private _snackBar: MatSnackBar,) { }

  ngOnInit(): void {

    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id']; // (+) converts string 'id' to a number
    console.log(this.id);
   });

   this.restaurantPageService.get_restaurant(this.id).subscribe((restaurant)=>this.restaurant = restaurant);

  }

  back(): void {
    this.router.navigate(["/map"]);
}

like(): void{
  this.restaurantPageService.like(this.id).subscribe((result)=>  this._snackBar.open("Liked " + this.restaurant.name, "Dismiss", {
    duration: 4000,
    }));
 
}


}
