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
  selectedFile!: File | null;
  selectedValue: string = '';
  accept: string = '';
  doc!: Docs;
  selectedLanguage: string = 'rus';
  user_output: string = '';
  id!: number;

  uploadSuccess: boolean = false;
  uploadError: boolean = false;
  uploadProblem: boolean = false;

  constructor(
    private uploadService: UploadService,
    private languageService: LanguageService
  ) { }

  ngOnInit(): void {
    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
      if(language === 'rus'){
        this.id = 1;
      }
      else if(language === 'en'){
        this.id = 2;
      }
      else{
        this.id = 3;
      }
      console.log(this.id);
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
          // if(response.is_upload === true){
          //   if(response.is_valid === true){
          //     this.user_output = response.message;
          //     this.uploadSuccess = true;
          //     this.uploadError = false;
          //     this.uploadProblem = false;
          //   }
          //   else{
          //     this.user_output = response.answer[response][this.id];
          //     this.uploadProblem = true;
          //     this.uploadSuccess = false;
          //     this.uploadError = false;
          //   }
          // }else{
          //   this.uploadError = true;
          //   this.uploadSuccess = false;
          //   this.uploadProblem = false;
          // }
          console.log(response);
        })
    }else{
      this.uploadError = true;
      this.uploadSuccess = false;
      this.uploadProblem = false;
    }
    this.selectedFile = null;
    this.selectedValue = '';
    this.accept = '';
  }
}
