import React, { useState, useRef, useEffect } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { purple, grey, green, red } from "@mui/material/colors";
import Slide from "@mui/material/Slide";
import { getEastWestList } from "../utils/httpsFunction";
import { Button } from "@mui/material";
import { styled } from "@mui/material/styles";

function createData(name, total, last, positionChange) {
  return { name, total, last, positionChange };
}

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

const ColorButton = styled(Button)(() => ({
  width: "100%",
  borderRadius: "0px",
  margin: "0px auto 10px auto",
  justifySelf: "center",
  alignSelf: "center",
  alignItems: "center",
  color: "#ffffff",
  backgroundColor: "#000000",
  "&:focus": {
    backgroundColor: "#ffffff",
    color: "#000000",
  },
}));

export default function MainContent() {
  const [tabValue, setTabValue] = useState(0);
  const [leftTab, setLeftTab] = useState(true);
  const [eastStats, setEastStats] = useState([]);
  const [westStats, setWestStats] = useState([]);
  const [eastDistance, setEastDistance] = useState(0);
  const [westDistance, setWestDistance] = useState(0);
  const containerRef = useRef(null);

  const handleChange = (event, newValue) => {
    setTabValue(newValue);
    setLeftTab((prev) => !prev);
  };

  useEffect(() => {
    async function fetchData() {
      const response = await getEastWestList();
      console.log(response.data.result);
      setEastStats(response.data.result.east_side_list);
      setWestStats(response.data.result.west_side_list);
      setEastDistance(response.data.result.east_side_mileage);
      setWestDistance(response.data.result.west_side_mileage);
    }
    fetchData();
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <Typography
        variant="h7"
        align="center"
        gutterBottom
        component="div"
        fontWeight={300}
        style={{
          color: "#191C1F",
        }}
      >
        The event has concluded.
      </Typography>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          margin: "10px auto 0px auto",
          width: "90%",
          maxWidth: 800,
        }}
      >
        <Typography variant="h4" align="center" component="div">
          West
        </Typography>
        <Typography variant="h4" align="center" component="div">
          East
        </Typography>
      </div>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          margin: "0px auto 0px auto",
          width: "90%",
          maxWidth: 800,
        }}
      >
        <Typography variant="h4" align="center" component="div">
          {westDistance.toFixed(2)} km
        </Typography>
        <Typography variant="h4" align="center" component="div">
          {eastDistance.toFixed(2)} km
        </Typography>
      </div>
      <div className="barChart">
        <div
          style={{
            height: "30px",
            background: "#cc0000",
            flexGrow: westDistance,
            animation: "myEffectEast 5s",
            "@keyframes myEffectEast": {
              "0%": {
                flexGrow: "1",
              },
              "100%": {
                flexGrow: westDistance,
              },
            },
          }}
        ></div>
        <div
          style={{
            height: "30px",
            background: "#009900",
            flexGrow: eastDistance,
            animation: "myEffectWest 5s",
            "@keyframes myEffectWest": {
              "0%": {
                flexGrow: "1",
              },
              "100%": {
                flexGrow: eastDistance,
              },
            },
          }}
        ></div>
      </div>
      <TableContainer
        ref={containerRef}
        component={Paper}
        sx={{
          width: "90%",
          maxWidth: 800,
          margin: "0px auto 10px auto",
          justifySelf: "center",
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
          <Tab label="West" />
          <Tab label="East" />
        </Tabs>
        <Box style={{ overflow: "scroll" }}>
          <TabPanel value={tabValue} index={0}>
            <Slide
              direction="left"
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
                    <TableCell>{""}</TableCell>
                    <TableCell>Name</TableCell>
                    {/* <TableCell>{""}</TableCell> */}
                    <TableCell>Total km</TableCell>
                    <TableCell>Awarded km</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {westStats.map((row, index) => (
                    <TableRow
                      key={index}
                      sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                    >
                      <TableCell component="th" scope="row">
                        {index + 1}
                      </TableCell>
                      <TableCell>{row.name}</TableCell>
                      {/* <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell> */}
                      <TableCell>
                        {row.mileage.toFixed(2) || "no run"}
                      </TableCell>
                      <TableCell>
                        {row.awarded_mileage.toFixed(2) || "no run"}
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
              >
                <TableHead>
                  <TableRow>
                    <TableCell>{""}</TableCell>
                    <TableCell>Name</TableCell>
                    {/* <TableCell>{""}</TableCell> */}
                    <TableCell>Total km</TableCell>
                    <TableCell>Awarded km</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {eastStats.map((row, index) => (
                    <TableRow
                      key={index}
                      sx={{
                        "&:last-child td, &:last-child th": { border: 0 },
                      }}
                    >
                      <TableCell
                        component="th"
                        scope="row"
                        // style={{ display: "flex", flexDirection: "column" }}
                      >
                        <div style={{ display: "flex" }}>
                          {index + 1}
                          {/* <ArrowDropUpIcon color="up" /> */}
                        </div>
                      </TableCell>
                      <TableCell>{row.name} </TableCell>
                      {/* <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell> */}
                      <TableCell>{row.mileage.toFixed(2)}</TableCell>
                      <TableCell>
                        {row.awarded_mileage.toFixed(2) || "no run"}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Slide>
          </TabPanel>
        </Box>
      </TableContainer>
    </ThemeProvider>
  );
}
