echo "# Start clean image"
docker image prune -f
docker system prune -a -f