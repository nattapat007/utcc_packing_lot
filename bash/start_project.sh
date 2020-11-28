echo "==============================="
echo "||      Start Project!!!!    ||"
echo "==============================="
echo "1. Start postgres"
docker-compose up -d postgres
sleep 12
echo "2. Start django"
docker-compose up -d django
sleep 10
docker-compose exec django sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py init_data && python manage.py runserver 0.0.0.0:8000'
echo "# show logs"
docker-compose logs -f