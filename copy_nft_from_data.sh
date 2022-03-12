rm -R ./public/entree
mkdir ./public/entree/

cp -r ./data/results ./public/entree/
mv ./public/entree/results ./public/entree/image

cp -r ./data/results_json ./public/entree/
mv ./public/entree/results_json ./public/entree/json