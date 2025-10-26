import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000/auth';
  private accessToken$ = new BehaviorSubject<string | null>(null);

  constructor(private http: HttpClient) {}

  login(data: { username: string; password: string }): Observable<any> {
    // Server returns access token in body; refresh token is set as HttpOnly cookie
    return this.http.post(`${this.apiUrl}/login`, data, { withCredentials: true });
  }

  refresh(): Observable<any> {
    return this.http.post(`${this.apiUrl}/refresh`, {}, { withCredentials: true });
  }

  logout(): Observable<any> {
    return this.http.post(`${this.apiUrl}/logout`, {}, { withCredentials: true });
  }

  setAccessToken(token: string) {
    this.accessToken$.next(token);
  }

  getAccessToken(): string | null {
    return this.accessToken$.getValue();
  }
}
