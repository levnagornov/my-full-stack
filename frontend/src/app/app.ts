import { Component, OnInit } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { AuthService } from './services/auth.service';
import { Observable } from 'rxjs';
import { AsyncPipe } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, AsyncPipe],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  isLoggedIn$: Observable<boolean>;

  constructor(private auth: AuthService) {
    this.isLoggedIn$ = this.auth.isLoggedIn$;
  }

  ngOnInit() {
    this.auth.refresh().subscribe({
      next: () => console.log('Token refreshed'),
      error: () => console.log('No valid refresh token')
    });
  }

  logout(event: Event) {
    event.preventDefault();
    this.auth.logout().subscribe(() => {
      this.auth.setAccessToken('');
    });
  }
}
