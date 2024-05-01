import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DocumentComponent } from './document/document.component';
import { FaqsComponent } from './faqs/faqs.component';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent},
    {path: 'document', component: DocumentComponent},
    {path: 'faqs', component: FaqsComponent},
    {path: 'login', component: LoginComponent},
    {path: '**', redirectTo: 'home'}
];
