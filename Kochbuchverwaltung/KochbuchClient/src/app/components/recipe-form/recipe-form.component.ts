import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Ingredient } from 'src/app/models/ingredient.model';

@Component({
    selector: 'app-recipe-form',
    templateUrl: './recipe-form.component.html',
    styleUrls: ['./recipe-form.component.css']
})
export class RecipeFormComponent implements OnInit {
    isEdit: boolean;

    recipeForm: FormGroup;
    ingredientForms: Array<FormGroup>;

    constructor(
        public dialogRef: MatDialogRef<RecipeFormComponent>,
        @Inject(MAT_DIALOG_DATA) public data: any,
        private fb: FormBuilder) {

        this.isEdit = !!data?.recipe;
        this.recipeForm = fb.group({
            title: [data?.recipe.getData('title') || '', Validators.required],
            prepareTimeMinutes: [data?.recipe.getData('prepareTimeMinutes') || 0, Validators.required],
            prepareInstructions: [data?.recipe.getData('prepareInstructions') || '', Validators.required]
        });

        this.ingredientForms = new Array<FormGroup>();

        if (this.isEdit) {
            data.recipe.getData('ingredients').forEach(ingredient => {
                this.ingredientForms.push(fb.group({
                    title: [ingredient.getData('title'), Validators.required],
                    amount: [ingredient.getData('amount'), Validators.required],
                    amountUnit: [ingredient.getData('amountUnit'), Validators.required],
                    calories: [ingredient.getData('calories'), Validators.required]
                }));
            });
        }
        this.addEmptyIngredient();
    }

    isAllIngredientsValid(): boolean {
        // Prüft, ob alle im Formular angegebenen Zutaten vollständig sind
        for (const ingredientForm of this.ingredientForms) {
            if (!ingredientForm.valid) {
                return false;
            }
        }
        return true;
    }

    addEmptyIngredient() {
        // Fügt ein neues Formularfeld für die Zutaten hinzu
        this.ingredientForms.push(this.fb.group({
            title: ['', Validators.required],
            amount: [0, Validators.required],
            amountUnit: ['', Validators.required],
            calories: [0, Validators.required]
        }));
    }

    onIngredientAdd() {
        if (this.isAllIngredientsValid()) {
            this.addEmptyIngredient();
        }
    }

    onSubmitSave() {
        if (this.recipeForm.valid) {
            const ingredients = new Array<any>();
            this.ingredientForms.forEach(ingredientForm => {
                if (ingredientForm.valid) {
                    ingredients.push(ingredientForm.value)
                }
            });
            return { recipeDetail: this.recipeForm.value, ingredients };
        }
        return false;
    }

    ngOnInit(): void {
    }

}
