import React, { useEffect, useState } from "react";
import TopAppBar from "../components/topAppBar";
import RedirectContent from "./redirectEastWestContent";
import { Button, Stack, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { eastWestAuthGetter } from "../utils/httpsFunction";
import { styled } from "@mui/material/styles";
import BottomAppBar from "../components/bottomAppBar";

const RedirectPage = (props) => {
  let navigate = useNavigate();
  const [isSuccess, setIsSuccess] = useState(false);
  const [successMessage, setSuccessMessage] = useState("");
  useEffect(() => {
    const cleanUpAuthToken = (str) => {
      return str.split("&")[1].slice(5);
    };
    const getEastOrWest = (str) => {
      return str.split("&")[0].slice(7);
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
        const chosenSide = getEastOrWest(window.location.search);
        console.log(stravaAuthToken);
        console.log(chosenSide);
        const response = await eastWestAuthGetter(stravaAuthToken, chosenSide);
        console.log(response);
        console.log(response.message);
        if (response.success) {
          console.log("You have successfully registered your strava account.");
          setIsSuccess(true);
          setSuccessMessage(response.message);
        } else {
          throw new Error("Problem registering, please try again!");
        }
      } catch (error) {
        console.log(error);
      }
    }
    authenticate();
  }, []);

  const ColorButton = styled(Button)(() => ({
    color: "#ffffff",
    backgroundColor: "#000000",
    "&:focus": {
      backgroundColor: "#ffffff",
      color: "#000000",
    },
  }));

  const submitAccessToken = () => {
    console.log("Submitting token to backend");
    navigate("../home", { replace: true });
  };

  return (
    <>
      <TopAppBar />
      <Box
        component="form"
        height="auto"
        noValidate
        autoComplete="off"
        width="90%"
        margin="20px auto"
      >
        <Stack spacing={2}>
          <RedirectContent
            success={isSuccess}
            successMessage={successMessage}
            submitHandler={submitAccessToken}
          />
          <ColorButton
            variant="contained"
            onClick={() => submitAccessToken()}
            sx={{ backgroundColor: "#000000" }}
            disableRipple={true}
          >
            Click to go to Home page.
          </ColorButton>
        </Stack>
      </Box>
    </>
  );
};

export default RedirectPage;
