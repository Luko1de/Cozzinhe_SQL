-- Tabela para armazenar as receitas
CREATE TABLE Recipes (
    id_recipes INT PRIMARY KEY,         -- Chave primária para identificar exclusivamente cada receita
    nome VARCHAR(255),                  -- Nome da receita
    tags VARCHAR(2000),                  -- Tags associadas à receita
    nutrition VARCHAR(255),             -- Informações nutricionais da receita
    n_steps INT,                        -- Número de passos na receita
    descricao TEXT                    -- Descrição da receita
);

-- Tabela para armazenar os dados nutricionais das receitas
CREATE TABLE Nutrition (
    id_nutrition INT PRIMARY KEY,       -- Chave primária para identificar exclusivamente cada entrada de dados nutricionais
    id_recipes INT,                     -- Chave estrangeira referenciando a tabela de Recipes, indicando a qual receita os dados nutricionais pertencem
    carbohydrates FLOAT,                -- Quantidade de carboidratos na receita
    fats FLOAT,                         -- Quantidade de gorduras na receita
    proteins FLOAT,                     -- Quantidade de proteínas na receita
    calories INT,                       -- Número de calorias na receita
    FOREIGN KEY (id_recipes) REFERENCES Recipes(id_recipes)  -- Restrição de chave estrangeira para garantir a integridade referencial
);

-- Tabela para armazenar os ingredientes
CREATE TABLE Ingredients (
    id_ingredients INT PRIMARY KEY,     -- Chave primária para identificar exclusivamente cada ingrediente
    nome VARCHAR(255)                   -- Nome do ingrediente
);

-- Tabela para armazenar os passos da receita
CREATE TABLE RecipeSteps (
    id_recipe_steps INT PRIMARY KEY,     -- Chave primária para identificar exclusivamente cada passo da receita
    id_recipes INT,                      -- Chave estrangeira referenciando a tabela de Recipes, indicando a qual receita o passo pertence
    step_number INT,                     -- Número do passo na sequência da receita
    step_description TEXT,               -- Descrição do passo
    FOREIGN KEY (id_recipes) REFERENCES Recipes(id_recipes)  -- Restrição de chave estrangeira para garantir a integridade referencial
);

-- Tabela para armazenar os ingredientes de cada receita
CREATE TABLE RecipeIngredients (
    id_recipeingredients INT PRIMARY KEY,-- Chave primária para identificar exclusivamente cada entrada de ingrediente da receita
    id_recipes INT,                      -- Chave estrangeira referenciando a tabela de Recipes, indicando a qual receita o ingrediente pertence
    id_ingredients INT,                  -- Chave estrangeira referenciando a tabela de Ingredients, indicando qual ingrediente está sendo usado
    FOREIGN KEY (id_recipes) REFERENCES Recipes(id_recipes),-- Restrição de chave estrangeira para garantir a integridade referencial
    FOREIGN KEY (id_ingredients) REFERENCES Ingredients(id_ingredients)-- Restrição de chave estrangeira para garantir a integridade referencial
);

