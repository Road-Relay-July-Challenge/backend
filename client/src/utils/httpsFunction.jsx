import axios from "axios";

const { REACT_APP_CLIENT_ID, REACT_APP_CLIENT_SECRET } = process.env;

export const testAuthGetter = async (authTok) => {
  try {
    const response = await axios.post(
      `https://www.strava.com/api/v3/oauth/token?client_id=${REACT_APP_CLIENT_ID}&client_secret=${REACT_APP_CLIENT_SECRET}&code=${authTok}&grant_type=authorization_code`
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

export const authGetter = async (authTok) => {
  try {
    const response = await axios.get(
      `https://www.rrjc-app.herokuapp.com/auth/verify?code=${authTok}`
    );
    return response.data;
  } catch (error) {
    console.log(error);
  }
};
