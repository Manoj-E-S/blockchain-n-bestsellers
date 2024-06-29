import React from "react";
import { Route, Routes } from "react-router-dom";
import Signup from "../Signup";
import Login from "../Login";
import Home from "../pages/Home";
import Layout from "../pages/Layout";
import About from "../pages/About";
import Contact from "../pages/Contact";

const AppRoutes: React.FC = () => {
  return (
    <Routes>
      {/* {Routes with Basic Layout} */}
      <Route path="/" element={<Layout><Home /></Layout>} />
      <Route path="/about" element={<Layout><About /></Layout>} />
      <Route path="/contact" element={<Layout><Contact /></Layout>} />

      {/* {Routes without Basic Layout} */}
      <Route path="/signup" element={<Signup />} />
      <Route path="/login" element={<Login />} />
      
    </Routes>
  );
};

export default AppRoutes;
