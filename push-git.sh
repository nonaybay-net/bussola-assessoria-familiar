msg="$1"

git add .
git commit -m "$msg ~ $(date)"
git push
