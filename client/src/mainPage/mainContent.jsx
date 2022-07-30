import React, { useState, useRef, useEffect } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import ArrowDropUpIcon from "@mui/icons-material/ArrowDropUp";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { purple, grey, green, red } from "@mui/material/colors";
import Slide from "@mui/material/Slide";
import {
  getAllDistance,
  getTeamDistance,
  getRankings,
} from "../utils/httpsFunction";
import Count from "../components/Count";
import { Button } from "@mui/material";
import { styled } from "@mui/material/styles";
import { useNavigate } from "react-router-dom";
import { CircularProgress } from "@mui/material";
import Announcement from "../components/announcement";

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

const theme = createTheme({
  palette: {
    primary: {
      // Purple and green play nicely together.
      main: purple[500],
    },
    secondary: {
      // This is green.A700 as hex.
      main: grey[500],
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
});

const ColorButton = styled(Button)((props) => ({
  width: "100%",
  borderRadius: "0px",
  margin: "0px auto 0px auto",
  justifySelf: "center",
  alignSelf: "center",
  alignItems: "center",
  color: "#ffffff",
  backgroundColor: "#000000",
  "&:focus": {
    backgroundColor: "#ffffff",
    color: "#000000",
  },
  animationName: "fadeIn" + props.direction,
  animationDuration: "0.85s",
  position: "relative",
}));

export default function MainContent() {
  const [tabValue, setTabValue] = useState(0);
  const [leftTab, setLeftTab] = useState(true);
  const [individualStats, setIndividualStats] = useState([]);
  const [teamStats, setTeamStats] = useState([]);
  const [isloading, setIsLoading] = useState(true);
  const containerRef = useRef(null);
  const navigate = useNavigate();

  const handleChange = (event, newValue) => {
    setTabValue(newValue);
    setLeftTab((prev) => !prev);
  };

  useEffect(() => {
    async function fetchData() {
      const response = await getAllDistance();
      const teamResponse = await getTeamDistance();
      const rankings = await getRankings();
      console.log(rankings);
      console.log(response.data.result);
      // slot ranking data in
      response.data.result.forEach((atheleteData) => {
        rankings.data.result.forEach((atheleteRankings) => {
          if (atheleteData.athlete_id === atheleteRankings.athlete_id) {
            atheleteData["oldranking"] = atheleteRankings.last_refresh_rank;
          }
        });
      });
      setIndividualStats(response.data.result);
      setTeamStats(teamResponse.data.result);
      setIsLoading(false);
    }
    fetchData();
  }, []);

  const directToEventPage = (link) => {
    navigate("../" + link, { replace: true });
  };

  return (
    <ThemeProvider theme={theme}>
      <ColorButton
        variant="contained"
        onClick={() => directToEventPage("HallOfFame")}
        sx={{ backgroundColor: "#45B8AC" }}
        disableRipple={true}
        fullWidth={true}
        direction="Right"
      >
        Hall Of Fame
      </ColorButton>
      <ColorButton
        variant="contained"
        onClick={() => directToEventPage("achievements")}
        sx={{ backgroundColor: "#e53170" }}
        style={{ marginBottom: "20px" }}
        disableRipple={true}
        fullWidth={true}
        direction="Left"
      >
        Achievements
      </ColorButton>
      <Announcement text="RRJC 2022 has concluded. Results will be released on 23rd." />
      <TableContainer
        ref={containerRef}
        component={Paper}
        sx={{
          width: "90%",
          maxWidth: 800,
          margin: "10px auto 10px auto",
          justifySelf: "center",
          display: "flex",
          flexDirection: "column",
        }}
        style={{
          animationName: "fadeIn",
          animationDuration: "0.85s",
          position: "relative",
        }}
      >
        <Tabs
          value={tabValue}
          onChange={handleChange}
          aria-label="wrapped label tabs example"
          variant="fullWidth"
          centered
          indicatorColor="secondary"
          textColor="secondary"
        >
          <Tab label="Team" />
          <Tab label="Individual" />
        </Tabs>
        {isloading ? (
          <CircularProgress
            style={{ alignSelf: "center", margin: "20px", color: "black" }}
          />
        ) : (
          <Box style={{ overflow: "scroll" }}>
            <TabPanel value={tabValue} index={0}>
              <Slide
                direction="right"
                in={leftTab}
                mountOnEnter
                unmountOnExit
                container={containerRef.current}
              >
                <Table
                  value="1"
                  sx={{ margin: 0 }}
                  size="small"
                  aria-label="a dense table"
                >
                  <TableHead>
                    <TableRow>
                      <TableCell align="right" padding="none">
                        {""}
                      </TableCell>
                      <TableCell>Team Name</TableCell>
                      <TableCell padding="none"> Team No</TableCell>
                      <TableCell align="right">Total km</TableCell>
                      <TableCell padding="none" align="right">
                        True km
                      </TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {teamStats.map((row, index) => (
                      <TableRow
                        key={index}
                        sx={{
                          "&:last-child td, &:last-child th": { border: 0 },
                        }}
                      >
                        <TableCell component="th" scope="row" padding="none">
                          {index + 1}
                        </TableCell>
                        <TableCell
                          style={{
                            overflowWrap: "break-word",
                            wordBreak: "break-all",
                          }}
                        >
                          {row.team_name}
                        </TableCell>
                        {/* <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell> */}
                        <TableCell padding="none" align="center">
                          {row.team_id}
                        </TableCell>
                        <TableCell align="right">
                          {row.team_contributed_mileage.toFixed(2) || "no run"}
                        </TableCell>
                        <TableCell align="right" padding="none">
                          {row.team_true_mileage.toFixed(2)}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </Slide>
            </TabPanel>

            <TabPanel value={tabValue} index={1}>
              <Slide
                direction="left"
                in={!leftTab}
                mountOnEnter
                unmountOnExit
                container={containerRef.current}
              >
                <Table
                  value="1"
                  sx={{ margin: 0 }}
                  size="small"
                  aria-label="a dense table"
                  padding="none"
                >
                  <TableHead>
                    <TableRow>
                      <TableCell padding="default">{""}</TableCell>
                      <TableCell>Name</TableCell>
                      {/* <TableCell>{""}</TableCell> */}
                      <TableCell>Team</TableCell>
                      <TableCell padding="default" align="right">
                        Total km
                      </TableCell>
                      <TableCell padding="default" align="right">
                        True km
                      </TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {individualStats.map((row, index) => (
                      <TableRow
                        key={index}
                        style={{
                          background:
                            row.oldranking < index + 1
                              ? "#e53170"
                              : row.oldranking > index + 1
                              ? "#45B8AC"
                              : "white",
                        }}
                        sx={{
                          "&:last-child td, &:last-child th": { border: 0 },
                        }}
                      >
                        <TableCell
                          component="th"
                          scope="row"
                          // style={{ display: "flex", flexDirection: "column" }}
                          style={{ paddingLeft: "7px" }}
                        >
                          {"    " + (index + 1)}
                          {/* <ArrowDropUpIcon color="up" /> */}
                        </TableCell>
                        <TableCell>{row.name} </TableCell>
                        <TableCell align="center">{row.team_number}</TableCell>
                        {/* <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell> */}
                        <TableCell padding="default" align="right">
                          {row.total_contributed_mileage.toFixed(2)}
                        </TableCell>
                        <TableCell padding="default" align="right">
                          {row.total_true_mileage.toFixed(2)}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </Slide>
            </TabPanel>
          </Box>
        )}
      </TableContainer>
    </ThemeProvider>
  );
}
