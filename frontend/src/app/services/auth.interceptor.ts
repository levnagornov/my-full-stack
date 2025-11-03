import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, switchMap } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AuthService } from './auth.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  constructor(private authService: AuthService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const accessToken = localStorage.getItem('access_token');

    let authReq = req;
    if (accessToken) {
      authReq = req.clone({
        setHeaders: { Authorization: `Bearer ${accessToken}` }
      });
    }

    return next.handle(authReq).pipe(
      catchError((err: HttpErrorResponse) => {
        if (err.status === 401) {
          return this.authService.refresh().pipe(
            switchMap(res => {
              localStorage.setItem('access_token', res.access_token);
              const newReq = req.clone({
                setHeaders: { Authorization: `Bearer ${res.access_token}` }
              });
              return next.handle(newReq);
            })
          );
        }
        return throwError(() => err);
      })
    );
  }
}
