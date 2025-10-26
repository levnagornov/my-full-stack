import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  imports: [FormsModule],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
  username = '';
  password = '';
  msg = '';

  constructor(private auth: AuthService) {}

  submit() {
    this.auth.register({username: this.username, password: this.password}).subscribe({
      next: (res: any) => {
        const token = res.access_token;
        this.auth.setAccessToken(token);
        this.msg = "Registration is successful!"
      }, 
      error: (err) => {
        console.error(err);
        this.msg = "Registratio failed. " + err.message
      }
    });
  }
}
