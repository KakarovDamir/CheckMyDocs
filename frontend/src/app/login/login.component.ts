import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { LanguageService } from '../services/language.service';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, HttpClientModule, RouterModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})


export class LoginComponent {

  loginObj: any = {
    Email: '',
    Password: ''
  };

  signupUsers: any[] = [];

  constructor(private router: Router, private languageService: LanguageService) {}

  ngOnInit(): void {
    const localData = localStorage.getItem('signupUsers');
    if (localData) {
      this.signupUsers = JSON.parse(localData);
    }

    this.languageService.getSelectedLanguage().subscribe(language => {
      this.selectedLanguage = language;
    });
  }

  onLogin() {
    const isUserExist = this.signupUsers.find(user => user.Email === this.loginObj.Email && user.Password === this.loginObj.Password);
    if (isUserExist) {
      alert('Login successful');
      this.router.navigate(['/home']);
    } else {
      alert('Invalid credentials');
    }
  }

  selectedLanguage: string = 'rus';
}