import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Recipe } from 'src/app/models/recipe.model';
import { Router, ActivatedRoute } from '@angular/router';
import { take } from 'rxjs/operators';
import { RecipeService } from 'src/app/services/recipe.service';
import { MatDialog } from '@angular/material/dialog';
import { RecipeFormComponent } from 'src/app/components/recipe-form/recipe-form.component';
import { DeleteDialogComponent } from 'src/app/components/delete-dialog/delete-dialog.component';
import { FormGroup } from '@angular/forms';

@Component({
    selector: 'app-recipe-detail',
    templateUrl: './recipe-detail.component.html',
    styleUrls: ['./recipe-detail.component.css']
})
export class RecipeDetailComponent implements OnInit {

    recipeDetail$: Observable<Recipe>;

    constructor(
        route: ActivatedRoute,
        private router: Router,
        private dialog: MatDialog,
        
        private recipeService: RecipeService) {
        route.params.pipe(take(1))
        .subscribe(params => this.recipeDetail$ = recipeService.getRecipe$(params.recipeID));
    }

    onRecipeDelete(recipeID) {
        const dialogRef = this.dialog.open(DeleteDialogComponent);

        dialogRef.afterClosed().subscribe(doDelete => {
            if (doDelete) {
                this.recipeService.deleteRecipe$(recipeID).subscribe(isDelete => {
                    if (isDelete) {
                        this.router.navigate(['/recipe']);
                    }
                });
            }
        });
    }

    onRecipeEdit(recipe: Recipe) {
        const dialogRef = this.dialog.open(RecipeFormComponent, { data: { recipe }});

        dialogRef.afterClosed().subscribe(result => {
            this.recipeService.updateRecipe$(recipe.getData('recipeID'), result)
            .subscribe(isUpdate => {
                if (isUpdate) {
                    this.recipeDetail$ = this.recipeService.getRecipe$(recipe.getData('recipeID'));
                }
            });
        });
    }

    ngOnInit(): void {
    }

}
