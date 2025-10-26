import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class TasksService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  runTask(taskId: string, formData: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/tasks/${taskId}/run`, formData);
  }
}
