import React from 'react';
import { NavLink } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <div className='w-full h-[16vh] bg-cream py-5 pl-10 pr-20 flex items-center justify-between font-raleway font-semibold'>
      <img src="/assets/logo_H2.png" alt="" />
      <div className='flex gap-4'>
        <NavLink 
          to="/" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          Home
        </NavLink>
        <NavLink 
          to="/about" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          About
        </NavLink>
        <NavLink 
          to="/books" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          Books
        </NavLink>
        <NavLink 
          to="/contact" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          Contact Us
        </NavLink>
      </div>
      <div className='flex gap-4'>
        <NavLink 
          to="/login" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          Login
        </NavLink>
        <NavLink 
          to="/signup" 
          className={({ isActive }) => isActive ? "text-gold text-darkBrown hover:text-gold" : "text-darkBrown hover:text-gold"}
        >
          Sign Up
        </NavLink>
      </div>
    </div>
  );
}

export default Header;
