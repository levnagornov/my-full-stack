import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'login',
  templateUrl: './login.html',
  styleUrl: './login.css',
  imports: [ReactiveFormsModule]
})
export class Login {
  // username = '';
  // password = '';
  // msg = '';

  errorMessage: string | null = null;
  loading = false;

  loginForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private auth: AuthService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });
  }


  get username() { return this.loginForm.get('username'); }
  get password() { return this.loginForm.get('password'); }

  onSubmit() {
    if (this.loginForm.invalid) return;

    this.loading = true;
    this.errorMessage = null;

    const { username, password } = this.loginForm.value;

    this.auth.login({ username: username!, password: password! }).subscribe({
      next: () => {
        this.loading = false;
        this.router.navigate(['/profile']);
      },
      error: (err) => {
        this.loading = false;
        this.errorMessage = err.error?.detail || 'Login failed. Please check your credentials.';
      }
    });
  }

  // submit() {
  //   this.auth.login({ username: this.username, password: this.password }).subscribe({
  //     next: (res: any) => {
  //       const token = res.access_token;
  //       this.auth.setAccessToken(token);
  //       this.msg = 'Logged in';
  //     },
  //     error: (err) => {
  //       console.error(err);
  //       this.msg = 'Login failed';
  //     }
  //   });
  // }


}
