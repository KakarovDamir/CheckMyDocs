import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  BASE_URL = 'http://localhost:8000'

  constructor(private http: HttpClient) { }

  uploadFile(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file, file.name);

    return this.http.post(`${this.BASE_URL}/api/upload`, formData).toPromise();
  }
}
