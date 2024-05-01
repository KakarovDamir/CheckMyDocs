import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AppComponent } from '../app.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LanguageService } from '../services/language.service';

@Component({
    selector: 'app-home',
    standalone: true,
    imports: [RouterModule, AppComponent, CommonModule, FormsModule],
    templateUrl: './home.component.html',
    styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  selectedLanguage: string = 'rus';

  constructor(private languageService: LanguageService) {}

  ngOnInit(): void {
    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
    });
  }
}
