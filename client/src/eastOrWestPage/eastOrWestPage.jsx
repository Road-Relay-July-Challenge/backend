import React from "react";
import EastOrWestContent from "./eastOrWestContent";
import Typography from "@mui/material/Typography";
import BottomAppBar from "../components/bottomAppBar";

const EastOrWestPage = () => {
  return (
    <>
      <div
        style={{
          marginTop: "20px",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          width: "100%",
          maxWidth: "600px",
          margin: "10px auto 0px auto",
          animationName: "fadeIn",
          animationDuration: "0.85s",
          position: "relative",
        }}
      >
        <Typography
          variant="h4"
          align="center"
          gutterBottom
          component="div"
          fontWeight={900}
          style={{
            color: "#191C1F",
          }}
        >
          East vs West
        </Typography>
        <EastOrWestContent />
      </div>
    </>
  );
};

export default EastOrWestPage;
