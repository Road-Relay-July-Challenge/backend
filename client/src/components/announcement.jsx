import React from "react";
import Typography from "@mui/material/Typography";
import CampaignIcon from "@mui/icons-material/Campaign";

const Announcement = ({ text = "More announcements coming." }) => {
  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          //padding: "10px",
          border: "black 1px solid",
          width: "90%",
          maxWidth: "800px",
          margin: "0px auto 10px auto",
          animationName: "fadeInOpacity",
          animationDuration: "3.5s",
        }}
      >
        <div>
          <CampaignIcon />
          <CampaignIcon />
          <CampaignIcon />
        </div>
        <Typography
          variant="h7"
          align="center"
          gutterBottom
          component="div"
          fontWeight={300}
          style={{
            color: "#191C1F",
            margin: "5px",
          }}
        >
          {text}
        </Typography>
      </div>
    </>
  );
};

export default Announcement;
