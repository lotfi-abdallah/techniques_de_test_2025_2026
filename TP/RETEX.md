# Retour d'Expérience

Ce document présente mon retour d'expérience sur le projet de service de triangulation réalisé dans le cadre du TP "Techniques de Test 2025/2026".

## Ce qui a bien fonctionné

- Écrire les tests en premier m'a obligé de bien comprendre les spécifications OpenAPI avant de commencer l'implémentation.
- Une fois les tests en place, j'ai pu modifier l'implémentation avec confiance.
- L'utilisation de `pytest` a facilité la création de tests unitaires et le mock de dépendance externe (PointSetManager).

## Ce qui aurait pu être mieux fait

### Plan de tests initial

Mon plan de tests initial était incomplet, j'avais sous-estimé le nombre de cas d'erreur à gérer (404, 400, 500, 503). Alors j'ai écrit qu'un seul test pour chaque cas d'erreur, ce qui n'était pas suffisant pour une couverture complète.

### Algorithme de triangulation

J'ai implémenté un algorithme simple (fan triangulation). Pour un projet en production, il faut implémenter un algorithme plus robuste comme Delaunay.

## Ce que je ferais différemment

- Utiliser un algorithme de triangulation plus avancé.
- Mettre en place beaucoup plus de tests d'intégration.
- Générer la documentation OpenAPI Swagger automatiquement depuis le code Flask.
