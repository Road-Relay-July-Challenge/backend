import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { Button } from "@mui/material";

export default function registerForm() {
  return (
    <Box
      component="form"
      height="auto"
      sx={{
        backgroundColor: "white",
      }}
      noValidate
      autoComplete="off"
      width="90%"
      margin="20px auto"
    >
      <div style={{ display: "flex", flexDirection: "column" }}>
        <Typography
          variant="h5"
          noWrap
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
              justifyContent: "center",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
          }}
        >
          Strava Registration Form
        </Typography>
        <Typography
          variant="h7"
          component="a"
          mt={3}
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            padding: 3,
          }}
        >
          Follow the steps below to link your strava account so that the running
          data could be collected.
        </Typography>
        <Typography
          variant="h7"
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            marginTop: 8,
            padding: 3,
          }}
        >
          1. Copy the link provided below and paste it into your browser.
        </Typography>
        <Typography
          variant="h7"
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            marginTop: 1,
            wordBreak: "break-all",
            padding: 3,
          }}
        >
          {
            "https://www.strava.com/oauth/authorize?client_id=51907&redirect_uri=http://localhost&response_type=code&scope=activity:read_all"
          }
        </Typography>
        <Button
          onClick={() => {
            navigator.clipboard.writeText(
              "https://www.strava.com/oauth/authorize?client_id=51907&redirect_uri=http://localhost&response_type=code&scope=activity:read_all"
            );
          }}
          variant="text"
        >
          Click to copy the link above.
        </Button>
        <Typography
          variant="h7"
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            marginTop: 8,
            padding: 3,
          }}
        >
          2. There should be a page asking you for permission. You will also be
          asked to sign in to your strava account.
        </Typography>
        <Typography
          variant="h7"
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            marginTop: 8,
            padding: 3,
          }}
        >
          3. After clicking "Authorize", it will bring you to another page that
          says "This site can't be reached." Ignore the content on the webpage
          and past the content in the url bar into the text field below.
        </Typography>
        <Typography
          variant="h7"
          component="a"
          sx={{
            display: {
              xs: "flex",
              md: "flex",
            },
            fontWeight: 1500,
            color: "inherit",
            textDecoration: "none",
            marginTop: 2,
            wordBreak: "break-all",
            padding: 3,
          }}
        >
          The URL would look something like this
          http://localhost/?state=&code=54715678a2af7b7ecc998dde3f9453a08eaaa1e4&scope=read,activity:read_all
        </Typography>
        <div style={{ display: "flex", width: "90%", padding: "auto auto" }}>
          <TextField
            id="standard-helperText"
            label="Paste the content in url bar here"
            variant="filled"
            sx={{ width: "90%" }}
          />
          <Button variant="text">Submit</Button>
        </div>
      </div>
    </Box>
  );
}
