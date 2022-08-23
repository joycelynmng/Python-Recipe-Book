class Recipes:
    def __init__(self): # holds recipe object to push into array
        self.name = input("What is the name of the item you want to add? ")
        self.ingredients = recipeBook.ingredientsArray()
        self.time = int(input("How many minutes will it take to make this? "))

    # asks you to add ingredients - child of Recipes Class
    def ingredientsArray(self): 
        try:
            numberOfIngredients = int(input("Enter the number of ingredients: ")) # first ask for the number of ingredients
            arrayOfIngredients = list(map(str,input("Enter the ingredients: ").strip().split())) [:numberOfIngredients]
            # make the array by creating map that takes the number of inputs and then splits it into indexes
        except ValueError:
            print("You must enter a number")
            return recipeBook.ingredientsArray() # return so will not print None for ingredients
            # use recurssion to call the function again so code does not break
        else:
            return arrayOfIngredients

    # tells you what recipe you added - child of inputRecipe()
    def returnRecipe(self): #tells you what you added
        print(f"This recipe is for {self.name}")
        print(f"Add {self.ingredients}")
        print(f"It will take {self.time} minutes to make")
        print("\n")


class RecipeBook(Recipes):
    # holds recipe book
    def __init__(self):
        self.__recipeBook = []

    # main add recipe to recipe book function
    def addRecipe(self, recipeAdd):
        self.__recipeBook.append(recipeAdd)

    # main delete recipe function # logic error with removing last index
    def deleteRecipe(self, deleteFood):
        for i in range(len(self.__recipeBook)):
            if self.__recipeBook[i].name == deleteFood:
                self.__recipeBook.remove(recipeBook.__recipeBook[i])
                print(f"{deleteFood} has been removed\n")
                return
            else:
                print(f"{deleteFood} does not exist\n")
                return

    # main modify function

    # prints recipeBook in beginning
    def displayRecipes(self):
        for i in range(0, len(self.__recipeBook)):
            print(self.__recipeBook[i].name)
        
    # main search recipe function
    def searchRecipe(self, search):
        for i in range(len(self.__recipeBook)):
            if self.__recipeBook[i].name == search:
                print("\n")
                Recipes.returnRecipe(recipeBook.__recipeBook[i])
                return
            else:
                print("Does not exist\n")
                return
        

# main "home page" section
options = {
    1 : "add",
    2: "delete",
    3: "modify",
    4: "search",
    5: "exit"
}

recipeBook = RecipeBook()
while True: # asks user if they want to add anything new
    print("Please choose an option:")
    print(options)
    print("\nHere are the current recipes:")
    recipeBook.displayRecipes()
    answerChoice = input("Enter an option: ")
    if answerChoice == "1":
        newRecipe = Recipes()
        recipeBook.addRecipe(newRecipe)
        print("\n")
        newRecipe.returnRecipe()
    elif answerChoice == "2":
        deleteFood = str(input("Which recipe you want to delete? "))
        recipeBook.deleteRecipe(deleteFood)
    elif answerChoice == "3":
        modFood = input("Which would you like to modify? name, ingredients, or time: ")
        recipeBook.___(modFood)
    elif answerChoice == "4":
        searchFood = str(input("Enter the the recipe you want to search? "))
        recipeBook.searchRecipe(searchFood)
    elif answerChoice == "5":
        break
    else:
        print("You have to choose an option from 1 - 5")

print("Here are the current recipes in your recipe book: ")
recipeBook.displayRecipes()