import React, { Component } from "react";
import Typography from "@mui/material/Typography";

class Clock extends Component {
  constructor(props) {
    super(props);
    this.state = {
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
    };
  }
  componentWillMount() {
    this.getTimeUntil(this.props.deadline);
  }
  componentDidMount() {
    setInterval(() => this.getTimeUntil(this.props.deadline), 1000);
  }
  leading0(num) {
    return num < 10 ? "0" + num : num;
  }
  leading1(num) {
    return num < 10 ? "0" + num : num;
  }
  getTimeUntil(deadline) {
    const time = Date.parse(deadline) - Date.parse(new Date());
    if (time < 0) {
      this.setState({ days: 0, hours: 0, minutes: 0, seconds: 0 });
    } else {
      const seconds = Math.floor((time / 1000) % 60);
      const minutes = Math.floor((time / 1000 / 60) % 60);
      const hours = Math.floor((time / (1000 * 60 * 60)) % 24);
      const days = Math.floor(time / (1000 * 60 * 60 * 24));
      this.setState({ days, hours, minutes, seconds });
    }
  }
  render() {
    return (
      <>
        <div
          style={{
            textAlign: "center",
            paddingTop: "15px",
            display: "flex",
            flexDirection: "row",
            height: "auto",
            width: "90%",
            maxWidth: 800,
            color: "#191C1F",
            flexWrap: "wrap",
            justifyContent: "center",
            margin: "auto",
            borderRadius: "5px 5px 0px 0px",
            background: "white",
          }}
        >
          Time Left
        </div>
        <div
          style={{
            textAlign: "center",
            display: "flex",
            flexDirection: "row",
            height: "auto",
            width: "90%",
            maxWidth: 800,
            color: "#191C1F",
            flexWrap: "wrap",
            justifyContent: "center",
            gap: "15px",
            margin: "0px auto 10px auto",
            borderRadius: "0px 0px 5px 5px",
            paddingBottom: "15px",
            paddingTop: "0px",
            background: "white",
          }}
        >
          <div
            className="Clock-days"
            style={{
              display: "flex",
              flexDirection: "column",
              background: "transparent",
            }}
          >
            <Typography
              variant="h3"
              noWrap
              component="a"
              href="/"
              sx={{
                display: { md: "flex", textAlign: "center" },
                fontFamily: "monospace",
                fontWeight: 2000,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              {this.leading0(this.state.days)}
            </Typography>
            Days
          </div>
          <div
            className="Clock-hours"
            style={{
              display: "flex",
              flexDirection: "column",
            }}
          >
            <Typography
              variant="h3"
              noWrap
              component="a"
              href="/"
              sx={{
                display: { md: "flex", textAlign: "center" },
                fontFamily: "monospace",
                fontWeight: 2000,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              {this.leading0(this.state.hours)}
            </Typography>
            Hours
          </div>
          {/* </div> */}
          {/* <div style={{ display: "flex" }}> */}
          <div
            className="Clock-minutes"
            style={{
              display: "flex",
              flexDirection: "column",
            }}
          >
            <Typography
              variant="h3"
              noWrap
              component="a"
              href="/"
              sx={{
                display: { md: "flex", textAlign: "center" },
                fontFamily: "monospace",
                fontWeight: 2000,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              {this.leading0(this.state.minutes)}
            </Typography>
            Min
          </div>
          <div
            className="Clock-seconds"
            style={{
              display: "flex",
              flexDirection: "column",
            }}
          >
            <Typography
              variant="h3"
              noWrap
              component="a"
              href="/"
              sx={{
                display: { md: "flex", textAlign: "center" },
                fontFamily: "monospace",
                fontWeight: 2000,
                color: "inherit",
                textDecoration: "none",
              }}
              // style={{
              //   animationName: "fadeInTimer",
              //   animationDuration: "1s",
              //   position: "relative",
              //   animationIterationCount: "infinite",
              // }}
            >
              {this.leading0(this.state.seconds)}
            </Typography>
            Sec
          </div>
          {/* </div> */}
        </div>
      </>
    );
  }
}
export default Clock;
