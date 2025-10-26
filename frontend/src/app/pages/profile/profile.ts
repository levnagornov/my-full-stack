import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { JsonPipe } from '@angular/common';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'profile',
  templateUrl: './profile.html',
  imports: [JsonPipe, CommonModule]
})
export class Profile {
  profile: any = null;
  msg = '';

  constructor(private auth: AuthService, private http: HttpClient) {}

  loadProfile() {
    const token = this.auth.getAccessToken();
    if (!token) {
      this.msg = 'No access token — try login or refresh';
      return;
    }
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    this.http.get('http://localhost:8000/users/me', { headers }).subscribe({
      next: (res) => { this.profile = res; this.msg = ''; },
      error: (err) => {
        console.error(err);
        this.msg = 'Access failed — try refresh';
      }
    });
  }

  refresh() {
    this.auth.refresh().subscribe({
      next: (res: any) => {
        this.auth.setAccessToken(res.access_token);
        this.msg = 'Refreshed token';
      },
      error: (err) => { 
        console.error(err);
        this.msg = "Refresh failed. " + err.message
      }
    });
  }
}
