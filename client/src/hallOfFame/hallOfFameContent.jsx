import React, { useEffect, useState, useCallback } from "react";
import TopAppBar from "../components/topAppBar";
import ConstructionIcon from "@mui/icons-material/Construction";
import { getHallOfFame } from "../utils/httpsFunction";
import Typography from "@mui/material/Typography";
import { CircularProgress } from "@mui/material";

const HallOfFameContent = () => {
  const [result, setResult] = useState([]);
  const [highestCount, setHighestCount] = useState(0);
  const [highestApp, setHighestApp] = useState([]);
  const [allHallOfFame, setAllOfFame] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(true);
    const fetchData = async () => {
      const response = await getHallOfFame();
      console.log(response.data);
      var records = {};
      var resultNew = [];
      var setAthelete = new Set();
      for (var object in response.data.result) {
        response.data.result[object].forEach((data) => {
          setAthelete.add(data.name);
          if (records[data.name]) {
            records[data.name] += 1;
            if (records[data.name] > highestCount) {
              setHighestCount(records[data.name]);
            }
            console.log(highestCount);
          } else {
            records[data.name] = 1;
          }
        });
        const resultSet = {
          name: object,
          fames: response.data.result[object],
        };
        resultNew.push(resultSet);
      }
      setResult(resultNew);
      const topAthelete = [...setAthelete].filter(
        (athelete) => records[athelete] === highestCount
      );
      setAllOfFame(topAthelete);
      setIsLoading(false);
    };
    fetchData();
  }, [allHallOfFame.length, highestCount]);

  return (
    <>
      <div
        style={{
          width: "90%",
          height: "140px",
          background: "white",
          margin: "10px auto",
          borderRadius: "20px",
          paddingBottom: "20px",
          paddingTop: "20px",
          display: "flex",
          flexDirection: "column",
          animationName: "fadeIn",
          animationDuration: "0.85s",
          position: "relative",
        }}
      >
        <Typography
          variant="h5"
          align="center"
          gutterBottom
          component="div"
          fontWeight={700}
          style={{
            color: "#191C1F",
          }}
        >
          Highest appearance
        </Typography>
        {isLoading ? (
          <CircularProgress style={{ alignSelf: "center", color: "black" }} />
        ) : (
          <div>
            {allHallOfFame.map((athelete, index) => (
              <Typography
                key={index}
                variant="h7"
                align="center"
                gutterBottom
                component="div"
                fontWeight={400}
                style={{
                  color: "#191C1F",
                }}
              >
                {athelete} ({highestCount})
              </Typography>
            ))}
          </div>
        )}
      </div>

      {result.map((fame, index) => (
        <div
          key={index}
          style={{
            width: "90%",
            height: "auto",
            background: "white",
            margin: "10px auto",
            borderRadius: "20px",
            paddingBottom: "20px",
            color: "#75808A",
            display: "flex",
            flexDirection: "column",
            animationName: "fadeIn",
            animationDuration: "1s",
            position: "relative",
          }}
        >
          <Typography
            variant="h5"
            align="center"
            gutterBottom
            component="div"
            fontWeight={700}
            style={{
              padding: "15px",
              margin: "15px",
              borderRadius: "20px",
              color: "#191C1F",
            }}
          >
            {fame.name}
          </Typography>
          {isLoading ? (
            <CircularProgress style={{ alignSelf: "center", color: "black" }} />
          ) : (
            <div>
              {fame.fames.map((athelete, index) => (
                <div key={index}>
                  <Typography
                    variant={index === 0 ? "h7" : "h7"}
                    align="center"
                    gutterBottom
                    component="div"
                    fontWeight={500}
                    style={{
                      display: "flex",
                      flexDirection: "row",
                      justifyContent: "space-between",
                      padding: "5px 20px",
                      marginRight: "15px",
                      marginLeft: "15px",
                      color: "#191C1F",
                    }}
                  >
                    <div>
                      {index + 1}
                      {".   " + athelete.name}
                      {"  (Team " + athelete.team_number + ")"}
                    </div>
                    <div>{athelete.data}</div>
                  </Typography>
                </div>
              ))}
            </div>
          )}
        </div>
      ))}
    </>
  );
};

export default HallOfFameContent;
