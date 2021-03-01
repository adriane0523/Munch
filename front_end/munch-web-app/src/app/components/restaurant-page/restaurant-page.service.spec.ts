import { TestBed } from '@angular/core/testing';

import { RestaurantPageService } from './restaurant-page.service';

describe('RestaurantPageService', () => {
  let service: RestaurantPageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RestaurantPageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
