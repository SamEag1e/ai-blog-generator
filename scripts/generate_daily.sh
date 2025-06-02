KEYWORD="wireless earbuds"
ENDPOINT="http://localhost:5000/generate?keyword=$(echo $KEYWORD | jq -sRr @uri)"

curl "$ENDPOINT" -o "generated_$(date +%F).json"
