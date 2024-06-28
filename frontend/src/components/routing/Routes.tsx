import React from "react";
import { Route, Routes } from "react-router-dom";
import Signup from "../Signup.tsx";
import Login from "../Login.tsx";
import Home from "../pages/Home.tsx";
import Layout from "../pages/Layout.tsx";
import About from "../pages/About.tsx";
import Contact from "../pages/Contact.tsx";

const AppRoutes: React.FC = () => {

  return (
      <Routes>
        {/* Different Pages that use Basic Layout */}
        <Route path="/" element={<Layout><Home /></Layout>} />
        <Route path="/about" element={<Layout><About /></Layout>} />
        <Route path="/contact" element={<Layout><Contact /></Layout>} />
        {/* Pages that dont use Basic Layout */}
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        {/*
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/search" element={<Search />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/getBook" element={<GetBook />} />
        <Route path="/addToExchangeList" element={<AddToExchangeList />} />
        <Route path="/removeFromExchangeList" element={<RemoveFromExchangeList />} />
        <Route path="/exchangeRequest" element={<ExchangeRequest />} />
        <Route path="/approveRequest" element={<ApproveRequest />} />
        <Route path="/rejectRequest" element={<RejectRequest />} />
        <Route path="/getExchangeableBooks/:id" element={<GetExchangeableBooks />} />
        <Route path="/sendCounterOffer" element={<SendCounterOffer />} /> */}
      </Routes>
  );
};

export default AppRoutes;
