import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Docs } from './models';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  BASE_URL = 'http://localhost:8000'

  constructor(private http: HttpClient) { }

  uploadFile(file: File, file_type: string, doc_type: string): Promise<any> {
    const formData = new FormData();
    formData.append('file', file, file.name);
    formData.append('file_type', file_type);
    formData.append('doc_type', doc_type);
    return this.http.post(`${this.BASE_URL}/api/upload`, formData).toPromise().catch(error => {
      console.error('Upload error', error);
      throw error; // Пробросить ошибку дальше, чтобы компонент мог обработать ее
    });
  }
}
