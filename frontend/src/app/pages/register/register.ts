import { Component } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  imports: [FormsModule],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
  errorMessage: string | null = null;
  loading = false;

  formData = {
    username: '',
    password: '',
    repeatPassword: ''
  };

  constructor(
    private authService: AuthService,
    private router: Router
  ) { }

  onSubmit(form: NgForm) {
    if (form?.invalid) {
      this.errorMessage = 'Please fix validation errors.';
      return;
    }

    if (this.formData.password !== this.formData.repeatPassword) {
      this.errorMessage = 'Passwords do not match.';
      return;
    }

    this.loading = true;
    this.errorMessage = null;
    
    this.authService.register(this.formData).subscribe({
      next: () => {
        this.loading = false;
        this.authService.login(this.formData).subscribe({
          next: () => this.router.navigate(['/profile']),
          error: () => this.errorMessage = 'Auto login failed.'
        });
      },
      error: (err) => {
        this.loading = false;
        this.errorMessage = err.error?.detail || 'Registration failed.';
      }
    });
  }
}
