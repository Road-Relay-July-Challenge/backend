# RRJC X Strava Web App API documentation

<img width="100%" alt="image" src="https://user-images.githubusercontent.com/60415251/181936592-b9c338b7-75c5-4479-a781-bcb75dc21f1c.png">


# Admin APIs

**Refresh All**
----
  Refreshes all details for all individuals and teams.

* **URL**

  /admin/refresh_all

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully refreshed all teams' mileage",
        "result": {
            "1": 7
        },
        "success": true
    }`

**Add all users into achievements collection**
----
  Adds all current users into Achievements collection.

* **URL**

  /admin/add_all_users_into_achievements_collection

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully added all users into achievements collection.",
        "result": null,
        "success": true
    }`

**Refresh all east west**
----
  Refreshes all details for all individuals and for east west

* **URL**

  /admin/refresh_all_east_west

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully refreshed all for east and west.",
        "result": null,
        "success": true
    }`

**Add individual weekly special mileage**
----
  Adds special mileage of athlete of that week, in km.

* **URL**

  /admin/add_individual_weekly_special_mileage

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  `athlete_id=[integer]` `week=[integer]` `mileage=[integer]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully updated special mileage for 73815270 to 14000 cm.",
        "result": null,
        "success": true
    }`

# Authentication APIs

**Authorize**
----
  Authorizes our application to retireve from Strava.
  Triggers the OAuth UI from Strava.

* **URL**

  /auth/authorize

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

  * `Redirects Strava OAuth UI to client`

**Verify**
----
  Authorizes our application to retrieve from Strava.
  Triggers the OAuth UI from Strava.

* **URL**

  /auth/authorize

* **Method:**

  `GET`
  
* **URL Params**

  `code=[string]`

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully added Jason Ng",
        "result": [
            {
                "access_token": "<DUMMY_TOKEN>",
                "access_token_expired_at": 1656848998,
                "athlete_id": 68227634,
                "multiplier": 1,
                "name": "Jason Ng",
                "refresh_token": "<DUMMY_TOKEN>",
                "team_number": 0,
                "total_contributed_mileage": 0,
                "total_true_mileage": 0
            },
            {
                "athlete_id": <DUMMY_ID>,
                "contributed_mileage": 0,
                "special_mileage": 0,
                "true_mileage": 0,
                "week": 29
            }
        ],
        "success": true
    }`

* **Notes:**

  This is a GET request and not POST since Strava API passes the parameter code in the URL.

**Authorize east west**
----
  Authorizes our application to retrieve from Strava, for east west event.
  Triggers the OAuth UI from Strava.

* **URL**

  /auth/refresh_all_east_west

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

  * `Redirects Strava OAuth UI to client`

**Choose east or west**
----
  Verifies the user account with authorization code returned by Strava OAuth API, and the side the user chose for the event.

* **URL**

  /auth/choose_east_or_west

* **Method:**

  `GET`
  
* **URL Params**

  `code=[string]` `chosen_side=[string]`

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully added your chosen side, the great EAST",
        "result": null,
        "success": true
    }`

* **Notes:**

  This is a GET request and not POST since Strava API passes the parameter code in the URL.

# Individual APIs

**List all individual**
----
  List all individuals and their data.

* **URL**

  /individual/list_all_individual

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all individuals.",
        "result": [
            {
                "athlete_id": 123,
                "multiplier": 1,
                "name": "test",
                "team_number": 0,
                "total_contributed_mileage": 0,
                "total_true_mileage": 0
            },
            {
                "athlete_id": <DUMMY_ID>,
                "multiplier": 1,
                "name": "Jason Ng",
                "team_number": 0,
                "total_contributed_mileage": 0,
                "total_true_mileage": 0
            }
        ],
        "success": true
    }`

**Get hall of fame**
----
  Lists top 5 individuals for the following categories: Longest run, Furthest run, Highest contributed mileage, Highest true mileage

* **URL**

  /individual/get_hall_of_fame

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{        
        "message": "Successfully retrieved hall of fame.",
        "result": {
            "Highest Contributed Mileage": [
                {
                    "athlete_id": <DUMMY_ID>,
                    "data": 36.03,
                    "name": "Hao Jun Sng",
                    "team_number": 7
                },
                {
                    "athlete_id": <DUMMY_ID>,
                    "data": 35.0,
                    "name": "Nico Sim",
                    "team_number": 7
                },
            ]
        },
        "success": true
    }`

**Update individual total mileage**
----
  Updates specific athlete’s total mileage, as retrieved from Strava

* **URL**

  /individual/get_hall_of_fame

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  `athlete_id=[integer]`

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully updated <DUMMY_ID>'s total mileage.",
        "result": {
            "athlete_id": "<DUMMY_ID>",
            "mileage": {
                "total_contributed_mileage": 45.42,
                "total_true_mileage": 45.42
            }
        },
        "success": true
    }`

