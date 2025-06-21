import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Exercise from "./pages/Exercise";
import Nutrition from "./pages/Nutrition";
import GlobalStyles from "./styles/GlobalStyles";
import styled from "styled-components";

const Nav = styled.nav`
  display: flex;
  gap: 1rem;
  background: #fff;
  padding: 1rem;
`;

export default function App() {
  return (
    <>
      <GlobalStyles />
      <BrowserRouter>
        <Nav>
          <Link to="/">Home</Link>
          <Link to="/exercise">Exercise</Link>
          <Link to="/nutrition">Nutrition</Link>
        </Nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/exercise" element={<Exercise />} />
          <Route path="/nutrition" element={<Nutrition />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}