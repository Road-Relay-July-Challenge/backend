import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import { Button } from "@mui/material";

export default function redirectContent(props) {
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
      {/* <div style={{ display: "flex", flexDirection: "column" }}>
        <Button variant="text">Redirected From Strava</Button>
      </div> */}
      <Typography variant="body1" gutterBottom component="div">
        {props.success
          ? "You have successfully registered your strava account"
          : "loading..."}
      </Typography>
    </Box>
  );
}
