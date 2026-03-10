#!/bin/bash
# ship.sh - The Build -> Push -> Deploy pipeline
# Usage: ./ship.sh "Description of project"

PROJECT_NAME=$1
PROJECT_DIR=$2
PROMPT=$3

if [ -z "$PROJECT_NAME" ] || [ -z "$PROMPT" ]; then
  echo "Usage: ./ship.sh <project_name> <directory> <prompt>"
  exit 1
fi

echo "🚀 Building project: $PROJECT_NAME"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"
git init

# 1. Build via Codex (GPT-5.4)
echo "🤖 Codex is working on it..."
codex exec --model openai/gpt-5.4 --full-auto "$PROMPT"

# 2. Push to GitHub
echo "📤 Pushing to GitHub..."
git add .
git commit -m "Initial commit: $PROJECT_NAME"
git branch -M main
git remote add origin https://github.com/NicolePrince1/"$PROJECT_NAME".git
git push -u origin main

# 3. Deploy to Vercel
echo "☁️ Deploying to Vercel..."
vercel --token $VERCEL --prod --yes

echo "✅ Done! Project is live."
