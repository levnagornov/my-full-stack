import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap } from 'rxjs';
import { map } from 'rxjs/operators';

interface RegisterRequest {
  username: string;
  password: string;
  repeatPassword?: string;
}

interface LoginRequest {
  username: string;
  password: string;
}

interface TokenResponse {
  access_token: string;
}


@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000/auth';
  private accessToken$ = new BehaviorSubject<string | null>(null);

  constructor(private http: HttpClient) {
    const token = localStorage.getItem('access_token');
    this.accessToken$.next(token);
  }

  login(data: { username: string; password: string }): Observable<TokenResponse> {
    return this.http.post<TokenResponse>(`${this.apiUrl}/login`, data, { withCredentials: true })
      .pipe(
        tap(res => this.setAccessToken(res.access_token))
      );
  }

  register(data: { username: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, data, { withCredentials: true });
  }

  refresh(): Observable<TokenResponse> {
    return this.http.post<TokenResponse>(`${this.apiUrl}/refresh`, {}, { withCredentials: true })
      .pipe(
        tap(res => this.setAccessToken(res.access_token))
      );
  }

  logout(): Observable<any> {
    return this.http.post(`${this.apiUrl}/logout`, {}, { withCredentials: true })
      .pipe(
        tap(() => this.clearAccessToken())
      );
  }

  setAccessToken(token: string) {
    if (token) {
      localStorage.setItem('access_token', token);
    } else {
      localStorage.removeItem('access_token');
    }
    this.accessToken$.next(token);
  }

  clearAccessToken() {
    this.accessToken$.next(null);
  }

  getAccessToken(): string | null {
    return this.accessToken$.getValue();
  }

  get isLoggedIn$(): Observable<boolean> {
    return this.accessToken$.pipe(map(token => !!token));
  }
}
