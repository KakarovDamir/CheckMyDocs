import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule,FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Verification of documents for authenticity';
  selectedFile!: File;

  constructor(private http: HttpClient) { }


  onFileSelected(event: any): void {
    this.selectedFile = event.target.files[0];
  }

  onUpload(): void {
    let formData = new FormData();
    formData.set("name", this.selectedFile.name);
    formData.set("file", this.selectedFile);

    this.http.post('http://localhost:3001/upload/uploadfiles', formData)
      .subscribe((response) => {
        console.log('Upload successful', response);
      }, error => {
        console.error('Upload error', error);
      });
  }
}
