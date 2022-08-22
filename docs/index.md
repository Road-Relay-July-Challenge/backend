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
  
*  **URL Params**

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
  
*  **URL Params**

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
  
*  **URL Params**

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
  
*  **URL Params**

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
