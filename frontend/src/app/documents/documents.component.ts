import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UploadService } from '../upload.service';
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
  selectedLanguage: string = 'rus';
  user_output: string = '';
  loaded!: boolean;

  uploadSuccess: boolean = false;
  uploadError: boolean = false;
  uploadExpired: boolean = false;

  docInvalidCredentials: boolean = false;
  docWrongFormat:  boolean = false;
  docTextNotRecognizeable:  boolean = false;

  constructor(
    private uploadService: UploadService,
    private languageService: LanguageService
  ) { }

  ngOnInit(): void {
    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
    });

    this.loaded = false;
  }

  onPDF(){
    this.accept = '.pdf';
  }
  onImage(){
    this.accept = '.png';
  }

  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  onDocTypeSelected(event: any): void {
    this.selectedValue = event.target.value;
  }

  onUpload(): void {
    this.loaded = false;
    if (this.selectedFile) {  
      this.uploadService.uploadFile(this.selectedFile, this.accept, this.selectedValue)
        .then(response => {
          if (response.message === "expired"){
            this.uploadError = false;
            this.uploadSuccess = false;
            this.uploadExpired = true;
            this.docInvalidCredentials = false;
            this.docWrongFormat = false;
            this.docTextNotRecognizeable = false;
          }else if (response.message === "valid"){
            this.uploadError = false;
            this.uploadSuccess = true;
            this.uploadExpired = false;
            this.docInvalidCredentials = false;
            this.docWrongFormat = false;
            this.docTextNotRecognizeable = false;
          }else if (response.message === "invalid_credentials"){
            this.uploadError = false;
            this.uploadSuccess = false;
            this.uploadExpired = false;
            this.docInvalidCredentials = true;
            this.docWrongFormat = false;
            this.docTextNotRecognizeable = false;
          }else if(response.message === "wrong_format"){
            this.uploadError = false;
            this.uploadSuccess = false;
            this.uploadExpired = false;
            this.docInvalidCredentials = false;
            this.docWrongFormat = true;
            this.docTextNotRecognizeable = false;
          }else if(response.message === "text_not_recognizeable"){
            this.uploadError = false;
            this.uploadSuccess = false;
            this.uploadExpired = false;
            this.docInvalidCredentials = false;
            this.docWrongFormat = false;
            this.docTextNotRecognizeable = true;
          }
          else{
            this.uploadError = true;
            this.uploadSuccess = false;
            this.uploadExpired = false;
          }
          this.loaded = true;
          console.log(response.is_uploaded, response.is_valid, response.message);
        })
    }else{
      this.uploadError = true;
      this.uploadSuccess = false;
      this.uploadExpired = false;
      this.docInvalidCredentials = false;
      this.docWrongFormat = false;
      this.docTextNotRecognizeable = false;
      this.loaded = true;
    }
  }
}
