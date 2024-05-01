import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UploadService } from '../upload.service';
import { Docs } from '../models';
import { LanguageService } from '../services/language.service';

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
  selectedLanguage: string = 'rus';

  uploadSuccess: boolean = false;
  uploadError: boolean = false;

  constructor(
    private uploadService: UploadService,
    private languageService: LanguageService
  ) { }

  ngOnInit(): void {
    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
    });
  }

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
                this.uploadSuccess = true;
                this.uploadError = false;
        })
        .catch(error => {
          console.error('Upload error', error);
                this.uploadSuccess = false;
                this.uploadError = true;
        });
    }else{
      this.uploadError = true;
    }
  }
}
