import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {

  lat:number = 33.4255;
  lng:number = -111.9400;
  
  constructor() { }

  ngOnInit(): void {
  }
  
  toggle(event: any) {
    console.log(event);
  }

}
