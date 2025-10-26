import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CommitRun } from './commit-run';

describe('CommitRun', () => {
  let component: CommitRun;
  let fixture: ComponentFixture<CommitRun>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CommitRun]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CommitRun);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
