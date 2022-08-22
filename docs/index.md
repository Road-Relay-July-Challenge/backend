# RRJC X Strava Web App API documentation

<img width="100%" alt="image" src="https://user-images.githubusercontent.com/60415251/181936592-b9c338b7-75c5-4479-a781-bcb75dc21f1c.png">


# Admin APIs

**Refresh All**
----
  Refreshes all details for all individuals and teams.

* **URL**

  /admin/refresh_all

* **Method:**

  `GET`
  
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


