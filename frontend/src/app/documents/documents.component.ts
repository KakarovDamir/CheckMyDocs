import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UploadService } from '../upload.service';

@Component({
  selector: 'app-documents',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './documents.component.html',
  styleUrl: './documents.component.css'
})
export class DocumentsComponent {
  selectedFile!: File;

  constructor(
    private http: HttpClient,
    private uploadService: UploadService
  ) { }


  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  onUpload(): void {
    if (this.selectedFile) {
      this.uploadService.uploadFile(this.selectedFile)
        .then(response => {
          console.log('Upload successful', response);
          // Handle success
        })
        .catch(error => {
          console.error('Upload error', error);
          // Handle error
        });
    }
  }
}
