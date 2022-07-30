import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import { Button } from "@mui/material";
import Stack from "@mui/material/Stack";
// import { createTheme } from "@mui/material/styles";
// import { grey, green, red } from "@mui/material/colors";
import { styled } from "@mui/material/styles";
import Announcement from "../components/announcement";

export const cleanUpAuthToken = (str) => {
  return str.split("&")[1].slice(5);
};

export default function registerForm() {
  const ColorButton = styled(Button)(() => ({
    color: "#ffffff",
    backgroundColor: "#000000",
    "&:focus": {
      backgroundColor: "#ffffff",
      color: "#000000",
    },
  }));

  return (
    <Box
      component="form"
      height="auto"
      noValidate
      autoComplete="off"
      width="90%"
      margin="20px auto"
    >
      <Announcement text="Strava registration and East VS West registration has closed." />
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
          // onClick={() => handleLogin()}
          sx={{ backgroundColor: "#000000" }}
          disableRipple={true}
          href={"https://rrjc-app.herokuapp.com/auth/authorize"}
          disabled={true}
        >
          Connect to Strava
        </ColorButton>

        <Typography variant="h6" align="center" gutterBottom component="div">
          East or West
        </Typography>

        <Typography variant="body1" gutterBottom component="div">
          Click on the button belows to choose East or West. You will be
          prompted to log in to Strava for us to know who you are.
        </Typography>

        <ColorButton
          variant="contained"
          sx={{ backgroundColor: "green" }}
          disableRipple={true}
          disabled={true}
          href={
            "https://rrjc-app.herokuapp.com/auth/authorize_east_west?chosen_side=east"
          }
        >
          EAST
        </ColorButton>

        <ColorButton
          variant="contained"
          sx={{ backgroundColor: "red" }}
          disableRipple={true}
          disabled={true}
          href={
            "https://rrjc-app.herokuapp.com/auth/authorize_east_west?chosen_side=west"
          }
        >
          WEST
        </ColorButton>
      </Stack>
    </Box>
  );
}
