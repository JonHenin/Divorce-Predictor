#powershell script
$ADDRESS='gcr.io'
$PROJECT_ID='docker-project-jhenin-1'
$REPOSITORY='divorce'
$VERSION='v0.06'

docker build -t ${REPOSITORY}:$VERSION .
$ID = (docker images ${REPOSITORY}:$VERSION --format "{{.ID}}" | Out-String).Trim()

docker tag $ID $ADDRESS/$PROJECT_ID/${REPOSITORY}:$VERSION

docker push $ADDRESS/$PROJECT_ID/${REPOSITORY}:$VERSION