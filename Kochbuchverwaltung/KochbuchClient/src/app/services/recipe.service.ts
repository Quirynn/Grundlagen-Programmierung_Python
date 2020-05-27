import { Injectable } from '@angular/core';
import { environment as env } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { Recipe } from '../models/recipe.model';
import { ThrowStmt } from '@angular/compiler';

@Injectable({
    providedIn: 'root'
})
export class RecipeService {

    constructor(private http: HttpClient) { }

    getRecipe$(recipeID): Observable<Recipe> {
        return this.http.get<{ recipeDetail }>(env.apiUrl.concat('/recipe/' + recipeID))
            .pipe(map(response => new Recipe(response.recipeDetail)));
    }

    getRecipeList$(): Observable<Array<Recipe>> {
        return this.http.get<{ recipeList: Array<any> }>(env.apiUrl.concat('/recipe'))
            .pipe(map(response => response.recipeList.map(recipe => new Recipe(recipe))));
    }

    createRecipe$(recipeData): Observable<boolean> {
        return this.http.post<{ isCreate: boolean }>(env.apiUrl.concat('/recipe'), recipeData)
        .pipe(map(response => response.isCreate));
    }

    updateRecipe$(recipeID, recipeData): Observable<boolean> {
        return this.http.put<{ isUpdate: boolean }>(env.apiUrl.concat('/recipe/' + recipeID), recipeData)
        .pipe(map(response => response.isUpdate));
    }

    deleteRecipe$(recipeID): Observable<boolean> {
        return this.http.delete<{ isDelete: boolean }>(env.apiUrl.concat('/recipe/' + recipeID))
        .pipe(map(response => response.isDelete));
    }
}
