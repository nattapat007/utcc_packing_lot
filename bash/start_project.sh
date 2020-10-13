echo "==============================="
echo "||      Start Project!!!!    ||"
echo "==============================="

echo "1. Start postgres"
docker-compose up -d postgres
sleep 10

echo "2. Start django"
docker-compose up -d django
sleep 10

echo "# show logs"
docker-compose logs -f

#$SHELL