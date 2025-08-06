# Ferme IA Ultra - Agent

## Déploiement sur Render

1. Ajouter votre token Telegram dans les secrets Render sous `TELEGRAM_TOKEN`.
2. Déployer ce dépôt sur Render en branch `main`.
3. Render installera automatiquement les dépendances et lancera le service.
4. Le service écoute sur le port 10000 et répond aux messages Telegram.
5. Pour tester, envoyez un message à votre bot Telegram et il vous répondra.

## Structure

- agent.py : application Flask + Telegram bot
- requirements.txt : dépendances Python
- render.yaml : configuration Render (python 3.10)