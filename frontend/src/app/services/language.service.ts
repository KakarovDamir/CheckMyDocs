import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LanguageService {
  private selectedLanguageSubject: BehaviorSubject<string> = new BehaviorSubject<string>('rus');

  getSelectedLanguage(): Observable<string> {
    return this.selectedLanguageSubject.asObservable();
  }

  setLanguage(language: string): void {
    this.selectedLanguageSubject.next(language);
  }
}
