import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DryRun } from './dry-run';

describe('DryRun', () => {
  let component: DryRun;
  let fixture: ComponentFixture<DryRun>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DryRun]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DryRun);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
