import React from "react";
import AppBar from "@mui/material/AppBar";
import { Container } from "@mui/system";
import Typography from "@mui/material/Typography";
import { Toolbar, Box, IconButton, Button } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import DirectionsRunIcon from "@mui/icons-material/DirectionsRun";
import { useState } from "react";
// import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const pages = [
  "Home",
  "Register",
  "Hall Of Fame",
  "East Or West",
  "Achievements",
];

const TopAppBar = () => {
  let navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(!anchorElNav);
  };

  const handleCloseNavMenu = (page) => {
    if (page === "Hall Of Fame") {
      page = "HallOfFame";
    } else if (page === "East Or West") {
      page = "eastOrWest";
    }
    navigate("../" + page, { replace: true });
    setAnchorElNav(null);
  };

  const handleCloseNavMenuWithoutReplace = () => {
    setAnchorElNav(null);
  };

  return (
    <AppBar
      position={anchorElNav ? "sticky" : "static"}
      sx={{ height: "max-content", background: "black", top: "0" }}
    >
      {anchorElNav && (
        <div
          style={{
            display: anchorElNav ? "flex" : "none",
            flexDirection: "column",
            position: "fixed",
            top: "50px",
            zIndex: "2",
            width: "100vw",
            backgroundColor: "blacks",
            animationName: "fadeInMenu",
            animationDuration: "0.5s",
          }}
        >
          {pages.map((page, index) => (
            <div
              key={index}
              onClick={() => handleCloseNavMenu(page)}
              style={{
                padding: "0px 5px 15px 25px",
                backgroundColor: "black",
              }}
            >
              {page}
            </div>
          ))}
        </div>
      )}
      <div
        onClick={() => handleCloseNavMenuWithoutReplace()}
        style={{
          display: anchorElNav ? "block" : "none",
          position: "fixed",
          backgroundColor: "white",
          width: "100vw",
          height: "80vh",
          opacity: "0.9",
          zIndex: "1",
          bottom: "0px",
          animationName: "fadeInOpacityOverlay",
          animationDuration: "1s",
        }}
      ></div>
      <Container maxWidth="xl" sx={{}}>
        <Toolbar disableGutters>
          <DirectionsRunIcon
            sx={{ display: { xs: "none", md: "flex" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="/home"
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex", textAlign: "center" },
              fontFamily: "monospace",
              fontWeight: 2000,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            RRJC'22
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
          </Box>
          <DirectionsRunIcon
            sx={{ display: { xs: "flex", md: "none" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="/home"
            sx={{
              mr: 2,
              display: { xs: "flex", md: "none" },
              flexGrow: 1,
              fontFamily: "monospace",
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            RRJC'22
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            {pages.map((page, index) => (
              <>
                <Button
                  key={index}
                  onClick={() => handleCloseNavMenu(page)}
                  sx={{ my: 2, color: "white", display: "block" }}
                >
                  {page}
                </Button>
              </>
            ))}
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default TopAppBar;
