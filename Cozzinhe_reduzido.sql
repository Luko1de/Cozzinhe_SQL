CREATE TABLE Recipes (
    id_recipes INT PRIMARY KEY,         -- Chave primária para identificar exclusivamente cada receita
    nome VARCHAR(255),                  -- Nome da receita
    tags VARCHAR(2000),                  -- Tags associadas à receita
    descricao TEXT,                     -- Descrição da receita
    quantity VARCHAR(50)                -- Quantidade do ingrediente necessário para a receita
);
-- Tabela para armazenar os ingredientes
CREATE TABLE Ingredients (
    id_ingredients INT PRIMARY KEY,     -- Chave primária para identificar exclusivamente cada ingrediente
    nome VARCHAR(255)                   -- Nome do ingrediente
);
-- Tabela para armazenar os ingredientes de cada receita
CREATE TABLE RecipeIngredients (
    id_recipeingredients INT PRIMARY KEY,-- Chave primária para identificar exclusivamente cada entrada de ingrediente da receita
    id_recipes INT,                      -- Chave estrangeira referenciando a tabela de Recipes, indicando a qual receita o ingrediente pertence
    id_ingredients INT,                  -- Chave estrangeira referenciando a tabela de Ingredients, indicando qual ingrediente está sendo usado
    FOREIGN KEY (id_recipes) REFERENCES Recipes(id_recipes),-- Restrição de chave estrangeira para garantir a integridade referencial
    FOREIGN KEY (id_ingredients) REFERENCES Ingredients(id_ingredients)-- Restrição de chave estrangeira para garantir a integridade referencial
);
CREATE TABLE Nutrition (
    id_nutrition INT PRIMARY KEY,       -- Chave primária para identificar exclusivamente cada entrada de dados nutricionais
    id_recipes INT,                     -- Chave estrangeira referenciando a tabela de Recipes, indicando a qual receita os dados nutricionais pertencem
    carbohydrates FLOAT,                -- Quantidade de carboidratos na receita
    fats FLOAT,                         -- Quantidade de gorduras na receita
    proteins FLOAT,                     -- Quantidade de proteínas na receita
    calories INT,                       -- Número de calorias na receita
    FOREIGN KEY (id_recipes) REFERENCES Recipes(id_recipes)  -- Restrição de chave estrangeira para garantir a integridade referencial
);
CREATE TABLE cozzinhe_import (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    tags VARCHAR(2000),
    nutrition VARCHAR(255),
    ingredients TEXT,
    n_ingredients INT
);

