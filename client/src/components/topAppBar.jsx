import React from "react";
import AppBar from "@mui/material/AppBar";
import { Container } from "@mui/system";
import Typography from "@mui/material/Typography";
import {
  Toolbar,
  Box,
  IconButton,
  Menu,
  MenuItem,
  Button,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import DirectionsRunIcon from "@mui/icons-material/DirectionsRun";
import { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const pages = ["home", "register", "contact"];

const TopAppBar = () => {
  let navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };

  const handleCloseNavMenu = (page) => {
    navigate("../" + page, { replace: true });
    setAnchorElNav(null);
  };

  const handleCloseNavMenuWithoutReplace = () => {
    setAnchorElNav(null);
  };

  return (
    <AppBar
      position="static"
      sx={{ height: "max-content", background: "black" }}
    >
      <Container maxWidth="xl" sx={{}}>
        <Toolbar disableGutters>
          <DirectionsRunIcon
            sx={{ display: { xs: "none", md: "flex" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="/"
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
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: "bottom",
                horizontal: "left",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "right",
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenuWithoutReplace}
              sx={{
                display: { xs: "block", md: "none" },
                transitionDuration: {
                  appearance: 50,
                  enter: 50,
                  exit: 50,
                },
              }}
            >
              {pages.map((page, index) => (
                <MenuItem
                  key={index}
                  sx={{ width: "100vw" }}
                  onClick={() => handleCloseNavMenu(page)}
                >
                  <Typography sx={{ width: "100vw" }} textAlign="center">
                    {page}
                  </Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
          <DirectionsRunIcon
            sx={{ display: { xs: "flex", md: "none" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
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
