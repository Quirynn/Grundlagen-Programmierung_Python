
export class Ingredient {
    private title: string;
    private amount: number;
    private amountUnit: string;
    private calories: number;

    constructor(data?: any) {
        this.title = data?.title || '';
        this.amount = data?.amount || 0;
        this.amountUnit = data?.amountUnit || '';
        this.calories = data?.calories || 0;
    }

    public getData(key: 'title' | 'amount' | 'amountUnit' | 'calories'): any {
        return this[key];
    }
}
