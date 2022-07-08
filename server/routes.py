# API

# auth API, starts with '/auth'
AUTHORIZE = '/authorize'
VERIFY = '/verify'
REFRESH_ALL = '/refresh_all'
AUTHORIZE_EAST_WEST = '/authorize_east_west'
CHOOSE_EAST_OR_WEST = '/choose_east_or_west'
REFRESH_ALL_EAST_WEST = '/refresh_all_east_west'

# team API, starts with '/team'
LIST_ALL_TEAM = '/list_all_team'
UPDATE_ALL_TEAM_MILEAGE = '/update_all_team_mileage'
GET_ALL_EAST_WEST_MILEAGE = '/get_all_east_west_mileage'
ADD_ALL_TEAM_RANKINGS = '/add_all_team_rankings'
GET_TEAM_RANKINGS = '/get_team_rankings'
UPDATE_TEAM_RANKINGS = '/update_team_rankings'

# individual API, starts with '/individual'
LIST_ALL_INDIVIDUAL = '/list_all_individual'
GET_HALL_OF_FAME = '/get_hall_of_fame'
ADD_ALL_USER_RANKINGS = '/add_all_user_rankings'
GET_USER_RANKINGS = '/get_user_rankings'
UPDATE_USER_RANKINGS = '/update_user_rankings'
UPDATE_INDIVIDUAL_TOTAL_MILEAGE = '/update_individual_total_mileage'

# URL
OAUTH_URL = "https://www.strava.com/oauth/token"
ACTIVITIES_URL = "https://www.strava.com/api/v3/athlete/activities"