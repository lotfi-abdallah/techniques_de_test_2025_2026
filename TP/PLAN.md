# Plan de Test

Ce document détaille la stratégie de test pour le micro-service `Triangulator`. L'objectif est de garantir la qualité, la robustesse et la performance de l'application à travers plusieurs niveaux de tests.

## 1. Tests Unitaires (TU)

Les tests unitaires visent à valider la logique métier principale de l'application de manière isolée, en particulier l'algorithme de triangulation et les fonctions de sérialisation.

### 1.1. Logique de Triangulation

- **TU 1.1.1 : Cas Nominal**

  - **Description :** Valider l'algorithme avec des ensembles de points simples et valides.
  - **Exemples :**
    - Un ensemble de 3 points (doit retourner un seul triangle).
    - Un ensemble de 4 points formant un carré (doit retourner deux triangles).
    - Un polygone convexe avec N points.
  - **Résultat Attendu :** Une liste de triangles correcte qui couvre l'ensemble des points.

- **TU 1.1.2 : Cas Limites et Particuliers**
  - **Description :** Tester le comportement de l'algorithme avec des données d'entrée problématiques ou inhabituelles.
  - **Exemples :**
    - Moins de 3 points (0, 1, ou 2 points).
    - Points colinéaires (tous les points sur une même ligne).
    - Points coïncidents (plusieurs points aux mêmes coordonnées).
  - **Résultat Attendu :**
    - Pour moins de 3 points ou des points colinéaires, le service doit retourner une liste de triangles vide.
    - Le comportement pour les points coïncidents doit être défini (par exemple, les doublons sont ignorés).

### 1.2. Sérialisation des Données

- **TU 1.2.1 : Validation du Format de Sortie**
  - **Description :** S'assurer que la structure de données `Triangles` est correctement encodée au format binaire spécifié dans `triangulator.yml`.
  - **Données d'Entrée :** Une liste de triangles générée.
  - **Résultat Attendu :** Un flux binaire (`bytes`) qui correspond exactement à la spécification (nombre de triangles suivi des coordonnées des sommets).

## 2. Tests d'API et de Comportement (TA)

Ces tests valident que le service se comporte comme attendu du point de vue d'un client HTTP, y compris ses interactions avec le service externe `PointSetManager`. Pour cela, nous utiliserons un "mock" de ce service.

- **TA 2.1 : Point de Terminaison `POST /triangulate` - Cas Nominal**

  - **Description :** Simuler un appel réussi à l'API où tout fonctionne comme prévu.
  - **Scénario :**
    1. Le client envoie une requête `POST /triangulate` avec un `pointSetId` valide.
    2. Le `Triangulator` appelle le `PointSetManager` (mock).
    3. Le mock retourne un ensemble de points valide (HTTP 200).
    4. Le `Triangulator` effectue la triangulation et retourne une réponse.
  - **Résultat Attendu :** Une réponse HTTP 200 avec `Content-Type: application/octet-stream` et un corps de réponse binaire non vide.

- **TA 2.2 : Gestion des Erreurs du `PointSetManager`**

  - **Description :** Vérifier que le `Triangulator` gère correctement les erreurs provenant du `PointSetManager`.
  - **Scénarios :**
    - Le `PointSetManager` (mock) retourne une erreur 404 (`pointSetId` non trouvé).
    - Le `PointSetManager` (mock) retourne une erreur 500 (panne serveur).
  - **Résultat Attendu :** Le `Triangulator` doit propager l'erreur en retournant le même code de statut HTTP (404 ou 500) au client.

- **TA 2.3 : Gestion des Requêtes Client Invalides**
  - **Description :** Tester la validation des données d'entrée fournies par le client.
  - **Scénarios :**
    - Requête avec un corps JSON malformé.
    - Requête où le champ `pointSetId` est manquant ou a un type incorrect.
  - **Résultat Attendu :** Le service doit retourner une erreur HTTP 400 (Bad Request) avec un message explicite.

## 3. Tests de Performance (TP)

Ces tests visent à mesurer et valider les performances de l'algorithme de triangulation et de la sérialisation pour des ensembles de données de grande taille.

- **TP 3.1 : Performance de la Triangulation**

  - **Description :** Mesurer le temps d'exécution de l'algorithme de triangulation pour un grand nombre de points.
  - **Scénario :** Exécuter la fonction de triangulation sur des ensembles de 1 000, 10 000, et 50 000 points.
  - **Résultat Attendu :** Le temps d'exécution doit rester dans des limites raisonnables (par exemple, moins de quelques secondes) et ne doit pas augmenter de manière exponentielle.

- **TP 3.2 : Performance de la Sérialisation**
  - **Description :** Mesurer le temps nécessaire pour encoder la structure `Triangles` en format binaire.
  - **Scénario :** Sérialiser des listes de triangles de grande taille.
  - **Résultat Attendu :** La sérialisation doit être très rapide, avec un impact négligeable sur le temps de réponse global.
