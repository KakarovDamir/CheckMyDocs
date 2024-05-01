import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DocumentsComponent } from './documents/documents.component';
import { FaqsComponent } from './faqs/faqs.component';
import { LoginComponent } from './login/login.component';

export const routes: Routes = [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent},
    {path: 'documents', component: DocumentsComponent},
    {path: 'faqs', component: FaqsComponent},
    {path: 'login', component: LoginComponent},
    {path: '**', redirectTo: 'home'}
];
