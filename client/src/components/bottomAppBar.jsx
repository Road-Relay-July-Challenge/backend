import React from "react";
import Typography from "@mui/material/Typography";
import InstagramIcon from "@mui/icons-material/Instagram";

const BottomAppBar = () => {
  const redirectToInsta = async () => {
    window.open(`https://www.instagram.com/road.relay/`, "_blank");
  };

  return (
    <div
      style={{
        backgroundColor: "black",
        height: "auto",
        width: "100vw",
        color: "white",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "10px 0px",
        gap: "10px",
        animationName: "fadeInOpacityBottomNavBar",
        animationDuration: "7s",
        alignSelf: "flex-end",
        justifySelf: "flex-end",
        marginBottom: "0px",
      }}
    >
      <Typography
        variant="h7"
        noWrap
        component="a"
        href="/"
        fullWidth
        sx={{
          mr: 2,
          display: { xs: "flex", md: "flex", textAlign: "center" },
          fontFamily: "monospace",
          fontWeight: 200,
          color: "inherit",
          textDecoration: "none",
        }}
      >
        Built and designed by RH Road Relay
      </Typography>
      <Typography
        variant="h7"
        noWrap
        component="a"
        href="/"
        fullWidth
        sx={{
          mr: 2,
          display: { xs: "flex", md: "flex", textAlign: "center" },
          fontFamily: "monospace",
          fontWeight: 200,
          color: "inherit",
          textDecoration: "none",
        }}
      >
        All rights reserved.©
      </Typography>
      {/* both ways can be used to open a new tab */}
      {/* <a
        href="https://www.instagram.com/road.relay/"
        target="_blank"
        rel="noreferrer"
        style={{ color: "white" }}
      >
        test
      </a> */}
      <InstagramIcon fontSize="large" onClick={() => redirectToInsta()} />
    </div>
  );
};

export default BottomAppBar;
