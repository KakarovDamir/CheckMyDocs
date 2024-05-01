import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UploadService } from '../upload.service';
import { Docs } from '../models';

@Component({
  selector: 'app-documents',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './documents.component.html',
  styleUrl: './documents.component.css'
})
export class DocumentsComponent {
  selectedFile!: File;
  selectedValue: string = '';
  accept: string = '';
  doc!: Docs;

  constructor(
    private uploadService: UploadService
  ) { }

  onPDF(){
    this.accept = '.pdf';
    // this.doc.file_type = this.accept;
  }
  onImage(){
    this.accept = '.png';
    // this.doc.file_type = this.accept;
  }

  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  onDocTypeSelected(event: any): void {
    this.selectedValue = event.target.value;
  }

  onUpload(): void {
    if (this.selectedFile) {  
      this.uploadService.uploadFile(this.selectedFile, this.accept, this.selectedValue)
        .then(response => {
          console.log('Upload successful', response);
        })
        .catch(error => {
          console.error('Upload error', error);
          // Handle error
        });
    }else{
      console.error('Upload error', 'Please select a file, a document type and a file type');
    }
  }
}
