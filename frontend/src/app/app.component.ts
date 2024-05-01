import { Component } from '@angular/core';
import { Router, RouterModule, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './home/home.component';
import { FaqsComponent } from './faqs/faqs.component';
import { FormsModule } from '@angular/forms';
import { LanguageService } from './services/language.service';
import { LoginComponent } from './login/login.component';



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule, CommonModule, HomeComponent,FaqsComponent, FormsModule, LoginComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  selectedLanguage: string = 'rus';

  constructor(private languageService: LanguageService) {}

  ngOnInit(): void {
    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
    });
  }

  onLanguageChange(language: string): void {
    this.languageService.setLanguage(language);
  }


  

}
