import React from "react";
import HallOfFameContent from "./hallOfFameContent";
import Typography from "@mui/material/Typography";
import BottomAppBar from "../components/bottomAppBar";

const HallOfFamePage = () => {
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
          Hall Of Fame
        </Typography>
        <HallOfFameContent />
      </div>
    </>
  );
};

export default HallOfFamePage;
