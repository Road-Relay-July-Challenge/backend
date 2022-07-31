import { Hidden } from "@mui/material";
import React, { Component } from "react";
import Clock from "./Clock";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { deadline: "July, 23, 2022" };
  }
  render() {
    return (
      <div
        style={{
          animationName: "fadeInOpacity",
          animationDuration: "1.5s",
          position: "relative",
          overflow: "hidden",
        }}
      >
        <Clock deadline={this.state.deadline} />
      </div>
    );
  }
}
export default App;
