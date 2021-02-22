import { Component, OnInit } from '@angular/core';
import { restaurant } from 'src/lib/interfaces/interfaces';
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
  
  constructor(
    private mapService: MapService
  ) { }

  ngOnInit(): void {
    this.mapService.get_home().subscribe((restaurants)=>
    {
      this.restautants = restaurants.result;
      this.convertDollarsign();
      console.log(this.restautants);
    });

  }

  convertDollarsign(){
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
