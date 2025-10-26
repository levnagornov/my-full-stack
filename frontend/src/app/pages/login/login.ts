import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'login',
  templateUrl: './login.html',
  imports: [FormsModule]
})
export class Login {
  username = '';
  password = '';
  msg = '';

  constructor(private auth: AuthService) {}

  submit() {
    this.auth.login({ username: this.username, password: this.password }).subscribe({
      next: (res: any) => {
        const token = res.access_token;
        this.auth.setAccessToken(token);
        this.msg = 'Logged in';
      },
      error: (err) => {
        console.error(err);
        this.msg = 'Login failed';
      }
    });
  }

  logout() {
    this.auth.logout().subscribe(() => {
      this.auth.setAccessToken('');
      this.msg = 'Logged out';
    });
  }
}
