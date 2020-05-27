import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RecipeOverviewComponent } from './views/recipe-overview/recipe-overview.component';
import { RecipeDetailComponent } from './views/recipe-detail/recipe-detail.component';
import { RouterModule, Routes } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavigationComponent } from './components/navigation/navigation.component';
import { RecipeListComponent } from './components/recipe-list/recipe-list.component';

import { HttpClientModule } from '@angular/common/http';

// Angular Material
import { MatInputModule } from '@angular/material/input';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { MatRippleModule } from '@angular/material/core';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';
import { RecipeFormComponent } from './components/recipe-form/recipe-form.component';
import { DeleteDialogComponent } from './components/delete-dialog/delete-dialog.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatStepperModule } from '@angular/material/stepper'; 
import { MatFormFieldModule } from '@angular/material/form-field';



// BASIC ROUTING
const routes: Routes = [
    { path: '', redirectTo: 'recipe', pathMatch: 'full' },
    { path: 'recipe', component: RecipeOverviewComponent },
    { path: 'recipe/:recipeID/detail', component: RecipeDetailComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    RecipeOverviewComponent,
    RecipeDetailComponent,
    NavigationComponent,
    RecipeListComponent,
    RecipeFormComponent,
    DeleteDialogComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routes),
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatToolbarModule,
    MatButtonModule,
    MatCardModule,
    MatTableModule,
    MatRippleModule,
    MatIconModule,
    MatTooltipModule,
    MatDialogModule,
    MatStepperModule,
    MatFormFieldModule,
    MatInputModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
