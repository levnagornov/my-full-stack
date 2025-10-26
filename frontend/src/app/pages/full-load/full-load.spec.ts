import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FullLoad } from './full-load';

describe('FullLoad', () => {
  let component: FullLoad;
  let fixture: ComponentFixture<FullLoad>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FullLoad]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FullLoad);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
