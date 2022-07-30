import "./App.css";
import MainPage from "./mainPage/mainPage";
import RegisterPage from "./registerPage/registerPage";
import RedirectPage from "./redirectPage/redirectPage";
import RedirectEastWestPage from "./redirectEastWestPage/redirectEastWestPage";
import HallOfFamePage from "./hallOfFame/hallOfFamePage";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import EastOrWestPage from "./eastOrWestPage/eastOrWestPage";
import AchievementPage from "./achievementPage/achievementPage";
import TopAppBar from "./components/topAppBar";
import BottomAppBar from "./components/bottomAppBar";

function App() {
  return (
    <>
      <Router>
        <TopAppBar />
        <div className="App">
          <Routes>
            <Route exact path="/home" element={<MainPage />}></Route>
            <Route exact path="/register" element={<RegisterPage />}></Route>
            <Route
              exact
              path="/HallOfFame"
              element={<HallOfFamePage />}
            ></Route>
            <Route
              exact
              path="/eastOrWest"
              element={<EastOrWestPage />}
            ></Route>
            <Route
              exact
              path="/achievements"
              element={<AchievementPage />}
            ></Route>
            <Route
              path="/redirect/exchange_token"
              element={<RedirectPage />}
            ></Route>
            <Route
              path="/redirect_east_west/exchange_token"
              element={<RedirectEastWestPage />}
            ></Route>
            <Route path="*" element={<Navigate replace to="/home" />} />
          </Routes>
        </div>
        <BottomAppBar />
      </Router>
    </>
  );
}

export default App;
