import React, { useEffect, useState } from "react";
import TopAppBar from "../components/topAppBar";
import RedirectContent from "./redirectContent";
import _ from "lodash";
import { testAuthGetter, getUserData } from "../utils/httpsFunction";

const RedirectPage = (props) => {
  const [isSuccess, setIsSuccess] = useState(false);
  useEffect(() => {
    const cleanUpAuthToken = (str) => {
      return str.split("&")[1].slice(5);
    };
    async function authenticate() {
      try {
        // If not redirected to Strava, return to home
        // if (_.isEmpty(location)) {
        //   console.log("Its here");
        //   return history.push("/");
        // }

        // Save the Auth Token to the Store (it's located under 'search' for some reason)
        const stravaAuthToken = cleanUpAuthToken(window.location.search);
        console.log(stravaAuthToken);
        const tokens = await testAuthGetter(stravaAuthToken);
        console.log(tokens);
        const accessToken = tokens.access_token;
        const userID = tokens.athlete.id;
        const user = await getUserData(userID, accessToken);
        console.log(user);
        if (user.status === 200) {
          console.log("You have successfully registered your strava account.");
          setIsSuccess(true);
        } else {
          throw new Error("Problem registering, please try again!");
        }
      } catch (error) {
        console.log(error);
      }
    }
    authenticate();
  }, []);

  return (
    <>
      <TopAppBar />
      <RedirectContent success={isSuccess} />
    </>
  );
};

export default RedirectPage;
