import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 20000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Sends the car data to the backend for prediction
export const predict = async (inputData) => {
  const response = await api.post("/predict", inputData);
  return response.data;
};

// Fetches the system accuracy and confusion matrix
export const getMetrics = async () => {
  const response = await api.get("/metrics");
  return response.data;
};

// Fetches the membership function data for the charts
export const getMembership = async () => {
  const response = await api.get("/membership");
  return response.data;
};

export default api;