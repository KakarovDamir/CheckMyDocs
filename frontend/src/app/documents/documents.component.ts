import { Component } from '@angular/core';
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
  accept: string = '';

  constructor(
    private uploadService: UploadService
  ) { }

  onPDF(){
    this.accept = '.pdf';
  }
  onImage(){
    this.accept = '.jpg, .jpeg, .png';
  }

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
