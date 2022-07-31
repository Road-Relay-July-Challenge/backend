import React, { useEffect, useState, useCallback } from "react";
import { getHallOfFame, getAchievementsCount } from "../utils/httpsFunction";
import Typography from "@mui/material/Typography";
import { CircularProgress, Grid } from "@mui/material";
import CampaignIcon from "@mui/icons-material/Campaign";
import Announcement from "../components/announcement";

const HallOfFameContent = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [teamStats, setTeamStats] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      let timeout;
      const response = await getAchievementsCount();
      console.log(response.data);
      response.data.result.forEach((teamData) => {
        var totalTeamAchievementsMileage = 0;

        teamData.rewarded_mileage_array.forEach((individualData) => {
          totalTeamAchievementsMileage += Object.entries(individualData)[0][1];
        });

        teamData.achievement_count_array.forEach((individualData) => {
          individualData[Object.entries(individualData)[0][0]] =
            Object.entries(individualData)[0][1];
        });

        totalTeamAchievementsMileage +=
          teamData.is_all_achieved.number_achieved ==
          teamData.is_all_achieved.total_strength
            ? teamData.is_all_achieved.number_achieved * 1
            : 0;

        console.log(totalTeamAchievementsMileage);
        teamData["total_team_achievements_mileage"] =
          totalTeamAchievementsMileage;
      });

      response.data.result.sort((a, b) => {
        return (
          b.total_team_achievements_mileage - a.total_team_achievements_mileage
        );
      });
      console.log(response.data.result);
      setTeamStats(response.data.result);
      function removeLoading() {
        setIsLoading(false);
      }
      timeout = setTimeout(removeLoading, 2000);
    };
    fetchData();
  }, []);

  return (
    <>
      <Grid
        container
        direction="row"
        justifyContent="center"
        alignItems="center"
        spacing={{ xs: 0, sm: 0 }}
      >
        <Grid item xs={8} sm>
          <Typography
            variant="h7"
            align="center"
            component="div"
            fontWeight={300}
            style={{
              color: "#191C1F",
            }}
          >
            🟩 - All members achieved
          </Typography>
        </Grid>
        <Grid item xs={8} sm>
          <Typography
            variant="h7"
            align="center"
            component="div"
            fontWeight={300}
            style={{
              color: "#191C1F",
            }}
          >
            🟧 - Some achieved
          </Typography>
        </Grid>
        <Grid item xs={8} sm>
          <Typography
            variant="h7"
            align="center"
            component="div"
            fontWeight={300}
            style={{
              color: "#191C1F",
            }}
          >
            🟥 - None achieved
          </Typography>
        </Grid>
      </Grid>
      {teamStats.map((team, index) => (
        <div
          key={index}
          style={{
            width: "90%",
            height: "auto",
            background: "white",
            margin: "10px auto",
            borderRadius: "20px",
            paddingTop: "10px",
            paddingBottom: "20px",
            alignItems: "center",
            color: "#75808A",
            display: "flex",
            flexDirection: "column",
            animationName: "fadeIn",
            animationDuration: "1." + index * 10 + "s",
            position: "relative",
          }}
        >
          <Typography
            variant="h6"
            align="center"
            gutterBottom
            component="div"
            fontWeight={700}
            style={{
              //   padding: "15px",
              marginLeft: "15px",
              //   borderRadius: "20px",
              color: "#191C1F",
            }}
          >
            {team.team_name}
            {team.is_all_achieved.number_achieved ==
            team.is_all_achieved.team_strength
              ? "🟩"
              : team.is_all_achieved.number_achieved >= 1
              ? "🟧"
              : "🟥"}
          </Typography>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              width: "90%",
            }}
          >
            <div
              style={{
                width: "75%",
                marginLeft: "15px",
              }}
            >
              <div style={{}}>
                {team.achievement_count_array.map((athelete, index) => (
                  <div
                    key={index}
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      justifyContent: "space-between",
                    }}
                  >
                    <div>{Object.entries(athelete)[0][0]}</div>
                    <div>
                      {Object.entries(athelete)[0][1]}🏆{" "}
                      {/* {Object.entries(athelete)[0][1] > 1
                        ? "🟩"
                        : Object.entries(athelete)[0][1] === 0
                        ? "🟥"
                        : "🟧"} */}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div
              style={{
                borderLeft: "solid 1px black",
                paddingLeft: "20px",
                height: "100",
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <Typography
                variant="h7"
                align="center"
                gutterBottom
                component="div"
                fontWeight={700}
                style={{
                  color: "#191C1F",
                }}
              >
                Gained
              </Typography>
              <div>{team.total_team_achievements_mileage.toFixed(2)} km</div>
            </div>
          </div>
        </div>
      ))}
    </>
  );
};

//🟩 - 2 | 🟧 - 1 | 🟥 - 0

export default HallOfFameContent;
