#!/bin/bash
# Synkroniserer lokal kopi med GitHub-repoet.
# Forkaster lokale endringer som kun er metadata (f.eks. pptx åpnet i PowerPoint),
# og henter siste versjon fra remote.

set -euo pipefail

cd "$(dirname "$0")"

BRANCH=$(git branch --show-current)
echo "Branch: $BRANCH"

# Hent siste fra remote
git fetch origin "$BRANCH"

# Sjekk om det finnes lokale endringer
if git diff --quiet && git diff --cached --quiet; then
    echo "Ingen lokale endringer."
else
    echo ""
    echo "Lokale endringer funnet:"
    git status --short
    echo ""

    # Sjekk om endringene kun er i binærfiler (metadata-endringer)
    CHANGED_FILES=$(git diff --name-only)
    ALL_BINARY=true
    for f in $CHANGED_FILES; do
        if git diff --numstat -- "$f" | grep -q "^-"; then
            # Binærfil (numstat viser "-" for binære filer)
            true
        elif git diff --numstat -- "$f" | awk '{print $1}' | grep -q "^0$"; then
            # Ingen tekstendringer — sannsynligvis metadata
            true
        else
            ALL_BINARY=false
            break
        fi
    done

    if [ "$ALL_BINARY" = true ]; then
        echo "Endringene ser ut til å kun være metadata/binærfiler."
        echo "Forkaster lokale endringer..."
        git checkout -- .
    else
        echo "Det finnes tekstendringer som kan være viktige."
        echo ""
        echo "Vil du forkaste disse og synkronisere med remote? (j/n)"
        read -r svar
        if [ "$svar" = "j" ] || [ "$svar" = "J" ]; then
            git checkout -- .
            echo "Lokale endringer forkastet."
        else
            echo "Avbryter. Commit eller stash endringene dine først."
            exit 1
        fi
    fi
fi

# Sjekk om det finnes nye commits å hente
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse "origin/$BRANCH")

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "Allerede oppdatert."
else
    AHEAD=$(git log --oneline "origin/$BRANCH..HEAD" | wc -l | tr -d ' ')
    BEHIND=$(git log --oneline "HEAD..origin/$BRANCH" | wc -l | tr -d ' ')

    if [ "$AHEAD" -gt 0 ]; then
        echo "Du har $AHEAD lokale commits som ikke er pushet."
        echo "Kjører rebase..."
    fi

    if [ "$BEHIND" -gt 0 ]; then
        echo "Henter $BEHIND nye commits fra remote..."
    fi

    git pull --rebase
    echo "Synkronisering fullført."
fi
