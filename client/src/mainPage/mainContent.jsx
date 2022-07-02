import React, { useState, useRef } from "react";
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

const rows = [
  createData("1", 159, 6.0, 1),
  createData("2", 237, 9.0, -1),
  createData("3", 262, 16.0, 0),
  createData("4", 305, 3.7, 0),
  createData("5", 356, 16.0, 1),
];

const individualRows = [
  createData("Chua Min", 15, 6.0, 4),
  createData("Jason", 237, 9.0, -3),
  createData("Wen Feng", 262, 16.0, 0),
  createData("Hao Jun", 305, 3.7, 4.3),
  createData("Lucas", 356, 16.0, 3.9),
];

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

export default function MainContent() {
  const [tabValue, setTabValue] = useState(0);
  const [leftTab, setLeftTab] = useState(true);
  const containerRef = useRef(null);

  const handleChange = (event, newValue) => {
    setTabValue(newValue);
    setLeftTab((prev) => !prev);
  };

  return (
    <ThemeProvider theme={theme}>
      <TableContainer
        ref={containerRef}
        component={Paper}
        sx={{
          width: "90%",
          maxWidth: 800,
          margin: "10px auto 10px auto",
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
          <Tab label="Team" />
          <Tab label="Individual" />
        </Tabs>
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
                    <TableCell>Team Name</TableCell>
                    <TableCell align="right">{""}</TableCell>
                    <TableCell align="right">Total Mileage</TableCell>
                    <TableCell align="right">Last Week</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {rows.map((row) => (
                    <TableRow
                      key={row.name}
                      sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                    >
                      <TableCell component="th" scope="row">
                        {row.name}
                      </TableCell>
                      <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell>
                      <TableCell align="right">{row.total}</TableCell>
                      <TableCell align="right">{row.last}</TableCell>
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
                value="2"
                sx={{ margin: 0 }}
                size="small"
                aria-label="a dense table"
              >
                <TableHead>
                  <TableRow>
                    <TableCell>Name</TableCell>
                    <TableCell>{""}</TableCell>
                    <TableCell>Total Mileage</TableCell>
                    <TableCell>Last Week</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {individualRows.map((row) => (
                    <TableRow
                      key={row.name}
                      sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                    >
                      <TableCell component="th" scope="row">
                        {row.name}
                      </TableCell>
                      <TableCell>
                        {row.positionChange > 0 ? (
                          <ArrowDropUpIcon color="up" />
                        ) : row.positionChange < 0 ? (
                          <ArrowDropDownIcon color="down" />
                        ) : (
                          <ArrowDropDownIcon color="nothing" />
                        )}
                      </TableCell>
                      <TableCell>{row.total}</TableCell>
                      <TableCell>{row.last}</TableCell>
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
