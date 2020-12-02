## Shut down all services, keep network
docker-compose down

# Kill containers of people who logged out without stopping their servers
docker kill $(docker ps -q)

## Tidy up everything
docker system prune --all

# NOT for the actual exam
if [ "$1" = "--volumes" ]; then
  echo 'Delete all volumes...'
  docker volume prune 
else
  echo 'Skip volumes'
fi;
