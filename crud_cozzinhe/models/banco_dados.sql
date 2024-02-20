drop database if exists cozzinhe;
CREATE DATABASE cozzinhe;
USE cozzinhe;

CREATE TABLE Recipes (
    id_recipes INT PRIMARY KEY,         -- Chave primária para identificar exclusivamente cada receita
    nome VARCHAR(255),                  -- Nome da receita
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
CREATE TABLE cozzinhe_import (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    ingredients TEXT,
    n_ingredients INT
);
-- Trigger para evitar ingredientes duplicados
CREATE TRIGGER evitar_ingredientes_duplicados 
BEFORE INSERT ON recipeingredients 
FOR EACH ROW
BEGIN
    DECLARE ingredient_count INT;
    SET ingredient_count = (SELECT COUNT(*) FROM recipeingredients WHERE recipe_id = NEW.recipe_id AND ingredient_id = NEW.ingredient_id);
    IF ingredient_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Não é permitido adicionar um ingrediente duplicado na mesma receita.';
    END IF;
END;

-- Trigger para evitar receitas duplicadas
CREATE TRIGGER evitar_receitas_duplicadas 
BEFORE INSERT ON recipes 
FOR EACH ROW
BEGIN
    DECLARE recipe_count INT;
    SET recipe_count = (SELECT COUNT(*) FROM recipes WHERE nome = NEW.nome);
    IF recipe_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Não é permitido adicionar uma receita com o mesmo nome.';
    END IF;
END;

