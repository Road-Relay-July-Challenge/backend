import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { Button } from "@mui/material";
import Stack from "@mui/material/Stack";
import Divider from "@mui/material/Divider";
import { createTheme } from "@mui/material/styles";
import { purple, grey, green, red } from "@mui/material/colors";
import { styled } from "@mui/material/styles";

export const cleanUpAuthToken = (str) => {
  return str.split("&")[1].slice(5);
};

export default function registerForm() {
  const { REACT_APP_CLIENT_ID } = process.env;
  const redirectUrl = "https://rrjc-app-herokuapp.com/auth/verify";

  const theme = createTheme({
    palette: {
      primary: {
        // Purple and green play nicely together.
        main: grey[100],
        contrastText: "#ffffff",
      },
      secondary: {
        // This is green.A700 as hex.
        main: "#ffffff",
        contrastText: red[500],
      },
      up: {
        main: green[500],
      },
      down: {
        main: red[500],
      },
      nothing: {
        main: "#ffffff",
      },
    },
    overrides: {
      MuiButton: {
        secondary: {
          main: "#ffffff",
          contrastText: red[500],
        },
      },
    },
  });

  const ColorButton = styled(Button)(() => ({
    color: "#ffffff",
    backgroundColor: "#000000",
    "&:focus": {
      backgroundColor: "#ffffff",
      color: "#000000",
    },
  }));

  const handleLogin = async () => {
    window.location = `http://www.strava.com/oauth/authorize?client_id=${REACT_APP_CLIENT_ID}&response_type=code&redirect_uri=${redirectUrl}/exchange_token&approval_prompt=force&scope=read`;
  };

  return (
    <Box
      component="form"
      height="auto"
      sx={
        {
          // backgroundColor: "white",
        }
      }
      noValidate
      autoComplete="off"
      width="90%"
      margin="20px auto"
    >
      <Stack spacing={2}>
        <Typography variant="h6" align="center" gutterBottom component="div">
          Strava Registration
        </Typography>

        <Typography variant="body1" gutterBottom component="div">
          Click on the button below to link RRJC Web App with your strava
          account.
        </Typography>

        <ColorButton
          variant="contained"
          onClick={() => handleLogin()}
          sx={{ backgroundColor: "#000000" }}
          disableRipple={true}
        >
          Connect to Strava
        </ColorButton>
      </Stack>
    </Box>
  );
}
