import axios from "axios";
// var StravaApiV3 = require("strava_api_v3");
// var defaultClient = StravaApiV3.ApiClient.instance;

export const testAuthGetter = async (authTok) => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/auth/verify?code=${authTok}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
};

export const eastWestAuthGetter = async (authTok, chosenSide) => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/auth/choose_east_or_west?code=${authTok}&chosen_side=${chosenSide}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
};

export const getUserData = async (userID, accessToken) => {
  try {
    const response = await axios.get(
      `https://www.strava.com/api/v3/athletes/${userID}/stats`,
      { headers: { Authorization: `Bearer ${accessToken}` } }
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getUserDetails = async (userId, accessToken) => {
  try {
    const response = await axios.get(`https://www.strava.com/api/v3/athlete`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
        param: { per_page: 5, page: 1 },
      },
    });
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getAllDistance = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/individual/list_all_individual`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getTeamDistance = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/team/list_all_team`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const startOAuth = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/auth/authorize`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getEastWestList = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/team/get_all_east_west_mileage`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getHallOfFame = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/individual/get_hall_of_fame`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getAchievementsCount = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com/team/list_all_team_achievement_count`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};

export const getRankings = async () => {
  try {
    const response = await axios.get(
      `https://rrjc-app.herokuapp.com//individual/get_user_rankings`
    );
    return response;
  } catch (error) {
    console.log(error);
  }
};