**Add all user rankings**
----
  Adds rankings for all participants

* **URL**

  /individual/add_all_user_rankings

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully added all rankings.",
        "result": null,
        "success": true
    }`

**Update all user rankings**
----
  Update rankings for all participants

* **URL**

  /individual/update_user_rankings

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully updated user rankings.",
        "result": [
            {
                "current_rank": 2,
                "last_refresh_rank": 1,
                "name": "Hao Jun Sng"
            },
            {
                "current_rank": 3,
                "last_refresh_rank": 2,
                "name": "Nico Sim"
            },
        ],
        "success": true
    }`

**Get user rankings**
----
  Get all user rankings

* **URL**

  /individual/get_user_rankings

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all user rankings.",
        "result": [
            {
                "athlete_id": <DUMMY_ID>,
                "current_rank": 25,
                "last_refresh_rank": 25
            },
            {
                "athlete_id": <DUMMY_ID>,
                "current_rank": 26,
                "last_refresh_rank": 26
            }
        ],
        "success": true
    }`

# Team APIs

**List all team**
----
  Lists all teams and their details, sorted in mileage order.

* **URL**

  /team/list_all_team

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all teams.",
        "result": [
            {
                "team_id": "1",
                "team_mileage": 5000
            },
            {
                "team_id": "2",
                "team_mileage": 50
            },
            {
                "team_id": "3",
                "team_mileage": 3
            }
        ],
        "success": true
    }`

**Update all team mileage**
----
  Update all team’s total true and contributed mileage, as retrieved from database.

* **URL**

  /team/update_all_team_mileage

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully updated all teams' mileage.",
        "result": {
            "1": {
                "team_contributed_mileage": 45.42,
                "team_true_mileage": 45.42
            }
        },
        "success": true
    }`

* **Notes:**

  You should call the update_individual_total_mileage first to update the DB if you have not done so.

**Get all east west mileage**
----
  Lists the east side list, west side list, and each side’s pax and mileage, sorted in mileage order.

* **URL**

  /team/get_all_east_west_mileage

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all east west mileages.",
        "result": {
            "east_side_list": [
                {
                    "athlete_id": <DUMMY_ID>,
                    "chosen_side": "east",
                    "mileage": 3.2,
                    "name": "Claire Chan"
                },
            ],
            "east_side_mileage": 3.2,
            "east_side_pax": 8,
            "west_side_list": [
                {
                    "athlete_id": <DUMMY_ID>,
                    "chosen_side": "west",
                    "mileage": 8.440000000000001,
                    "name": "yu ching ng"
                },
            ],
            "west_side_mileage": 8.440000000000001,
            "west_side_pax": 2
        },
        "success": true
    }`

**Add all team rankings**
----
  Adds rankings for all teams.

* **URL**

  /team/add_all_team_rankings

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully added all rankings.",
        "result": null,
        "success": true
    }`

**Update team rankings**
----
  Updates rankings for all teams.

* **URL**

  /team/update_team_rankings

* **Method:**

  `POST`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully updated team rankings.",
        "result": [
            {
                "current_rank": 2,
                "last_refresh_rank": 1,
                "name": 7
            },
            {
                "current_rank": 3,
                "last_refresh_rank": 2,
                "name": 5
            },
        ],
        "success": true
    }`

**Get team rankings**
----
  Get rankings for all teams.

* **URL**

  /team/get_team_rankings

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all team rankings.",
        "result": [
            {
                "athlete_id": 1,
                "current_rank": 4,
                "last_refresh_rank": 4
            },
            {
                "athlete_id": 2,
                "current_rank": 7,
                "last_refresh_rank": 7
            }
        ],
        "success": true
    }`

**List all team achievement count**
----
  Lists all teams’ and their team members’ achievement count.

* **URL**

  /team/list_all_team_achievement_count

* **Method:**

  `GET`
  
* **URL Params**

  NIL

* **Data Params**

  NIL

* **Success Response:**

    * **Code:** 200 <br />
    **Content:** `{
        "message": "Successfully retrieved all teams' achievement count.",
        "result": [
                        {
                "achievement_count_array": [
                    {
                        "Cynthia  Lau": 0
                    },
                    {
                        "Luah Jun Yang": 0
                    },
                    {
                        "Wilfred Lim": 0
                    },
                    {
                        "Hoo Fang Yu": 0
                    }
                ],
                "is_all_achieved": {
                    "number_achieved": 2,
                    "team_strength": 4
                },
                "rewarded_mileage_array": [
                    {
                        "Cynthia  Lau": 0
                    },
                    {
                        "Luah Jun Yang": 0
                    },
                    {
                        "Wilfred Lim": 0
                    },
                    {
                        "Hoo Fang Yu": 0
                    }
                ],
                "team_name": "EZ$60",
                "team_number": 3
            }
        ],
        "success": true
    }`
