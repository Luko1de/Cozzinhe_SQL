drop database if exists cozzinhe;
CREATE DATABASE cozzinhe;
USE cozzinhe;

CREATE TABLE Recipes (
    id_recipes INT PRIMARY KEY,         -- Chave primária para identificar exclusivamente cada receita
    nome VARCHAR(255),                  -- Nome da receita
    tags VARCHAR(10000),                  -- Tags associadas à receita
    descricao TEXT,                     -- Descrição da receita
    quantity INT              -- Quantidade do ingrediente necessário para a receita
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
    FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe) ON DELETE CASCADE,-- Restrição de chave estrangeira para garantir a integridade referencial
    FOREIGN KEY (id_ingredients) REFERENCES Ingredients(id_ingredients) ON DELETE CASCADE-- Restrição de chave estrangeira para garantir a integridade referencial
);

CREATE TABLE cozzinhe_import (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    ingredients TEXT,
    n_ingredients INT
);

-- Triggers
DELIMITER //

CREATE TRIGGER atualizar_quantidade_ingredientes
AFTER INSERT ON RecipeIngredients
FOR EACH ROW
BEGIN
    -- Atualiza a quantidade de ingredientes na receita após adicionar um novo ingrediente
    UPDATE Recipes 
    SET quantity = quantity + 1 
    WHERE id_recipes = NEW.id_recipes;
END;
//

CREATE TRIGGER diminuir_quantidade_ingredientes
AFTER DELETE ON RecipeIngredients
FOR EACH ROW
BEGIN
    -- Atualiza a quantidade de ingredientes na receita após remover um ingrediente
    UPDATE Recipes 
    SET quantity = quantity - 1 
    WHERE id_recipes = OLD.id_recipes;
END;
//

DELIMITER ;
