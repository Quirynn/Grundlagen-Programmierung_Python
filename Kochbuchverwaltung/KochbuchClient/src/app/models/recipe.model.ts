import { Ingredient } from './ingredient.model';

export class Recipe {
    private recipeID: number;
    private title: string;
    private prepareTimeMinutes: number;
    private prepareInstructions: string;
    private ingredients: Array<Ingredient>;

    constructor(data?: any) {
        this.recipeID = data?.recipeID || 0;
        this.title = data?.title || '';
        this.prepareTimeMinutes = data?.prepareTimeMinutes || 0;
        this.prepareInstructions = data?.prepareInstructions || '';
        this.ingredients = new Array<Ingredient>();
        if (!!data?.ingredients) {
            data.ingredients.forEach(ingredient => this.ingredients.push(new Ingredient(ingredient)));
        }
    }

    public getData(key: 'recipeID' | 'title' | 'prepareTimeMinutes' | 'prepareInstructions' | 'ingredients'): any {
        return this[key];
    }

    public getCaloriesSum(): number {
        if (this.ingredients.length > 0) {
            return this.ingredients
            .map(ingredient => ingredient.getData('calories'))
            .reduce((aCalories, bCalories) => aCalories + bCalories);
        }
        return 0;
    }
}