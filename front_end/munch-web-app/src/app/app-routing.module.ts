import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AccountComponent } from './components/account/account.component';
import {LoginComponent} from "./components/login/login.component";
import { MapComponent } from './components/map/map.component';
import { PreferencesComponent } from './components/preferences/preferences.component';
import {RegisterComponent} from "./components/register/register.component";
import { RestaurantPageComponent } from './components/restaurant-page/restaurant-page.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'map', component: MapComponent },
  { path: 'restaurant/:id', component:RestaurantPageComponent},
  { path: 'account', component: AccountComponent },
  { path: 'preferences', component: PreferencesComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
